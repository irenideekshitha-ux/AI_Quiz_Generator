from flask import Flask, render_template, request
from quiz_generator import generate_quiz

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    quiz = []
    topic = "Python"
    num = 5

    if request.method == "POST":
        topic = request.form.get("topic", "Python")
        num = int(request.form.get("num", 5))

        # Allow a maximum of 30 questions
        num = max(1, min(num, 30))

        quiz = generate_quiz(topic, num)

    return render_template(
        "index.html",
        quiz=quiz,
        topic=topic,
        num=num
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)