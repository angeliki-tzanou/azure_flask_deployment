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