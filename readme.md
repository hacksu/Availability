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

## Serve JSON

* Right now we'll just returning html which isn't the most useful thing for scripts, instead lets return JSON.
* Add `, jsonify` after the Flask import
* Now we can call jsonify to turn a python dictionary into a json responce for any of our routes
* As an example replace "Hello Wold!" with jsonify({"message": "Hello World!"})
* Now when we reload the website we get... `[object Object]` not exactly what we wanted. Lets print it out instead
    * Replace `alart` with `console.log`
    * We get `Object {message: "Hello World!"}` much more useful. It got parsed into a JavaScript object because jQuery is useful
* We can print out just the message by doing `data.message` so `alert(data.message)`

## Serve the right JSON

Let's actually serve JSON which can be used to display the information we want

* Lets add a new route "availability" like

        @app.route("/availability")
        def get_availability():
            return jsonify({})
            
* The format we want to use for the finished version will be very simple
    * Just a dictionary of names and availabilities
    * So for now lets return something like `{"isaac": "free", "timothy": "kind of busy"}
* Change the index.html file to fetch  `http://127.0.0.1:5000/availability` then just print out the result.

## Record status

Let's actually record if people are available.

* To do that we need another route, but this one will be special. All the others have just defaulted to be GET, this one needs to be PUT
* So we specify the method like this: @app.route("/availability", methods=["POST"])
* Then we need to add a method to go with it.
* Import `request` from flask, this is a variable which holds details about the current request being made.
* Now we are going to define a global dictionary to hold our data. THIS IS A BAD IDEA, but we'll hackers so lets do it. `availability = {}`
* Inside our new function, make sure python knows we want to use it with  `global availability`
* Now we just need to merge the data we just got with our existing data on availability. This does that perfectly `availability.update(request.get_json())`
* We have to return something so let's return the current availability dictionary `return jsonify(availability)`
* And let's do the same thing when we're getting availability

## Show status

Lets display all this cool info we have to the user

* So what we need to do is dynamically edit the web page. The good news is we can do just that.
* First step is to add a div to mark the spot we'll be putting this info. Something like `<div id="availabilities"></div>`
* Make sure it give it an id so we can find it later
* Now in when we get our data back from the backend, we need to make sure the website has been totally loaded so we can edit it
* We pass a function to jQuery and it will take care of it like this:

        $(function () {
        });

* The first thing we need to do is find that div we created. Like this `var availabilities = $("#availabilities");`
* Now we can just loop through every user and add a list item for them like so

        for (var user in data) {
            availabilities.append("<li>" + user + ": " + data[user] + "</li>")
        }
* Reload the page and... you see nothing because we don't have any data yet. We can add some with postman, or you can just use my data

## Set Status

Lets let users actually set if they are free or not

* Add the menu, your options can be different, but my backend will strip any inputs but those listed

        <input type="text" id="name"/>
        
        <select id="availability">
          <option value="Free">Free</option>
          <option value="Busy">Busy</option>
          <option value="Putting out a fire">Putting out a fire</option>
          <option value="Running really fast">Running really fast</option>
        </select>
        <button onclick="submit_availability()">Submit</button>
* Add the function

        function submit_availability() {
            var name = $("#name").val();
            var availability = $("#availability").val();
            var data = {};
            data[name] = availability;
            jQuery.ajax({
                type: "POST",
                url: "http://127.0.0.1:5000/availability",
                data: JSON.stringify(data),
                success: function (data) {
                    console.log(data);
                },
                contentType: "application/json"
            });

        }
