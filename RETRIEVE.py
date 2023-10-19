from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

website_url = input("Enter the website url: ")
# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# change string to the name of your database; add path if necessary
db_name = 'students.db'
# note - path is necessary for a SQLite db!!!
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize the app with Flask-SQLAlchemy
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    roll = db.Column(db.Integer, nullable=False)
    passw = db.Column(db.String(20), nullable=False)



def perform_web_automation(username, password):

    webdriver_path = "C:/chromedriver-win32 (1)/chromedriver-win32/chromedriver.exe"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.executable_path = webdriver_path

    browser = webdriver.Chrome(options=chrome_options)

    website_url = website_url
    browser.get(website_url)

    username_field = WebDriverWait(browser, 10).until(
        ec.visibility_of_element_located((By.ID, "username"))
    )

    password_field = browser.find_element(By.ID, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = browser.find_element(By.ID, "loginbtn")
    login_button.click()
    time.sleep(5)




@app.route('/')
def display_data():
        stut = User.query.all()

        for sock in stut:
            perform_web_automation(sock.email, sock.passw)


if __name__ == '__main__':
    app.run(debug=True)
