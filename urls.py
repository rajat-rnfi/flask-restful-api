from . import app  # from __init__ file
from flask import request
from . import controllers
from .helper import error_resp


@app.route('/', methods=['GET'])
def index_urls():
    if request.method == 'GET':
        return controllers.index()
    else:
        return 'Method is Not Allowed'


@app.route('/api/articles', methods=['GET'])
def list_urls():
    if request.method == 'GET':
        return controllers.list()
    else:
        return error_resp({'message': "Method is Not Allowed"}, 405)


@app.route('/api/articles', methods=['POST'])
@app.route('/api/articles/<int:article_id>', methods=['PUT'])
def add_urls(article_id=None):
    if request.method == 'POST':
        return controllers.addOrUpdate(article_id)
    elif request.method == 'PUT':
        return controllers.addOrUpdate(article_id)
    else:
        return error_resp({'message': "Method is Not Allowed"}, 405)


@app.route('/api/articles/<int:article_id>', methods=['GET'])
def detail_urls(article_id):
    if request.method == 'GET':
        return controllers.detail(article_id)
    else:
        return error_resp({'message': "Method is Not Allowed"}, 405)


@app.route('/api/articles/<int:article_id>/comments', methods=['POST'])
def addComments_urls(article_id):
    if request.method == 'POST':
        return controllers.addComments(article_id)
    else:
        return error_resp({'message': "Method is Not Allowed"}, 405)


@app.route('/api/articles/<int:article_id>', methods=['DELETE'])
def delete_urls(article_id):
    if request.method == 'DELETE':
        return controllers.delete(article_id)
    else:
        return error_resp({'message': "Method is Not Allowed"}, 405)
