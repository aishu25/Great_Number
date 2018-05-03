from flask import Flask, redirect, render_template, request, session
import random


numbers = Flask(__name__)
numbers.secret_key = 'ThisIsSecret'

@numbers.route('/')
def pick():
    if "random" not in session:
        session["random"] = random.randrange(0, 100)
    print "the random number is " + str(session["random"])
    return render_template('index.html')

@numbers.route('/guess', methods=['POST'])
def guess():
    random = session["random"]
    guess = int(request.form["guess"])
    print "the guess is " + str(guess) + ", the random number is " + str(random)

    if (random == guess):
        print "You Win!"
        session["verify"] = "win"

    elif (random < guess):
        print "Too High"
        session["verify"] = "high"

    else:
        print "Too Low"
        session["verify"] = "low"

    return redirect('/')


@numbers.route('/replay')
def replay():
    session.pop("random")
    session.pop("verify")
    return redirect('/')

numbers.run(debug=True)
