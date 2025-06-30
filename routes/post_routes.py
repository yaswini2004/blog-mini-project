from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, make_response, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from models.post import Post, db, User
import uuid, jwt
from datetime import datetime, timedelta, timezone

from controllers.post_controller import (
    list_posts, get_post, create_post, update_post, list_drafts
)

post_bp = Blueprint('posts', __name__, url_prefix='/posts')
@post_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'message': 'User already exists. Please login.'}), 400

        hashed_password = generate_password_hash(password)
        new_user = User(public_id=str(uuid.uuid4()), name=name, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('posts.login'))

    return render_template('register.html')

@post_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid email or password'}), 401

        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.now(timezone.utc) + timedelta(hours=1)},
                           current_app.config['SECRET_KEY'], algorithm="HS256")

        response = make_response(redirect(url_for('posts.show_posts')))
        response.set_cookie('jwt_token', token)

        return response

    return render_template('login.html')

@post_bp.route('/', methods=['GET'])
def show_posts():
    posts = list_posts(published=True)
    return render_template('posts.html', posts=posts)

@post_bp.route('/<int:post_id>', methods=['GET'])
def post_detail(post_id):
    post = get_post(post_id)
    return render_template('post_detail.html', post=post)

@post_bp.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        form = request.form
        return create_post(form)
    return render_template('post_form.html', post=None)

@post_bp.route('/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    if request.method == 'POST':
        form = request.form
        return update_post(post_id, form)
    post = get_post(post_id)
    return render_template('post_form.html', post=post)

@post_bp.route('/drafts', methods=['GET'])
def drafts():
    posts = list_drafts()
    return render_template('posts.html', posts=posts)
