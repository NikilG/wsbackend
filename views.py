from flask import render_template, session, url_for, Response, request, jsonify, g
from flask_classy import FlaskView, route
from models import WhiteboardModel, WhiteboardSchema
import json

whiteboard_schema = WhiteboardSchema()

class DataView(FlaskView):
    route_base = '/'

    @route('/')
    def test_api(self):
        print("1.1")
        return "Test API"
    

    @route('/event_create', methods=['POST'])
    def create_event(self):
        """ Creation of White Board Events """
        try:
            req_data = request.get_json()
            print("REQUEST DATA", req_data)
            data = whiteboard_schema.load(req_data)
            print("DATA", data)
  
            event = WhiteboardModel(data)
            event.save()

            ser_data = whiteboard_schema.dump(event)
            Response = {'message': 'Event Created', 'status': '201', 'response': ser_data}
            return Response
            #return Response(response, 201) #response=json.dumps(ser_data))
        except Exception as e:
            print("Something Went wrong while creating Event --> ", e)
            return "Something Went wrong while creating Event --> {} ".format(e)
  

    def custom_response(self, res, status_code):
        """ Custom Response Function  """
        return Response(
            mimetype="application/json",
            response=json.dumps(res),
            status=status_code
            )

    @route('/allevents')
    def events_all(self):
        """ Get all events """
        events = WhiteboardModel.get_all_events()
        ser_events = whiteboard_schema.dump(events, many=True)
        return self.custom_response(ser_events, 200)

    @route('/event/<int:event_id>', methods=['GET'])
    def get_a_event(self, event_id):
        """ Get a single event """
        event = WhiteboardModel.get_one_event(event_id)
        if not event:
            return self.custom_response({'error': 'Event not found'}, 404)
  
        ser_event = whiteboard_schema.dump(event)
        return self.custom_response(ser_event, 200)
    

