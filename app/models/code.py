from . import db


class Code(db.Model):

    __table_name__ = "codes"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    title = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )

    parent_code_id = db.Column(
        db.Integer,
        db.ForeignKey(id),
        nullable=True
    )
    parent_code = db.relationship(
        'Code',
        remote_side=[id],
        backref=db.backref('subcodes', lazy=False),
        lazy=False
    )

    def __init__(self, code, title, parent_code=None):
        self.code = code
        self.title = title
        self.parent_code = parent_code

    def save(self):
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def full_code(self):
        codes = [self.code]
        if self.parent_code is not None:
            codes.insert(0, self.parent_code.code)
        return "".join(codes)

    def full_title(self):
        titles = [self.title]
        if self.parent_code is not None:
            titles.insert(0, self.parent_code.title)
        return ", ".join(titles)

    # Format for API Response
    def __repr__(self):
        return {
            'codeId': self.id,
            'parentCodeId': self.parent_code_id or None,
            'code': self.code,
            'fullCode': self.full_code(),
            'title': self.title,
            'fullTitle': self.full_code(),
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }
