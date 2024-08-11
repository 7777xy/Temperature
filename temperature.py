from flask import Flask

app = Flask(__name__)


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


@app.route('/f')
@app.route('/f/<celsius_string>')
def convert(celsius_string):
    """Convert Celsius to Fahrenheit via a URL."""
    try:
        celsius = float(celsius_string)
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        return f"<h1>{fahrenheit:.2f}</h1>"
    except ValueError:
        return "<h1>Invalid input! Please enter a valid number.</h1>"


# http://127.0.0.1:5000/f/100.2

if __name__ == '__main__':
    app.run()