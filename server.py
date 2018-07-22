"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULT = [
 	'bad', 'mean', 'silly', 'kinda-funny-looking', 'incompetent', 
 	'lazy', 'boring', 'dull'
 	]


@app.route('/')
def start_here():
    """Home page."""
    form_string = ""

    for compliment in AWESOMENESS:
    	form_string += "<option value={}>{}</option> \n".format(compliment, compliment.title())

    insult_string = ""

    for insult in INSULT:
    	insult_string += "<option value={}>{}</option> \n".format(insult, insult.title())



    return """
   		<!doctype html>
   		<html>
   		Hi! This is the home page.
   		<a href="/hello">Visit hello</a>
   		
   		<form action="/greet">
   		<p>What's your name?</p>
   		<input type="text" name="person">

   		<p>Choose a compliment</p>
   		<select name="compliment">
   			{}
   		<input type="submit" value="Submit">
   		</select>
   		</form>
   		
   		<hr>

   		<p>Or, would you prefer an insult?</p>

   		<form action="/diss">
   		<p>What's your name?</p>
   		<input type="text" name="person">

   		<p>Choose an insult</p>
   		<select name="insult">
   			{}
   		<input type="submit" value="Submit">
   		</select>
   		</form>
   		</html>

   		""".format(form_string, insult_string)


@app.route('/diss')
def say_insult():
    """Say insults and prompt for user's name."""
    player = request.args.get("person")

    insult = request.args.get("insult")


    return """
    <!doctype html>
    <html>
      <head>
        <title>An insult</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, insult)


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")


    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
