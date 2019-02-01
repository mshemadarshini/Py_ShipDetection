import sys, os, importlib
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from Ship_Statistic import MyShip_DB


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\hselvaraju2\\PycharmProjects\\WebAutoScreenshot\\01_PyLondon\\me_code\\pythonship01.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'

db = SQLAlchemy(app)
db_file = os.getcwd() + "\pythonship01.db"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ships')
def show_table():
    conn = MyShip_DB.create_connection(db_file)
    data_table= MyShip_DB.show_table(conn,'Ship_Txn_new')
    return data_table


@app.route('/api/positions/<imo>/')
def ship_position():
    return


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5012,debug=True)
