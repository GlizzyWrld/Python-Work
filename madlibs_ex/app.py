from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension 
from stories import story 

app = Flask(__name__)

#app.debug = True

app.config['SECRET_KEY'] = "GrantIsTheMan"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)


@app.route('/story')
def create_story():
    
    text = story.generate(request.args)

    return render_template("story.html", text=text)
    