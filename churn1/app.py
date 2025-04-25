from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Charger le modèle entraîné
model = joblib.load('bestchurn.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    
        data = [
             int(request.form['RowNumber']),
            int(request.form['CreditScore']),
            0 if request.form['Geography'] == 'France' else 1 if request.form['Geography'] == 'Germany' else 2,
            1 if request.form['Gender'] == 'Male' else 0,
            int(request.form['Age']),
            int(request.form['Tenure']),
            float(request.form['Balance']),
            int(request.form['NumOfProducts']),
            1 if request.form['HasCrCard'] == 'True' else 0,
            1 if request.form['IsActiveMember'] == 'True' else 0,
            float(request.form['EstimatedSalary']),
            float(request.form['balance_salary_ratio']),
            float(request.form['tenure_age_ratio'])
        ]

        features = np.array([data])
        prediction = model.predict(features)[0]
        resulta ='Client va churn' if prediction == 1 else 'Client reste'

        return render_template('index.html',prediction_text=resulta)

    

if __name__ == '__main__':
    app.run(debug=True)
