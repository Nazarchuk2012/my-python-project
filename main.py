from flask import Flask, render_template
import os

app = Flask(__name__)


# === ROUTES =================
@app. route('/')
def index():
        return render_template('index.html')

# Запуск програми
if __name__ == '__main__':
    app.run(debug=True)
