from flask import request
from .helper import error_resp, mainHeaders, success_resp, validate_payload, datatable
from .models import Articles, Comments
from . import db
from sqlalchemy import desc, asc


def index():
    return "Restful API Project is Working!"


def list():
    try:
        payload = request.form.to_dict()
        
        articles = Articles.query
        dataResult = datatable(articles, payload, 'article_id')
        dataset = []
        for artcle in dataResult['data']:
            dataset.append(artcle.toDict())

        data = {}
        data['message'] = 'Records Fetched Successfully!' if len(
            dataset) > 0 else "No Record Found!"
        data['data'] = dataset
        data['recordsTotal'] = dataResult['count']
        data['header'] = mainHeaders(dataset[0])
        resp = success_resp(data)
        return resp
    except Exception as e:
        resp = error_resp({'message': str(e)})
        return resp


def addOrUpdate(article_id=None):
    try:
        payload = request.json
        if not validate_payload('title', payload) or not validate_payload('content', payload):
            resp = error_resp(
                {'message': "Title & Content is mandatory to proceed further!"}, 422)
            return resp

        if request.method == "POST":
            article = Articles(**payload)
            db.session.add(article)
            db.session.commit()
        elif request.method == "PUT" and article_id:
            article = Articles.query.get_or_404(article_id)
            article.update(**payload)
            db.session.commit()

        data = {}
        data['message'] = 'Record Updated Successfully!'
        data['data'] = article.toDict()
        resp = success_resp(data)
        return resp
    except Exception as e:
        resp = error_resp({'message': str(e)})
        return resp


def detail(article_id):
    try:
        article = Articles.query.filter_by(
            article_id=article_id).first_or_404()

        data = {}
        data['message'] = 'Record Fetched Successfully!'
        data['data'] = article.toDict()
        resp = success_resp(data)
        return resp
    except Exception as e:
        resp = error_resp({'message': str(e)})
        return resp


def addComments(article_id):
    try:
        payload = request.json
        if not validate_payload('author', payload) or not validate_payload('content', payload):
            resp = error_resp(
                {'message': "Author & Content is mandatory to proceed further!"}, 422)
            return resp
        payload['article_id'] = article_id

        if request.method == "POST":
            comment = Comments(**payload)
            db.session.add(comment)
            db.session.commit()

        data = {}
        data['message'] = 'Comment Added Successfully!'
        data['data'] = comment.toDict()
        resp = success_resp(data)
        return resp
    except Exception as e:
        resp = error_resp({'message': str(e)})
        return resp


def delete(article_id):
    try:
        article = Articles.query.filter_by(
            article_id=article_id).first_or_404()
        db.session.delete(article)
        db.session.commit()

        data = {}
        data['message'] = 'Record Deleted Successfully!'
        resp = success_resp(data)
        return resp
    except Exception as e:
        resp = error_resp({'message': str(e)})
        return resp
