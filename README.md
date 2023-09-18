# azure_flask_deployment: 
Azure flask deployment (https:// angeliki-504-flask.azurewebsites.net)

## First create your repo
- Go to your GitHub account and create a repo in this case named ```azure_flask_deployment```.
- Then open your Google Shell environment
- Git clone with the url of your repo
- Start adding content and information based on the desired outcome. In this case, the following content and changes were made:

## Create in google cloud shell the following:
- Create an ```app.py``` file where it will hold the root python codes for the flask app. In this case, the following was included:
- First import the packages ```flask```, ```random``` and ```faker```
- Then follow the format ```@app.route('/___.html')``` and fill in the name of the tab you want to be created within the homebase ('/').
( In this case: ```@app.route('/about')```, ```@app.route('/data')```, ```@app.route('/random')```, ```@app.route('/random')```)
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
## Creating the base.html format and following the same for the rest of the tabs:
- Part of the code below depicts the way you can create the tabs within your base and name them as well with including editing of the text color and format.
- When creating the rest of tabs such as About, Data etc. you need to extend the code from the ```base.html``` to integrate it under the following commands with ```{% extends "base.html" %} ```.
```
<!--Below are the tabs created inside the app: Home, About, Data, Random Stuff-->
            <ul class="flex space-x-4">
                <li><a href="/" class="hover:underline text-white">Home</a></li>
                <li><a href="/about" class="hover:underline text-white">About</a></li>
                <li><a href="/data" class="hover:underline text-white">Data</a></li>
                <li><a href="/random" class="hover:underline text-white">Random Stuff</a></li>```
```
## Then save all your progress to your repo through the following commands:
- ```git add .```, ```git commit -m "___"```, ```git push```

# Azure Deployment:
## In order to deploy your flask app through Azure the following commands need to be used in the google shell cloud environment
- First visit portal.Azure login page and create an account
- There you will have to go to resource groups ( also shown in app services) and create a resource group with a unique name
- After that going into your google shell environment you will need to type the following commands while making sure you are in the right location (can use ```ls``` and ```cd__``` to locate and move to the correct folder:
    - 
