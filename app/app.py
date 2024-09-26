from flask import Flask, request
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/vote', methods=['POST'])
def vote():
    vote = request.form['vote']
    r.incr(vote)
    return f"Voted for {vote}!"

@app.route('/results', methods=['GET'])
def results():
    option1 = r.get('option1') or 0
    option2 = r.get('option2') or 0
    return f"Option 1: {int(option1)} votes, Option 2: {int(option2)} votes"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
