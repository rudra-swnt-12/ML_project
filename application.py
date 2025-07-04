from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import sys
import os

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
 
application = Flask(__name__)
app = application

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
@app.route('/aboutus', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        print(results)
        # Extract values to pass to template
        option1 = data.gender
        option2 = data.race_ethnicity
        option3 = data.parental_level_of_education
        option4 = data.lunch
        option5 = data.test_preparation_course
        option6 = data.reading_score
        option7 = data.writing_score

        return render_template(
            'result.html',
            results=results[0],
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            option5=option5,
            option6=option6,
            option7=option7
        )

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

