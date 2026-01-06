from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1

    if score <= 2:
        return "Weak", 25, "danger"
    elif score == 3 or score == 4:
        return "Medium", 60, "warning"
    else:
        return "Strong", 100, "success"

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    percent = 0
    color = ""

    if request.method == "POST":
        password = request.form.get("password")
        strength, percent, color = check_strength(password)

    return render_template(
        "index.html",
        strength=strength,
        percent=percent,
        color=color
    )

if __name__ == "__main__":
    app.run(debug=True)
