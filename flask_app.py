from flask import Flask, render_template, url_for

app = Flask(__name__)
"""
Author: Mark K.
DESC: Scaffold flask_app
"""

@app.route('/')
def index():
    return render_template('index.html')

#----------------------------------------------------------------------

# run the application. Turn off this debug in prod.
if __name__ == '__main__':
    app.run(port=5000, debug=True)
