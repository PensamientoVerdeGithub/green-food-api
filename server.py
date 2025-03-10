from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def headers():
    return f"<pre>{request.headers}</pre>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
