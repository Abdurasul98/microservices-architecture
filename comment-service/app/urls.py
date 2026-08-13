from .views import comment_bp

def register_routes(app):
    app.register_blueprint(comment_bp, url_prefix='/api/comments')