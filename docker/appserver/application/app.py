import time
import mysql.connector
from mysql.connector import errorcode
from flask import Flask
from flask import render_template
from datetime import datetime
app = Flask(__name__)

def get_hit_count():
    retries = 5
    while True:
        try:
            cnx = mysql.connector.connect(user='user', password='password',
                                          host='database',
                                          database='venera_test')
            cursor = cnx.cursor()
            add_access = ("INSERT INTO access_journal (id,access_time,firstname,lastname) VALUES (%s, now(), %s, %s)")
            cursor.execute(add_access, (1,'Tester','Testovic'))
            cnx.commit()
            cursor.execute('SELECT COUNT(*) FROM access_journal')
            total_records = cursor.fetchone()
            cursor.close()
            cnx.close()
            return total_records[0]
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            if retries == 0:
                raise err
            retries -= 1
            time.sleep(0.5)

def get_table():
    retries = 5
    while True:
        try:
            cnx = mysql.connector.connect(user='user', password='password',
                                          host='database',
                                          database='venera_test')
            cursor = cnx.cursor()
            cursor.execute('SELECT id,access_time,firstname,lastname FROM access_journal')
            data = cursor.fetchall()
            cursor.close()
            cnx.close()
            return data
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            if retries == 0:
                raise err
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    data = get_table()
    return render_template('template.html', output_data = data, hits_count = count)
#    return 'This page was viewed {} times.\n'.format(count)