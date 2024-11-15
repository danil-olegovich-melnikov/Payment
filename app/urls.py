from flask import Blueprint
from .routes import *

main = Blueprint('main', __name__)

main.add_url_rule('/', view_func=index)
main.add_url_rule('/search', view_func=search)
main.add_url_rule('/form', view_func=form, methods=["GET", "POST"])