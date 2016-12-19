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
        return render_template('error.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            # no user input
            return render_template('empty.html')
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                # ***user didn't type exactly one of the options
                currentscene = map.SCENES[session['scene']] #**NOT SURE IF THIS WORKS! IT SOULD GIVE THE SCENE AGIAN ALLOWING USER TO TRY again
                return render_template('again.html')
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene) #scene is the variable being passed to template
    else:
        # There's no session
        return render_template('error.html')

# This URL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = map.START.urlname
    return redirect(url_for('game_get')) # redirect the browser to the url for gmae_get

app.secret_key = 'lpthw52'

if __name__ == "__main__":
    app.run()
