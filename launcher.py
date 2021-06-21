import os

from flask import Flask, render_template
from mysql.connector import connect, Error


app = Flask(__name__)


class DBConnect:
    def __init__(self):
        self.table = "User_Info"
        self.conn = connect(
            host=os.environ.get("DB_HOST", ""),
            username=os.environ.get("DB_USER", ""),
            password=os.environ.get("DB_PASS", ""),
            database=os.environ.get("DB_NAME", "")
        )
        self.cursor = self.conn.cursor()

    def retrieve_all(self):
        sql_statement = 'SELECT * FROM {}'.format(self.table)
        userdatas = []
        try:
            self.cursor.execute(sql_statement)
            records = self.cursor.fetchall()
            for record in records:
                userdata = {
                    "username": record[0],
                    "coin": record[1],
                    "watchtime": record[2],
                    "submonth": record[3]
                }
                userdatas += [userdata]
            return userdatas
        except Error as e:
            print(e)


db = DBConnect()


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/Dashboard')
def Dashboard_page():
    userdatas = db.retrieve_all()
    return render_template('Dashboard.html', rows=userdatas)
