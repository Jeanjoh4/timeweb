from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def show_time():
    current_time = datetime.now().strftime('%b %d, %Y, %H:%M')
    return current_time

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8086)

