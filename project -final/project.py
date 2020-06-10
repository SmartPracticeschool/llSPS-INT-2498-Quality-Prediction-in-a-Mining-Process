import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from joblib import load
app = Flask(__name__)
model = pickle.load(open('qualityprediction.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('iron.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[int(x) for x in request.form.values()]]
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    
    return render_template('iron.html', prediction_text='Silica Concentrate {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
