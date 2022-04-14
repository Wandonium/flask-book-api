
class Book:

  def __init__(self, id, available, title, timestamp):
    self.id = id
    self.title = title
    self.available = available
    self.timestamp = timestamp

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'title': self.title,
      'available': self.available,
      'timestamp':self.timestamp
    }