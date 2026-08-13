from flask import Blueprint, request, jsonify
import requests
from .database import db
from .models import Comment

comment_bp = Blueprint('comments', __name__)

USER_SERVICE_URL = "http://127.0.0.1:8001/api/users"
POST_SERVICE_URL = "http://127.0.0.1:8002/api/posts"

@comment_bp.route('/', methods=['GET'])
def get_comments():
    """
    Barcha izohlarni olish
    ---
    responses:
      200:
        description: Izohlar ro'yxati
    """
    comments = Comment.query.all()
    return jsonify([c.to_dict() for c in comments])

@comment_bp.route('/', methods=['POST'])
def create_comment():
    """
    Yangi izoh yaratish
    ---
    parameters:
      - in: body
        name: body
        schema:
          properties:
            content:
              type: string
            user_id:
              type: integer
            post_id:
              type: integer
    responses:
      201:
        description: Izoh yaratildi
      404:
        description: User yoki Post topilmadi
    """
    data = request.get_json()

    user_response = requests.get(f"{USER_SERVICE_URL}/{data['user_id']}/")
    if user_response.status_code != 200:
        return jsonify({'detail': 'User topilmadi!'}), 404

    post_response = requests.get(f"{POST_SERVICE_URL}/{data['post_id']}/")
    if post_response.status_code != 200:
        return jsonify({'detail': 'Post topilmadi!'}), 404

    user = user_response.json()
    post = post_response.json()

    comment = Comment(
        content=data['content'],
        user_id=data['user_id'],
        post_id=data['post_id']
    )
    db.session.add(comment)
    db.session.commit()

    result = comment.to_dict()
    result['created_by'] = user
    result['post'] = post
    return jsonify(result), 201

@comment_bp.route('/<int:comment_id>/', methods=['GET'])
def get_comment(comment_id):
    """
    Bitta izohni olish
    ---
    parameters:
      - in: path
        name: comment_id
        type: integer
    responses:
      200:
        description: Izoh ma'lumotlari
      404:
        description: Izoh topilmadi
    """
    comment = Comment.query.get_or_404(comment_id)
    return jsonify(comment.to_dict())