from flask_sqlalchemy import SQLAlchemy
#from . import db
# initialize our db
db = SQLAlchemy()

from marshmallow import fields, Schema
import datetime
#from . import db

class WhiteboardModel(db.Model):
  """
  Whiteboard Events Model
  """

  # table name
  __tablename__ = 'whiteboard'

  id = db.Column(db.Integer, primary_key=True)
  status = db.Column(db.String, nullable=False)
  whiteboard_task_id = db.Column(db.Integer)
  description = db.Column(db.String)
  schedule = db.Column(db.DateTime)
  duration_minutues = db.Column(db.Integer)
  location_latitude = db.Column(db.Float)
  location_longitude = db.Column(db.Float)
  location_address = db.Column(db.String)
  city = db.Column(db.String)
  state = db.Column(db.String)
  contact_name = db.Column(db.String)
  contact_phone_number = db.Column(db.String)
  notes = db.Column(db.Text)


  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.status = data.get('status')
    self.description = data.get('description')
    self.schedule = data.get('schedule')
    self.whiteboard_task_id = data.get('whiteboard_task_id')
    self.duration_minutues = data.get('duration_minutues')
    self.location_latitude = data.get('location_latitude')
    self.location_longitude = data.get('location_longitude')
    self.location_address = data.get('location_address')
    self.city = data.get('city')
    self.state = data.get('state')
    self.contact_name = data.get('contact_name')
    self.contact_phone_number = data.get('contact_phone_number')
    self.notes = data.get('notes')

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    #self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_events():
    return WhiteboardModel.query.all()

  @staticmethod
  def get_one_event(id):
    return WhiteboardModel.query.get(id)

  @staticmethod
  def get_events_on_date(schedule_1, schedule_2): 
    return db.session.query(WhiteboardModel).filter(WhiteboardModel.schedule.between(schedule_1, schedule_2)).all()
    #return res

  @staticmethod
  def get_event_on_status(status):
    return WhiteboardModel.query.filter(WhiteboardModel.status == status).all()

  def __repr(self):
    return '<id {}>'.format(self.id)


class WhiteboardSchema(Schema):
  """
  Whiteboard Schema
  """
  id = fields.Integer(dump_only=True)
  status = fields.Str(required=True)
  whiteboard_task_id = fields.Integer(required=True)
  description = fields.Str(required=True)
  schedule = fields.Str(required=True)
  duration_minutues = fields.Integer(required=True)
  location_latitude = fields.Str(required=True)
  location_longitude = fields.Str(required=True)
  location_address = fields.Str(required=True)
  city = fields.Str(required=True)
  state = fields.Str(required=True)
  contact_name = fields.Str(required=True)  
  contact_phone_number = fields.Str(required=True)
  notes = fields.Str(required=True)




class WhiteboardTask(db.Model):
  """
  Whiteboard Task Model
  """

  # table name
  __tablename__ = 'whiteboard_tasks'

  id = db.Column(db.Integer, primary_key=True)
  Name = db.Column(db.String, nullable=False)


  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.status = data.get('Name')

  def __repr(self):
      return '<id {}>'.format(self.id)

class WhiteboardTaskSchema(Schema):
  """ WhiteboardTaskSchema Schema """
  id = fields.Integer(dump_only=True)
  Name = fields.Str(required=True)