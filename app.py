from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse

app = Flask(__name__) #Create Flask object app

api = Api(app) #creating api object wrapping app as API

episode_args = reqparse.RequestParser() #creating arguments for the episode 
#adding required arguments 
episode_args.add_argument(name="name", type=str, help="name of episode", required=True)
episode_args.add_argument(name="listens", type=int, help="Number of listens")
episode_args.add_argument(name="likes", type=int, help="Number of likes")



episodes = {1:{"episode_name":"How to build a car","discription":"This is an episode on how to build your own car using boxes and glue", "listens":15, "likes":7},
            2:{"episode_name":"How to build a car","discription":"This is an episode on how to build your own car using boxes and glue", "listens":145, "likes":7},
            3:{"episode_name":"How to build a car","discription":"This is an episode on how to build your own car using boxes and glue", "listens":59, "likes":7},
            4:{"episode_name":"How to build a car","discription":"This is an episode on how to build your own car using boxes and glue", "listens":1500, "likes":7},
            5:{"episode_name":"How to build a car","discription":"This is an episode on how to build your own car using boxes and glue", "listens":515, "likes":7},
            6:{"episode_name":"How to build a car","discription":"This is an episode on how to build your own car using boxes and glue", "listens":786, "likes":7},
            7:{"episode_name":"How to build a car","discription":"This is an episode on how to build your own car using boxes and glue", "listens":2021, "likes":7},
            8:{"episode_name":"my cats got married","discription":"This is an episode on how to build your own car using boxes and glue", "listens":49, "likes":7},
            9:{"episode_name":"How to build an API","discription":"This is an episode on how to build your own car using boxes and glue", "listens":11456, "likes":7}}
class episode(Resource): #Create class episode inheriting from Resource class to handle episode requests
    def get(self, episode_id):
        """"
        Override get method from Resource class for class episode takes in self and episode_id
        """
        args = episode_args.parse_args()
        return {episode_id: args}

    def put(self):
        pass

api.add_resource(episode, "/episode/<int:id>") #adding episode class to resource with an endpoint /episode/<episode_id>

@app.route('/')
def home():
    return render_template('index.html', episodes = episodes)


if __name__ == "__main__":
    app.run(debug="True")