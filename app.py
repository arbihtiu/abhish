from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Abhishek Kumar Assistant professor'

if __name__ == '__main__':
    app.run(port=5000)
