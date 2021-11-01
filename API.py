from flask import Flask,jsonify,request
import pandas as pd
import numpy as numpy
import traceback
from catboost import CatBoostClassifier

app = Flask(__name__)

@app.route("/")
def hello():
    json_ = {"gender":["Male"],
                     "SeniorCitizen":["0"],
                     "Partner":["0"],
                     "Dependents":["0"],
                     "tenure":["-0.223317"],
                     "MultipleLines":["-0.508112"],
                     "InternetService":["No"],
                     "Contract":["Month-to-month"],
                     "PaperlessBilling":["1"],
                     "PaymentMethod":["Electronic check"],
                     "MonthlyCharges":["-1.512322"],
                     "AddServices":["-1.757234"]}
    data = pd.DataFrame
    ##return("Welcome")
    print(data)
    return(data)



@app.route('/predict',methods=['POST'])
def predict():
    prediction = CatB.predict(data)
    return jsonify({'prediction': list(prediction)})




if __name__ == '__main__':
    from_file = CatBoostClassifier()
    CatB = from_file.load_model("model")
    print("Model Loaded")
    app.run(debug=True)

