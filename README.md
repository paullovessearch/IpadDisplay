# MissionManager

Creating to manage life-missions in the real world, with a digital interface for verification of completion and awarding of badges.
I'm thinking this could have a lot of interesting applications around the world for all sorts of purposes.

Installation steps:

1. Install python 3.8 (other versions may work, this is the version I tested)

        pipenv --python 3.8

1. Package installs:

        pipenv install flask
        pipenv install flask-socketio

1. Run it:

        export FLASK_APP=MissionManager
        pipenv run flask run

    * OR: (use with care)

        pipenv run flask run --host 0.0.0.0 --port 80
    
