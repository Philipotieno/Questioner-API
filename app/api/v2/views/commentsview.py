from flask import Blueprint, jsonify, request

from app.api.v2.models.commentsmodel import Comment
from app.api.v2.models.questionsmodel import Question
from app.api.v2.models.usersmodels import User
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from app.api.v2.models.db import Database

v2_comments = Blueprint('v2_comments', __name__)

db = Database()
cur = db.cur


@v2_comments.route('', methods=['POST'])
@jwt_required
def post_comments(question_id):
    '''function to post comments'''
    qns = Question.get_specific_question(question_id)
    if not qns:
        return jsonify({'message': 'question not found!'}), 404

    username = get_jwt_identity()
    user = User.get_user_by_name(username)

    data = request.get_json()
    if not data:
        return jsonify({'message': 'No json data entered!'}), 401

    if not data or not data["body"] or " ":
        return jsonify({'message': 'All fields are required!'}), 400

    query = "SELECT user_id, question_id, body FROM comments;"
    cur.execute(query)
    cmts = cur.fetchall()
    for cmts in cmts:
        if cmts['user_id'] == user['user_id'] and cmts['question_id'] == qns['question_id'] \
        and cmts['body'] == data['body']:
            return jsonify({'message': 'Such a comment already exist for that question'}), 409

    comments_details = Comment(
        data['body'],
        user['user_id'],
        qns['question_id']
    )

    new_comment = comments_details.post_comment()
    if new_comment:
        return jsonify({'status':201,'message': 'Comment posted successfully!', "data" : new_comment}), 201
    return jsonify({'status':409,'message': 'Comment already exist for that question!'}), 409
