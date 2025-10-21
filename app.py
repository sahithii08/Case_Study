from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Simple in-memory storage for reminders
reminders = []

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        name = request.form.get('name')
        time = request.form.get('time')

        if name and time:
            reminders.append({'name': name, 'time': time})
            message = "Medicine reminder added successfully!"
        else:
            message = "Please fill out all fields."

    # Check for medicines due now
    current_time = datetime.now().strftime("%H:%M")
    due = [r for r in reminders if r['time'] == current_time]

    return render_template('index.html', reminders=reminders, due=due, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
