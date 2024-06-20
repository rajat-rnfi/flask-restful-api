from . import db  # from __init__ file
from datetime import datetime
# from sqlalchemy import inspect


class Articles(db.Model):
    article_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(200))
    author = db.Column(db.String(50), default='')
    publication_date = db.Column(db.Date)
    status = db.Column(db.Integer, default=1)
    comments = db.relationship(
        'Comments', backref="parent", passive_deletes=True)
    updated_at = db.Column(db.DateTime(timezone=True),
                           default=datetime.now(), onupdate=datetime.now())
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())

    def toDict(self):
        return {
            'article_id': self.article_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'publication_date': self.publication_date.strftime('%d-%m-%Y'),
            'comments': list(map(lambda comment: comment.toDict(), self.comments)),
            'updated_at': self.created_at.strftime('%d-%m-%Y %H:%M:%S'),
            'created_at': self.created_at.strftime('%d-%m-%Y %H:%M:%S'),
        }
        # return {c.key: getattr(self, c.key) if c.key != 'publication_date' else self.publication_date.strftime('%d-%m-%Y') for c in inspect(self).mapper.column_attrs}

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


class Comments(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey(
        'articles.article_id', ondelete='CASCADE'))
    author = db.Column(db.String(50))
    content = db.Column(db.Text)
    status = db.Column(db.Integer, default=1)
    updated_at = db.Column(db.DateTime(timezone=True),
                           default=datetime.now(), onupdate=datetime.now())
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())

    def toDict(self):
        return {
            'comment_id': self.comment_id,
            'author': self.author,
            'content': self.content,
        }
