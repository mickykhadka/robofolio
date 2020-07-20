from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def pages(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        # print(data)
        write_to_csv(data)
    return redirect('/thankyou.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')
        print(file)


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
