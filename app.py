import pickle
from flask import Flask, request, jsonify,render_template
import ml_functions
import debug
import os
import sys
import logging



#Initialize the flask App
app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

model = pickle.load(open('model.pkl', 'rb'))

#default page of our web-app
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    
    url = request.form['url']
    output = ml_functions.predict_website(url,model) 
    if(output == -1):
        op = "Phishing url"
    else:
        op = "Legitimate Url"
    '''except:
        op = "Phishing url"'''
    return render_template('index.html', prediction_text='The website is  :{}'.format(op))

if __name__ == "__main__":
    app.run(debug=True)
    