# IpadDisplay

Creating a new project to enable flashing messages on iPads for the IMAG museum. 
I'm thinking this could have a lot of interesting applications for an interactive museum display.

Installation steps:

1. Install python 3.8 (other versions may work, this is the version I tested)

        pipenv --python 3.8

1. Package installs:

        pipenv install flask<br/>
        pipenv install flask-socketio

1. Run it:

        export FLASK_APP=ipad
        pipenv run flask run

    * OR: (use with care)

        pipenv run flask run --host 0.0.0.0 --port 80
    
