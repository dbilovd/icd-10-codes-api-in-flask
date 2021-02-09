from . import db

class Code(db.Model):

  __table__name = "codes"

  id = db.Column(db.Integer, primary_key=True)
  code = db.Column(db.String(10))
  title = db.Column(db.String(150))
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
  updated_at = db.Column(
      db.DateTime,
      default=db.func.current_timestamp(),
      onupdate=db.func.current_timestamp()
  )

  def __init__(self, code, title = None):
    self.code = code
    self.title = title
  
  def save(self):
    db.session.add(self)
    db.session.commit()
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()

  # Format for API Response  
  def __repr__(self):
    return {
        'codeId': self.id,
        'code': self.code,
        'title': self.title,
        'createdAt': self.created_at,
        'updatedAt': self.updated_at
    }
