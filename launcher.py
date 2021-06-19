from flask import Flask,render_template
# from flask_sqlalchemy import SQLALchemy
from mysql.connector import connect, Error

app = Flask(__name__)
# db = SQLALchemy(app)

class DBConnect:
    def __init__(self):
        self.table = "User_Info"
        self.conn = connect(
            host=HOST,
            username=USER,
            password=PASS,
            database=DB
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
            print(userdatas)
        except Error as e:
            print(e)


db = DBConnect()
db.retrieve_all()




# class Item(db.Model):
#     id = db.Column(db.Intreger(), primary_key=True)
#     coin= db.Column(db.String(length=30), nullable=False, unique=True)
#     submonth= db.Column(db.String(length=30), nullable=False,)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/Dashboard')
def Dashboard_page():
    return render_template('Dashboard.html')