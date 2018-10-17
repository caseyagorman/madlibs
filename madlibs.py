"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("greet.html",
                           person=player,
                           compliment=compliment)


@app.route('/play_game')
def play_game():
    """Plays game."""
    game_response = request.args.get("play_game")
    if game_response == "no":
        return render_template("goodbye.html")
    else: 
        color = request.args.get("color_type")
        noun = request.args.get("noun_type")
        person = request.args.get("adjective_type")
        adjective = request.args.get("person_type")
        
        return render_template("play_game.html",
                            color_type=color,
                            noun_type=noun,
                            person_type=person,
                            adjective_type=adjective)
                

@app.route('/madlibs')
def show_madlib():
    color = request.args.get("color_type")
    noun = request.args.get("noun_type")
    person = request.args.get("adjective_type")
    adjective = request.args.get("person_type")
    return render_template("madlibs.html")

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)