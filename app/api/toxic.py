from app.api import bp
from flask import jsonify

@bp.route('/prediction', methods=['GET'])
def get_sentence_classification():
    return jsonify(dict(toto=1))
