# test_hello_add.py
from API import app
from flask import json

def test_predict():        
    response = app.test_client().post(
        '/predict',
        data=json.dumps({"gender":["Male"],
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
                     "AddServices":["-1.757234"]
}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['sum'] == 3

    print(data)
