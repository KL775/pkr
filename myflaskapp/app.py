from flask import Flask, render_template
import data
import psycopg2 as pg2

conn = pg2.connect(database='dvdrental', user='postgres',password = "*NewYork77")
cur = conn.cursor()
app = Flask(__name__)

pricing = data.prices()
@app.route('/')
def home():
	cur.execute("select amount from payment")
	x = cur.fetchmany(10);
	print (x[:3])
	return render_template('home.html')

@app.route('/pricing')
def prices():
	return render_template('pricing.html', pricing = pricing)

@app.route('/pricing/<string:id>/')
def plan(id):
	plan = pricing[0]
	for price in pricing:
		if price['id'] == id:
			plan = price
			break
	return render_template('plan.html', plan=plan)


if __name__ == '__main__':
	app.run(debug = True)