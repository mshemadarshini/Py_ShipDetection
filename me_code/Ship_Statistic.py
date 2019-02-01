
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,sqlite3, csv, os
from sqlite3 import Error

class MyShip_DB:

    def create_connection(self,db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None

    def create_table(self,conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def main(self):
        database = os.getcwd()+"/pythonship01.db"
        win_csv_filename= r"C:\Users\hselvaraju2\PycharmProjects\WebAutoScreenshot\01_PyLondon\me_code\positions.csv"
        unix_csv_filename = os.getcwd()+"/positions.csv"
        files_to_use_unix= os.path.join("me_code","positions.csv")
        sql_create_ship_info_table = """ CREATE TABLE IF NOT EXISTS Ship_Info (
                                            IMO  integer PRIMARY KEY,
                                            Ship_Name text NOT NULL ); """


        sql_create_ship_NEW_txn_table = """ CREATE TABLE IF NOT EXISTS Ship_Txn_new (
                                        ShipTxn_Id	INTEGER NOT NULL PRIMARY KEY ,
                                        IMO  INTEGER NOT NULL,
                                        ShipTxn_Timestamp	INTEGER NOT NULL,
                                        ShipTxn_​latitude​	INTEGER NOT NULL,
                                        ​ShipTxn_​longitude	INTEGER NOT NULL,
                                        FOREIGN KEY(ShipInfo_ID) REFERENCES Ship_Info(Ship_ID)
                                        ); """

        conn = self.create_connection(database)
        if conn is not None:
            # create table for ship Info and Ship Txn Details table
            self.create_table(conn, sql_create_ship_info_table)
            self.create_table(conn, sql_create_ship_NEW_txn_table)
            self.insert_csv_into_db(conn,unix_csv_filename)
            print("=================================================")
            self.show_table(conn, "Ship_Txn_new")
        else:
            print("Error! cannot create the database connection.")

    def show_table(self,conn,tablename):
        """ TO enter the data from csv file into db
            :param conn:
            :param tablename:
            :return:
            """
        c = conn.cursor()
        show_table_Command= "select * from " + tablename + ";"
        try:
            c = conn.cursor()
            c.execute(show_table_Command)
            print(c.fetchall())
        except Error as e:
            print(e)


    def insert_csv_into_db(self,conn,csvfilename):
        """ TO enter the data from csv file into db
        :param conn:
        :param csvfilename:
        :return:
        """
        c = conn.cursor()
        insert_command="INSERT INTO 'Ship_Txn_new'('ShipInfo_ID','ShipTxn_Timestamp','ShipTxn_​latitude​','​ShipTxn_​longitude')VALUES (?,?,?,?)"
        try:
            with open(csvfilename,"r") as f:
                # listdata = csv.reader(f)
                reader = csv.reader(f, delimiter=',',quotechar='|')
                for data in f:
                    for i in reader:
                        to_db = [(i[0], i[1],i[2],i[3])]
                        newfile = c.executemany(insert_command, to_db)
                        print(to_db)
                c.close()
        except Error as e:
            print(e)


if __name__ == '__main__':
    # MyShip_DB().main()

    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    sys.path.append(r'C:\Users\hselvaraju2\PycharmProjects\WebAutoScreenshot\01_PyLondon\me_code\r2.py')

