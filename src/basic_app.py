from flask import Flask, jsonify
import json
import csv
import pandas as pd


app = Flask(__name__)


# with open('one_piece_characters.json', 'r') as file:
#     characters = json.load(file)


characters = pd.read_csv('one_piece_characters.csv') 


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/characters', methods=['GET'])
def send_json():

    return jsonify(characters.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
