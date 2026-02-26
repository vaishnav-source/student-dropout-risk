from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load retrained model
with open("model/xgboost_web_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        features = np.array([[
            float(data["attendance"]),
            float(data["avg_score"]),
            int(data["engagement"]),
            float(data["submission_gap"]),
            int(data["fees_status"])
        ]])

        risk = float(model.predict_proba(features)[0][1] * 100)
        risk = round(risk, 2)

        if risk < 30:
            label = "Low Risk"
        elif risk < 70:
            label = "Medium Risk"
        else:
            label = "High Risk"

        return jsonify({
            "risk": risk,
            "label": label
        })

    except Exception as e:
        print("Prediction error:", e)
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)