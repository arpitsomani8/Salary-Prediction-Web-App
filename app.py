from flask import Flask

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():

    return "Lets Begin!"


if __name__ == "__main__":
    app.run(debug=True)
