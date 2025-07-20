from flask import Flask, render_template_string, request
import joblib
import pandas as pd

# Create Flask app
app = Flask(__name__)

# Load the trained pipeline (model.pkl contains both the preprocessor and model)
model = joblib.load('model (2).pkl')

# HTML template with embedded CSS
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Price Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #f3f4f6;
        }
        .container {
            width: 50%;
            margin: 5% auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        h1 {
            text-align: center;
            color: #333333;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        input, select, button {
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            border: 1px solid #cccccc;
        }
        button {
            background: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background: #eaf5ea;
            color: #2d7b2d;
            text-align: center;
            font-size: 18px;
            border: 1px solid #c3e6cb;
            border-radius: 5px;
        }
        .error {
            margin-top: 20px;
            padding: 10px;
            background: #f8d7da;
            color: #721c24;
            text-align: center;
            font-size: 18px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Car Price Prediction</h1>
        <form method="POST" action="/predict">
            <input type="text" name="name" placeholder="Car Name (e.g., Honda City)" required>
            <input type="text" name="company" placeholder="Car Company (e.g., Honda)" required>
            <input type="number" name="year" placeholder="Manufacture Year (e.g., 2015)" required>
            <input type="number" name="kms_driven" placeholder="Kilometers Driven (e.g., 45000)" required>
            <select name="fuel_type" required>
                <option value="">Select Fuel Type</option>
                <option value="Petrol">Petrol</option>
                <option value="Diesel">Diesel</option>
                <option value="CNG">CNG</option>
                <option value="LPG">LPG</option>
                <option value="Electric">Electric</option>
            </select>
            <button type="submit">Predict Price</button>
        </form>
        {% if prediction_text %}
        <div class="result">
            {{ prediction_text }}
        </div>
        {% endif %}
        {% if error_text %}
        <div class="error">
            {{ error_text }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs
        name = request.form['name']
        company = request.form['company']
        year = int(request.form['year'])
        kms_driven = int(request.form['kms_driven'])
        fuel_type = request.form['fuel_type']
        
        # Prepare input as a DataFrame (to match training format)
        input_data = pd.DataFrame([[name, company, year, kms_driven, fuel_type]],
                                  columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
        
        # Make prediction using the loaded pipeline
        prediction = model.predict(input_data)
        predicted_price = round(prediction[0][0], 2)  # Round to 2 decimal places
        
        return render_template_string(html_template, prediction_text=f"Predicted Price: ₹{predicted_price}")
    except Exception as e:
        # Handle any errors that occur
        return render_template_string(html_template, error_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
