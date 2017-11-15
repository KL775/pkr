from flask import Flask, render_template
import psycopg2 as pg2

conn = pg2.connect(database='dvdrental', user='postgres',password = "*NewYork77")
cur = conn.cursor()
app = Flask(__name__)

@app.route('/')
def home():
	cur.execute("select amount from payment")
	x = cur.fetchmany(10);
	print (x[:3])
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug = True)