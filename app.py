# app.py

from flask import Flask, render_template, request, jsonify
from modules.agent import TaskBuddyAgent

app = Flask(__name__)
agent = TaskBuddyAgent()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"response": "Please enter a valid message."})
    
    response = agent.act(agent.observe(user_input))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
