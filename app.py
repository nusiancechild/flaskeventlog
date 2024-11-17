from flask import Flask, request
import csv
from datetime import datetime

app = Flask(__name__)

# Log user actions to a CSV file
@app.route('/log', methods=['POST'])
def log_action():
    data = request.json
    with open('user_actions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for action in data:
            writer.writerow([action['action'], action['timestamp'], datetime.now().isoformat()])
    return 'Logged successfully', 200

if __name__ == '__main__':
    app.run(debug=True)
