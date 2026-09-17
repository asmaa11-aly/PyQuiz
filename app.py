from flask import Flask, render_template, request
from urllib.parse import unquote
from questions import questions

app = Flask(__name__)


# ================= TOPICS PAGE =================

@app.route("/")
@app.route("/topics")
def topics_page():

    topics = []

    topic_info = {
        "Lists": {
            "icon": "▤",
            "class": "purple",
        },
        "Dictionaries": {
            "icon": "◇",
            "class": "blue",
        },
        "Strings": {
            "icon": "Aa",
            "class": "pink",
        },
        "Functions": {
            "icon": "ƒ",
            "class": "green",
        },
        "For loops": {
            "icon": "↻",
            "class": "orange",
        },
        "While loops": {
            "icon": "∞",
            "class": "purple",
        },
        "Tuples": {
            "icon": "()",
            "class": "blue",
        },
        "Sets": {
            "icon": "◉",
            "class": "pink",
        },
        "Lambda / Map / Filter": {
            "icon": "λ",
            "class": "green",
        },
        "Mixed": {
            "icon": "✦",
            "class": "orange",
        },
    }

    for question in questions:

        topic_name = question["topic"]

        if not any(topic["name"] == topic_name for topic in topics):

            count = sum(
                1
                for q in questions
                if q["topic"] == topic_name
            )

            topics.append({
                "name": topic_name,
                "count": count,
                "icon": topic_info[topic_name]["icon"],
                "class": topic_info[topic_name]["class"]
            })

    return render_template(
        "index.html",
        topics=topics
    )


# ================= QUIZ PAGE =================



@app.route("/quiz/<path:topic_name>", methods=["GET", "POST"])
def quiz(topic_name):

    topic_map = {
        "lists": "Lists",
        "dictionaries": "Dictionaries",
        "strings": "Strings",
        "functions": "Functions",
     "for loops": "For loops",
    "while loops": "While loops",
        "tuples": "Tuples",
        "sets": "Sets",
  "lambda / map / filter": "Lambda / Map / Filter",
       
        "mixed": "Mixed"
    }

    topic_name = topic_map.get(topic_name.lower())

    if topic_name is None:
        return "Topic not found", 404

    selected_questions = [
        q for q in questions
        if q["topic"] == topic_name
    ]

    # ================= CHECK ANSWERS =================

    if request.method == "POST":

        score = 0

        for i, question in enumerate(selected_questions):

            user_answer = request.form.get(
                f"question_{i}"
            )

            if user_answer == question["answer"]:
                score += 1

        return render_template(
            "result.html",
            topic=topic_name,
            score=score,
            total=len(selected_questions)
        )

    # ================= SHOW QUIZ =================

    return render_template(
        "quiz.html",
        questions=selected_questions,
        topic=topic_name
    )

# ================= RUN =================

if __name__ == "__main__":
    app.run(debug=True)