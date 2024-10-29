from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Conversion functions (same as before)

def convert_length(value, from_unit, to_unit):
    length_units = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1,
        'kilometer': 1000,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34
    }
    return value * (length_units[from_unit] / length_units[to_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'milligram': 0.001,
        'gram': 1,
        'kilogram': 1000,
        'ounce': 28.3495,
        'pound': 453.592
    }
    return value * (weight_units[from_unit] / weight_units[to_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        return value * 9/5 + 32 if to_unit == 'Fahrenheit' else value + 273.15
    elif from_unit == 'Fahrenheit':
        return (value - 32) * 5/9 if to_unit == 'Celsius' else (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        return value - 273.15 if to_unit == 'Celsius' else (value - 273.15) * 9/5 + 32

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    value = float(request.form['value'])
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit']
    category = request.form['category']

    if category == 'length':
        converted_value = convert_length(value, from_unit, to_unit)
        result = f"{value} {from_unit} = {converted_value:.2f} {to_unit}"
    elif category == 'weight':
        converted_value = convert_weight(value, from_unit, to_unit)
        result = f"{value} {from_unit} = {converted_value:.2f} {to_unit}"
    elif category == 'temperature':
        converted_value = convert_temperature(value, from_unit, to_unit)
        result = f"{value} {from_unit} = {converted_value:.2f} {to_unit}"
    else:
        return redirect(url_for('index'))

    return render_template('result.html', result=result, category=category)

@app.route('/length')
def length():
    return render_template('length.html')

@app.route('/weight')
def weight():
    return render_template('weight.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')

if __name__ == '__main__':
    app.run(debug=True)