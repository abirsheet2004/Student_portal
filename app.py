from flask import Flask, render_template, request,flash,redirect
import mysql.connector


app = Flask(__name__)

app.secret_key = 'vwqadada$%jeu'
db=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="abir2004",
    database="student"
)
cursor=db.cursor()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            cur =db.cursor()
            cur.execute("INSERT INTO abir (name, address, pin, city ) VALUES (%s, %s, %s, %s)", (nm, addr, city, pin))
            db.commit()
        except Exception as e:
            db.rollback()
            flash("DatabaseError: {str(e)}")
        finally:
            cur.close()
            flash("Scuessfully submit data")
            return redirect("/")

@app.route('/list')
def list():
    cursor=db.cursor()
    cursor.execute("SELECT * FROM abir;")
    alllist=cursor.fetchall()
    print(alllist)
    cursor.close()
    return render_template('list.html',alllist=alllist)


if __name__ == '__main__':
    app.run(debug=True)
