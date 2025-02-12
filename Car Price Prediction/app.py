from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model (assuming 'random_forest_model.pkl' is in the same directory)
model = joblib.load('random_forest_model.pkl')

# List of unique car names
car_names = sorted(list(set([
    'ritz', 'sx4', 'ciaz', 'wagon r', 'swift', 'vitara brezza', 's cross', 'alto 800', 'ertiga', 'dzire', '800', 
    'alto k10', 'ignis', 'baleno', 'omni', 'fortuner', 'innova', 'corolla altis', 'etios cross', 'etios g', 
    'etios liva', 'etios gd', 'camry', 'land cruiser', 'Royal Enfield Thunder 500', 'UM Renegade Mojave', 
    'KTM RC200', 'Bajaj Dominar 400', 'Royal Enfield Classic 350', 'KTM RC390', 'Hyosung GT250R', 
    'Royal Enfield Thunder 350', 'KTM 390 Duke', 'Mahindra Mojo XT300', 'Bajaj Pulsar RS200', 
    'Royal Enfield Bullet 350', 'Royal Enfield Classic 500', 'Bajaj Avenger 220', 'Bajaj Avenger 150', 
    'Honda CB Hornet 160R', 'Yamaha FZ S V 2.0', 'Yamaha FZ 16', 'TVS Apache RTR 160', 'Bajaj Pulsar 150', 
    'Honda CBR 150', 'Hero Extreme', 'Bajaj Avenger 220 dtsi', 'Bajaj Avenger 150 street', 'Yamaha FZ v 2.0', 
    'Bajaj Pulsar NS 200', 'TVS Apache RTR 180', 'Hero Passion X pro', 'Yamaha Fazer', 'Honda Activa 4G', 
    'TVS Sport', 'Honda Dream Yuga', 'Bajaj Avenger Street 220', 'Hero Splender iSmart', 'Activa 3g', 
    'Hero Passion Pro', 'Honda CB Trigger', 'Yamaha FZ S', 'Bajaj Pulsar 135 LS', 'Honda CB Unicorn', 
    'Hero Honda CBZ extreme', 'Honda Karizma', 'Honda Activa 125', 'TVS Jupyter', 'Hero Honda Passion Pro', 
    'Hero Splender Plus', 'Honda CB Shine', 'Bajaj Discover 100', 'Suzuki Access 125', 'TVS Wego', 
    'Honda CB twister', 'Hero Glamour', 'Hero Super Splendor', 'Bajaj Discover 125', 'Hero Hunk', 
    'Hero Ignitor Disc', 'Hero CBZ Xtreme', 'Bajaj ct 100', 'i20', 'grand i10', 'i10', 'eon', 'xcent', 
    'elantra', 'creta', 'verna', 'city', 'brio', 'amaze', 'jazz'
])))

# Home route to display the form
@app.route('/')
def home():
    return render_template('index.html', car_names=car_names)  # Pass car names to the template

# Route to handle form submission and prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        car_name = request.form['car_name']
        year = int(request.form['year'])
        present_price = float(request.form['present_price'])
        kms_driven = int(request.form['kms_driven'])
        seller_type = request.form['seller_type']
        
        # Process dropdown inputs
        fuel_type = request.form['fuel_type']
        transmission = request.form['transmission']
        
        # Encode the dropdown values as required by the model
        fuel_type_diesel = 1 if fuel_type == 'diesel' else 0
        fuel_type_petrol = 1 if fuel_type == 'petrol' else 0
        seller_type_individual = 1 if seller_type == 'individual' else 0
        seller_type_owner = 1 if seller_type == 'owner' else 0
        transmission_manual = 1 if transmission == 'manual' else 0
        
        # Calculate 'Years_Since_Manufacture'
        years_since_manufacture = 2025 - year
        
        # Prepare the input data for prediction
        input_data = np.array([[year, present_price, kms_driven, fuel_type_diesel, fuel_type_petrol,
                                seller_type_individual, transmission_manual, seller_type_owner, years_since_manufacture]])
        
        # Get the prediction from the model
        prediction = model.predict(input_data)
        
        # Convert the prediction to lakhs (assuming the model predicts in thousands)
        prediction_in_lakhs = prediction[0] / 100
        
        # Render the result on the HTML page
        return render_template('index.html', car_names=car_names, 
                               prediction_text='Estimated Selling Price: ₹{:.2f} Lakhs'.format(prediction_in_lakhs))
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
