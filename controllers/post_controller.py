from flask import flash, redirect, url_for
from models.post import Post, db

def list_posts(published=True):
    return Post.query.filter_by(is_published=published).all()

def get_post(post_id):
    return Post.query.get_or_404(post_id)

def create_post(form):
    title = form.get('title', '').strip()
    body = form.get('body', '').strip()
    if 'is_published' in form and form['is_published']:
        raise ValueError("Post is already published.")
    is_published = 'is_published' in form

    if not title or not body:
        flash("Title and body are required.", 'error')
        return redirect(url_for('posts.new_post'))

    new_post = Post(title=title, body=body, is_published=is_published)
    db.session.add(new_post)
    db.session.commit()

    flash("Post created!", 'success')
    return redirect(url_for('posts.show_posts'))

def update_post(post_id, form):
    post = get_post(post_id)
    title = form.get('title', '').strip()
    body = form.get('body', '').strip()
    is_published = 'is_published' in form

    if post.is_published:
        raise ValueError("Post is already published.")

    if not title or not body:
        flash("Title and body are required.", 'error')
        return redirect(url_for('posts.edit_post', post_id=post_id))

    post.title = title
    post.body = body
    post.is_published = is_published
    db.session.commit()

    flash("Post updated!", 'success')
    return redirect(url_for('posts.show_posts'))

def list_drafts():
    return list_posts(published=False)
