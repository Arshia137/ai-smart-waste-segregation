from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

def classify_waste(item):
    item = item.lower()

    if item in ["banana peel", "food waste", "vegetable waste"]:
        return "Wet Waste  - Put in compost bin"
    elif item in ["plastic bottle", "paper", "cardboard","bottle"]:
        return "Dry Waste  - Recyclable bin"
    elif item in ["battery", "charger", "mobile","electronics"]:
        return "E-Waste  - E-waste collection center"
    elif item in ["medicine", "chemical"]:
        return "Hazardous Waste!!- Safe disposal required"
    else:
        return "Unknown waste ? - Check local guidelines"
    
@app.route("/")
def home():
    return render_template_string("""
    <h2>AI Smart Waste Segregation Guide</h2>

    <form method="post" action="/classify-form">
        <input name="item" placeholder="Enter waste item" required>
        <button type="submit">Check</button>
    </form>
    """)

@app.route("/classify", methods=["POST"])
def classify():
    data = request.json
    item = data.get("item", "")
    result = classify_waste(item)
    return jsonify({"result": result})

@app.route("/classify-form", methods=["POST"])
def classify_form():
    item = request.form.get("item")
    result = classify_waste(item)

    return f"""
    <h3>Result:</h3>
    <p>{result}</p>
    <a href="/">Go Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
