import requests
from app import app, db
from flask import request
from model.day import Day
from model.ip_view import IpView
from sqlalchemy.sql.functions import count
import datetime

BASE = "http://127.0.0.1:5000"


def get_current_day():
    today = datetime.date.today()
    return today.strftime("%Y-%m-%d")

def get_current_id():
    


@app.route("/view", methods=["GET"])
def on_view():
    try:
        day_id = get_current_day() # get our day_id, which is the date string in the format "yyyy-mm-dd"
        client_ip = request.remote_addr # get the ip address of where the client request came from

        query = Day.query.filter_by(id=day_id) # try to get the row associated to the current day
        if query.count() > 0: 
            # the current day is already in table, simply increment its views
            current_day = query.first()
            current_day.views += 1
        else:
            # the current day does not exist, its the first view for the day.
            current_day = Day(day_id, 1, 0)
            db.session.add(current_day) # insert a new day into the day table
        
        query = IpView.query.filter_by(ip=client_ip,date_id=day_id)
        if query.count() == 0: # check if its the first time a viewer from this ip address is viewing the website
            ip_view = IpView(client_ip, day_id)
            db.session.add(ip_view) # insert into the ip_view table
        
        db.session.commit() # commit all the changes to the database
        return {}, 200
    except Exception as e:
        return {"error":True, "message": str(e)}, 500

@app.route("/read", methods=["GET"])
def on_read():
    try:
        day_id = get_current_id()
        query = Day.query.filter_by(id=day_id)
        if query.count() == 0:
            return {"error": True, "message": f"Day {day_id} does not exist"}, 400
        day = query.first()
        day.reads += 1
        db.session.commit()
        return {}, 200
    except Exception as e:
        return {"error": True, "message":str(e)}, 500


response = requests.get(BASE + "/episode/<int:id>")
responses = requests.post(BASE + "/hello")
print(response.json())
print(responses.json())
