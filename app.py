from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained model
filename = 'rf_raw_model.pkl'
with open(filename, 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Extract input data
        data = {
            'Minimum_Temperature': request.form['min_temp'],
            'Maximum_Temperature': request.form['max_temp'],
            'Temperature': request.form['temp'],
            'Dew_Point': request.form['dew_point'],
            'Relative_Humidity': request.form['humidity'],
            'Wind_Speed': request.form['wind_speed'],
            'Wind_Direction': request.form['wind_direction'],
            'Precipitation': request.form['precipitation'],
            'Visibility': request.form['visibility'],
            'Cloud_Cover': request.form['cloud_cover'],
            'Sea_Level_Pressure': request.form['pressure']
        }

        # Convert data to DataFrame
        df = pd.DataFrame([data])

        # Convert data types to numeric
        df = df.apply(pd.to_numeric)

        # Make prediction using the model
        prediction = model.predict(df)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
