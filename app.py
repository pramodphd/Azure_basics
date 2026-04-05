from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Aparnaa Love Pramod very deeply , she will kiss him very deeply till his life"
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
