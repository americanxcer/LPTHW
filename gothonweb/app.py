from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        # The user doesn't have a session...
        # What should your code do in response?
        print "Your session has expiered.."
        return render_template('you_died.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            # Weird, a POST request to /game with no user input... what should your code do?
            print "You need to make a descision!"
            return render_template('you_died.html')
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                # There's no transition for that user input
                # what should your code to in response?
                print "Does not compute!"
                return render_template('you_died.html')
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        # There's no session, how could the user get here?
        # What should your code do in response?
        print "Your session has expiered.."
        return render_template('you_died.html')

# This URL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = map.START.urlname
    return redirect(url_for('game_get')) # redirect the browser to the url for gmae_get

app.secret_key = 'lpthw52'

if __name__ == "__main__":
    app.run()
