from flask import Flask, jsonify
import lent_logic.findingPaschaAndLent as fpl

app = Flask(__name__)

pascha_date = fpl.pascha_date


@app.route('/', methods=['GET'])
def get_pascha_date():
    # Your Python logic here to calculate the date

    return jsonify({"pascha_date": pascha_date})


if __name__ == '__main__':
    app.run(debug=False)
