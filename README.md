# IpadDisplay

Creating a new project to enable flashing messages on iPads for the IMAG museum. 
I'm thinking this could have a lot of interesting applications for an interactive museum display.

Installation steps:

1. Install python 3.8 (other versions may work, this is the version I tested)

1. pip3 installs:

        pip3 install flask<br/>
        pip3 install flask-socketio

1. Run it:

        export FLASK_APP=ipad
        flask run

    * OR: (use with care)

        flask run --host 0.0.0.0 --port 80
    
