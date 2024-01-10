## Flask Method to Deploy

import pandas as pd
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home_page():
    result = ''
    if request.method == 'POST':
        model = pd.read_pickle('loan_model.pickle')
        cols = model.feature_names_in_
        query_data = []
        for col in cols:
            # query = eval(input(f'Enter {col}: '))
            query = eval(request.form[col])
            query_data.append(query)

        query_df = pd.DataFrame([query_data], columns=cols)
        result = model.predict(query_df).tolist()[0]
        result = 'probable' if result==1 else 'Not probable'
        result = f'This Customer is {result} for Personal Loan'

    return render_template('index.html', result = result)

app.run(debug=True)

