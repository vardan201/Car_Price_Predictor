# 🚗 Car Price Predictor

This project is a machine learning model that predicts the price of used cars based on features such as car name, manufacturing year, fuel type, kilometers driven, and company. The data used is sourced from Quikr's used car listings.

---

## 🧠 ML Model: Linear Regression with Pipeline

The model uses the following techniques:

- **Data Cleaning & Preprocessing**
- **OneHotEncoding** for categorical features (`name`, `company`, `fuel_type`)
- **Train-Test Split** using the best `random_state` based on R² score
- **Scikit-learn Pipeline** for streamlined preprocessing and model fitting
- **Model & Encoder Serialization** using `joblib`

---

## 📁 Dataset

It includes fields like:
- `name`: Name of the car
- `company`: Manufacturer
- `year`: Manufacturing year
- `Price`: Selling price (target variable)
- `fuel_type`: Type of fuel used (Petrol/Diesel/etc.)
- `kms_driven`: Kilometers the car has been driven
- `owner`: Ownership type (First, Second, etc.)
## 📊 Steps Performed

### 1. **Data Cleaning**
- Removed rows with `"Ask for Price"` or missing numeric values.
- Removed non-numeric values from `year` and `kms_driven`.
- Filtered out outliers where price > ₹60 Lakhs.
- Simplified car names to the first 3 words.

### 2. **Preprocessing**
- Converted `year`, `Price`, and `kms_driven` to integers.
- Used `OneHotEncoder` for categorical columns: `name`, `company`, `fuel_type`.

### 3. **Model Training**
- Used `LinearRegression` from `sklearn`.
- Wrapped all preprocessing and model training steps in a `Pipeline`.
- Ran 1000 iterations with different `random_state` values to choose the best model based on **R² Score**.

### 4. **Model Saving**
- Serialized the trained model (`model.pkl`) and the fitted encoder (`encoder.pkl`) using `joblib`.

---

## 📈 Performance Metric

The model uses **R² score** to evaluate performance. The best random state is selected based on the highest R² score from 1000 trials.

---

## 🛠️ Installation

### Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

Edit
pip install -r requirements.txt

💾 Saved Files
model.pkl → Trained Linear Regression pipeline

encoder.pkl → Fitted OneHotEncoder (for inference)

requirements.txt → Required dependencies

🔮 Future Improvements
Add more features such as engine capacity, mileage, or transmission.

Use more powerful models like RandomForest or XGBoost.


  
