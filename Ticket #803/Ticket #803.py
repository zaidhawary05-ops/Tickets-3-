from flask import Flask,request

app = Flask(__name__)

@app.route("/weather")

def weather():
    city = request.args.get("city", "")
    if not city:
        return "error"
    if not city.replace(" ", "").isalpha():
        return "error"


    return f"Sunny in {city}"
