from flask import session, Response, request, jsonify
from flask_classy import FlaskView, route
from models import WhiteboardModel, WhiteboardSchema, db, WhiteboardTask, WhiteboardTaskSchema
import json
from logger import log

whiteboard_schema = WhiteboardSchema()
#whiteboardtasSchema = WhiteboardTaskSchema()

class DataView(FlaskView):
    route_base = '/'

    @route('/')
    def test_api(self):
        log.info("1.1")
        return "Test API"
    

    @route('/events', methods=['POST'])
    def create_event(self):
        """ Creation of White Board Events """
        try:
            req_data = request.get_json()             #Input POST Data / Payload
            status = req_data.get('status')
            res = WhiteboardTask.query.filter(WhiteboardTask.Name == status).all()  #Fetching Task id from WhiteboardTask Table
            wid = [i.id for i in res]
            wtid = {'whiteboard_task_id': wid[0] }
            req_data.update(wtid)
            data = whiteboard_schema.load(req_data)
            
            event = WhiteboardModel(data)
            event.save()
            ser_data = whiteboard_schema.dump(event)
            
            Response = {'message': 'Event Created', 'status': '201', 'response': ser_data}
            log.info("Event Created Succesfully --> {}".format(Response))
            return Response
            #return Response(response, 201) #response=json.dumps(ser_data))
        except Exception as e:
            print("Something Went wrong while creating Event --> ", e)
            log.error("Something Went wrong while creating Event --> {} ".format(e))
            return "Something Went wrong while creating Event --> {} ".format(e)
  

    def custom_response(self, res, status_code):
        """ Custom Response Function  """
        return Response(
            mimetype="application/json",
            response=json.dumps(res),
            status=status_code
            )

    @route('/events')
    def events_all(self):
        """ Get all events """
        events = WhiteboardModel.get_all_events()
        ser_events = whiteboard_schema.dump(events, many=True)
        log.info("All Events --> {}".format(ser_events))
        return self.custom_response(ser_events, 200)

    @route('/events/<int:event_id>', methods=['GET'])
    def get_a_event(self, event_id):
        """ Get a single event """
        event = WhiteboardModel.get_one_event(event_id)
        if not event:
            log.info("No Events found for this event id --> {}".format(event_id))
            return self.custom_response({'error': 'Event not found'}, 404)
  
        ser_event = whiteboard_schema.dump(event)
        log.info("Event info --> {}".format(ser_event))
        return self.custom_response(ser_event, 200)


    @route('/events/<int:event_id>', methods=['PUT'])
    def update_a_event(self, event_id):
        """ Update a single event """
        try:
            req_data = request.get_json()
            data = whiteboard_schema.load(req_data, partial=True)
            event = WhiteboardModel.get_one_event(event_id)
            
            if not event:
                log.info("No Event found with this id --> {}".format(event_id))
                return self.custom_response({'error': 'Event not found with this Id'}, 404)
            else:
                event.update(data)
                ser_event = whiteboard_schema.dump(event)
                #print("RES UPDATE", ser_event)
                Response = {'message': 'Event Updated', 'status': '201', 'response': ser_event}
                log.info("Event Updated --> {}".format(Response))
                return Response
        except Exception as e:
            log.info("Something went wrong while updating event --> {}".format(e))
            return "Something went wrong while updating event --> {}".format(e)

    
    @route('/filter_events', methods=['GET'])
    def filter_events_on_date(self):
        """ Fetch events based on date filter by using start  """
        try:
            start_date = request.args.get('start_date', None) # use default value repalce 'None'
            end_date = request.args.get('end_date', None)
            response = WhiteboardModel.get_events_on_date(start_date, end_date)
            ser_events = whiteboard_schema.dump(response, many=True)
            log.info("Found Events between {} and {} --> {}".format(start_date, end_date, ser_events))
            return self.custom_response(ser_events, 200)
        except Exception as e:
            log.info("Something went wrong while filtering events --> {}".format(e))
            return ("Something went wrong while filtering events --> {}".format(e))


    @route('/filter_status/<string:status>', methods=['GET'])
    def filter_events_on_status(self, status):
        """ Fetch events based on status """
        response = WhiteboardModel.get_event_on_status(str(status))
        print("response", response)
        ser_events = whiteboard_schema.dump(response, many=True)
        log.info("Event found for status = {} are --> {}".format(status, ser_events))
        return self.custom_response(ser_events, 200)