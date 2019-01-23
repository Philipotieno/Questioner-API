from flask import Blueprint, jsonify, request

from app.api.v2.models.commentsmodel import Comment
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from app.api.v2.models.db import Database

v2_comments = Blueprint('v2_comments', __name__)

db = Database()
cur = db.cur


@v2_comments.route('', methods=['POST'])
@jwt_required
def post_comments():
    '''function to post comments'''
    # try:
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No json data entered!'}), 401

    if not data or not data["body"] or not data["user_id"] or not data["question_id"]:
        return jsonify({'message': 'All fields are required!'}), 400
    comments_details = Comment(
        data['body'],
        data['user_id'],
        data['question_id'],
    )

    new_comment = comments_details.post_comment()
    return jsonify({'message': 'Comment posted successfully!', "data" : new_comment}), 201

    # except Exception as e:
    #     return jsonify({'message': 'Body cannot be empty enter valid data'}), 400


@v2_comments.route('', methods=['GET'])
def view_all_comments():
	'''function to get all comments'''
	comment = Comment.get_all_comments()
	if comment:
		return jsonify({'Comment': comment}), 200
	return jsonify({'message': 'No comments available!'}), 404