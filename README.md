# Weather Prediction System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.0.3-green)
![HTML](https://img.shields.io/badge/HTML-5-orange)
![CSS](https://img.shields.io/badge/CSS-3-blue)

## Project Overview

The Weather Prediction System is a web-based application designed to forecast weather conditions based on 11 numerical input values. The project was developed between March 2024 and May 2024 using Python, HTML, CSS, and Flask.

## Features

- **User Input**: Accepts 11 numerical input values for predicting weather conditions.
- **Forecast Display**: Outputs predicted weather conditions in a user-friendly format.
- **Responsive Design**: Ensures that the web application is accessible and usable across various devices and screen sizes.

## Tools & Technologies

- **Python**: The core programming language used to build the prediction logic.
- **Flask**: A lightweight WSGI web application framework used for creating the web application.
- **HTML/CSS**: Used for structuring and styling the web pages.

## Installation

To set up the Weather Prediction System locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Afsana-Setu/Weather-Prediction.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Weather-Prediction
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage

1. Input the 11 numerical values in the provided fields.
2. Click the "Predict" button to view the forecasted weather conditions.
3. The predicted weather will be displayed on the same page.

## Project Structure

```
Weather-Prediction/
│
├── templates/
│   └── index.html        # Main page of the application
│
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles for the application
│
├── app.py                # Main Flask application file
├── model.py              # Prediction model logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Future Improvements

- **Integration with Real-Time Weather APIs**: To enhance the prediction accuracy by integrating with live weather data APIs.
- **Advanced UI/UX**: Improve the design and user experience of the web application.
- **Deployment**: Deploy the application to a cloud platform like Heroku or AWS.

## Acknowledgments

- Flask documentation
- Python community for extensive libraries and support

## Project Link

[Weather Prediction System](https://github.com/Afsana-Setu/Weather-Prediction)

---
