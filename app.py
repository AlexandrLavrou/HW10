from flask import Flask

import utils

app = Flask(__name__)

file_path = 'https://jsonkeeper.com/b/DYDL'


@app.route("/")
def main():
    return utils.good_looking_candidates(file_path)


@app.route("/skills/<input_skill>/")
def skills(input_skill):
    return f"<h3>{utils.get_candy_with_skill(input_skill, file_path)}"


@app.route("/candidate/<input_id>/")
def identification(input_id):
    return f"<h3>{utils.get_candy_from_id(input_id, file_path)}"


app.run()
