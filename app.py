from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/home')
def hello_world():
    return render_template('index.html')

sqlite_connect = sqlite3.connect('developers.db')
connect = sqlite3.connect('developers.db')
connect.execute("CREATE TABLE IF NOT EXISTS PARTICIPANTS (name Text, \
                email Text, city Text, country Text, phone Text)")

@app.route("/join", methods = ["GET", "POST"])
def join():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        country = request.form['country']
        phone = request.form['phone']
        print("hello")
        with sqlite3.connect("developers.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO PARTICIPANTS(name, email, city, country, phone) VALUES (?,?,?,?,?)",
            (name, email, city, country, phone))
            users.commit()
            return render_template('index.html')
    else:
        return render_template('developers.html')


@app.route('/')
def show_db():
    with sqlite3.connect("developers.db") as conn:
        cursor = conn.cursor()
        print(cursor)
        cursor.execute("SELECT * FROM PARTICIPANTS")
        data = cursor.fetchall()
        print(data)
        return render_template('index.html', data=data)






if __name__ == '__main__':
    app.run()