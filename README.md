# azure_flask_deployment
Azure flask deployment

## First create your repo
- Go to your GitHub account and create a repo in this case named ```azure_flask_deployment```.
- Then open your Google Shell environment
- Git clone with the url of your repo
- Start adding content and information based on the desired outcome. In this case, the following content and changes were made:

## Create in google cloud shell the following:
- Create an ```app.py``` file where it will hold the root python codes for the flask app. In this case, the following was included:
- First import the packages ```flask```, ```random``` and ```faker```
- Then following the format ```@app.route('/___.html')``` and filling in the name of the tab you want to be created within the homebase ('/').
( In this case: ```@app.route('/about')```, ```@app.route('/data')```, ```@app.route('/random')```)
```
from flask import Flask, render_template
import random
from faker import Faker

fake = Faker()

# small change

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/data')
def datapage():
    return render_template('data.html')

@app.route('/random')
def randomnumber():
    number_var = random.randint(1, 10000)
    fake_address = fake.address()
    return render_template('random.html', single_number = number_var, single_address = fake_address)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )
```

