from flask import Flask, render_template
from data import departures, tours

app = Flask(__name__)

@app.route("/")
def index():
    """Головна сторінка"""
    return render_template("index.html", departures=departures, tours=tours)

@app.route("/departures/<departure_code>")
def departure(departure_code):
    """Сторінка відображення турів для вибраного міста"""
    city_name = departures.get(departure_code, "Unknown location")
    city_tours = {key: tour for key, tour in tours.items() if tour["departure"] == departure_code}
    return render_template("departure.html", city_name=city_name, tours=city_tours)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/kyiv")
def kyiv_tours():
    return render_template("tour.html", title="З Києва")

@app.route("/lviv")
def lviv_tours():
    return render_template("tour.html", title="Зі Львова")

@app.route("/odesa")
def odesa_tours():
    return render_template("tour.html", title="З Одеси")

@app.route("/chernihiv")
def chernihiv_tours():
    return render_template("tour.html", title="З Чернігова")

@app.route("/chernivtsi")
def chernivtsi_tours():
    return render_template("tour.html", title="З Чернівців")

if __name__ == "__main__":
    app.run(debug=True)