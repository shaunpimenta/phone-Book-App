import sqlite3
import sys
import os
from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path
app = Flask(__name__)
temp = None
dict = {'First Name': 'fname', 'Last Name': 'lname', 'Mobile Number': 'mobile'}

def createdatabase():
    try:
        sqliteConnection = sqlite3.connect('PhoneBook.db')
        cursor = sqliteConnection.cursor()
        createtable="create table Phonebook(fname TEXT NOT NULL,lname TEXT,mobile INT(10) UNIQUE)"
        cursor.execute(createtable)
        cursor.close()
        sqliteConnection.commit()
        print("Done")
    except sqlite3.Error as error:
        print("Failed due to", error)

def createuser(fname, lname, phone):
    try:
        sqliteConnection = sqlite3.connect('PhoneBook.db')
        add = f"INSERT into Phonebook values('{fname}','{lname}',{phone})"
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(add)
        cursor.close()
        print("Successful")
        sqliteConnection.commit()
    except sqlite3.Error as error:
        print("Failed due to", error)


def updateuser(change, new, phone):
    try:
        sqliteConnection = sqlite3.connect('PhoneBook.db')
        cursor = sqliteConnection.cursor()
        update = f"UPDATE Phonebook SET {change}='{new}' WHERE mobile={phone};"
        cursor.execute(update)
        cursor.close()
        sqliteConnection.commit()
    except sqlite3.Error as error:
        print("Failed due to", error)


def deleteuser(phone):
    try:
        sqliteConnection = sqlite3.connect('PhoneBook.db')
        cursor = sqliteConnection.cursor()
        delete = f"DELETE from Phonebook where mobile={phone}"
        cursor.execute(delete)
        cursor.close()
        sqliteConnection.commit()
        print('done')
    except sqlite3.Error as error:
        print("Failed due to", error)


def fetchdata():
    try:
        sqliteConnection = sqlite3.connect('PhoneBook.db')
        cursor = sqliteConnection.cursor()
        fetchname = "Select * from Phonebook"
        data = cursor.execute(fetchname).fetchall()
        cursor.close()
        sqliteConnection.commit()
        return data
    except sqlite3.Error as error:
        print("Failed due to", error)


def Main():
    @app.route('/', methods=['GET', 'POST'])
    def index():
        # base="False"
        file = Path("PhoneBook.db")
        if not file.is_file():
            return render_template('index.html',data=[],base="True",len=0)
        else:
            data = fetchdata()
            return render_template('index.html', data=data,len=len(data))

    @app.route('/create')
    def created():
        createdatabase()
        print("Hi")
        return redirect(url_for('index'))
    @app.route('/delete')
    def deleted():
        os.remove('PhoneBook.db')
        return redirect(url_for('index'))

    @app.route('/addcontact', methods=['GET', 'POST'])
    def addcontacts():
        if request.method == 'POST':
            fname = request.form.get('fname')
            lname = request.form.get('lname')
            phone = request.form.get('phone')
            print(fname)
            createuser(fname, lname, phone)
            return redirect(url_for('index'))
        else:
            return render_template('index.html')

    @app.route('/path', methods=['GET', 'POST'])
    def deletecontact():
        if request.method == 'POST':
            a = request.form.get('name')
            a = a.strip()
            data = a.split(" ")
            deleteuser(data[-1])
            return render_template('index.html')
        else:
            return render_template('index.html')

    @app.route('/update', methods=['GET', 'POST'])
    def updatecontact():
        global temp
        global dict
        if temp is None:
            temp = request.form.get('name')
        if request.method == 'POST':
            data1 = request.form.getlist('size')
            data = request.form.get('name1')
            if temp is not None:
                phone = temp.split(" ")
                updateuser(dict[data1[0]], data, phone[-1])
                temp = None
                return redirect(url_for("index", sucess='True'))
            else:
                return render_template('index.html')

    if __name__ == "__main__":
        app.run(debug=True)


if __name__ == '__main__':
    from pathlib import Path
    Main()
