# AvailabilityBackend

This project demonstrates the use of Flask to produce a JSON api.

* GET /availability returns every user's availability
* POST /availability allows the user to specify their availability

## Instructions

### Hello World

Lets make it say hi to us like every good program should.

* First lets make sure Flask is installed type `pip install flask`
* Now lets create a file. I'll call it AvailabilityBackend.py, but the file name really doesn't mater.
* Open it up in your text editor of choice
* We'll be importing the the Flask class from the flask package add `from flask import Flask`
* We'll define our web server with `app = Flask(__name__)` the `__name__` is set by the interceptor to show the context the script is run in
* We need to register a function to be run when Flask gets various requests
* Here well by adding

        @app.route("/")
        def hello_world():
            return "Hello World!"
        
    this may look strange, but this is just what we call a decorator. In essence, it's a fancy way of saying `app.route("/", hello_world)`
    It's a lot easier to read though so people generally do it this way.

* You notice we returned "Hello World!" that was what we wanted our route to return. It's that simple
* We just have to run a local server. Add `app.run()`
* Run your file with `python` your file name. In my case `python AvailabilityBackend.py`
* It should give you the url it is listening on. Go to that url and you should see `Hello World!`
* This works, but it isn't right. One we may need to load this file as a module, so we can use a more fully fledged web server
than the built in one. To do this we'll need to check if we're the main file when we're about to run the web server
* Add `if __name__ == "__main__":` in front of the `app.run()`


### Read the info in jQuery

Let's change tacks and load the route we just created using jQuery.

* Create a html file. I'll be calling it `index.html`
* Add the minimal stuff to make it a valid page
        
        <html>
        <head>
            
        </head>
        <body>
        
        </body>
        </html>
* Then we need to include jQuery. We'll make this bit interactive.
    * Search for `jquery cdn`
    * find the link to the library
    * Include it by adding a `<script src="`your url`"></script>` where your url is the url we found earlier
* Add a script tag again in the head
* Let's make a GET request to fetch that page we created. We can do this a number of different ways but the easiest
is just to do 
    
        $.get("http://127.0.0.1:5000/", "", function (data) {
            alert(data)
        })

* Load that page... You should see nothing. 
    * If you open up the console you'll see `XMLHttpRequest cannot load http://127.0.0.1:5000/. No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://localhost:6209' is therefore not allowed access.`
    * This is a very common error. We'll getting it because we didn't tell chrome it was OK to let Javascript load our resource.
* There's an easy solution. Install flask-cors with `pip install flask-cors`
* Add `from flask.ext.cors import CORS` to import the library
* Add `CORS(app)` to apply it
* Reload and you should get an alert that says "Hello World!"