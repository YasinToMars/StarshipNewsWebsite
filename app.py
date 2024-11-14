from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/multicam')
def multi_cam():
    return render_template('multicam.html')

# Route for the closures page
@app.route('/closures')
def closures():
    conn = sqlite3.connect('closures.db')
    cursor = conn.cursor()
    cursor.execute("SELECT closure_name, closure_date FROM closures")
    closures_data = cursor.fetchall()
    conn.close()
    
    return render_template("closures.html", closures=closures_data)

@app.route('/news')
def news():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)
