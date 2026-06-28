from __future__ import annotations

from flask import Flask, render_template, request

from .predictor import Predictor


def register_routes(app: Flask, predictor: Predictor) -> None:
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/predict", methods=["POST", "GET"])
    def predict():
        if request.method == "POST":
            symptoms = request.form.get("symptoms", "")
            user_symptoms = [s.strip("[]' ") for s in symptoms.split(",") if s.strip()]
            predicted_disease = predictor.predict(user_symptoms)
            pre, die = predictor.get_recommendations(predicted_disease)
            return render_template(
                "index.html",
                predicted_disease=predicted_disease,
                dis_pre=pre,
                dis_diet=die,
                submitted=True,
            )
        return render_template("index.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")
