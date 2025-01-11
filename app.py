import mysql.connector
from flask import Flask,render_template,request

db = mysql.connector.connect(host="Planetfitness.mysql.pythonanywhere-services.com",user="Planetfitness",password="password@1",database="Planetfitness$fitness")

app = Flask(__name__)


@app.route('/')
def index():


    return render_template('home.html')


@app.route('/district', methods=['GET'])
def district():
    district = request.args.get('district')
    cursor = db.cursor()
    cursor.execute("select * from health_clubs where district = %s", (district,))
    clubs = cursor.fetchall()

    cursor.execute("select * from activities where district = %s", (district,))
    
    activities = cursor.fetchall()

    return render_template('district.html', district=district, clubs=clubs, activities=activities)


@app.route('/clubs', methods=['GET'])
def filter():
    
    district = request.args.get('district')
    gender = request.args.get('gender')
    cursor = db.cursor()

    if gender:
        cursor.execute("select * from health_clubs where district = %s AND gender = %s", (district, gender))
    else:
        cursor.execute("select * from health_clubs where district = %s", (district,))
    clubs = cursor.fetchall()

    cursor.execute("select * from activities where district = %s", (district,))
    activities = cursor.fetchall()

    return render_template('district.html', district=district, clubs=clubs, activities=activities)



if __name__ == '__main__':
    app.run("0.0.0.0", 9000)