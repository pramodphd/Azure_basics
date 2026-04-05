from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Aparnaa Loves Pramod very deeply , she will kiss him very foundly till his life and he is gonna enjoy it "
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
