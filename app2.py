from flask import Flask, render_template, request
from quiz_generator import generate_quiz

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    quiz = []

    if request.method == "POST":
        topic = request.form["topic"]
        num = int(request.form["num"])
        quiz = generate_quiz(topic, num)

    return render_template("index.html", quiz=quiz)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)