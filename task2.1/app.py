from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('list.html', candidates=load_candidates_from_json('candidates.json'))


@app.route('/candidate/<int:x>')
def candidate(x):
    return render_template('card.html',candidate=get_candidate(x))

@app.route('/search/<candidate_name>')
def search(candidate_name):
    return render_template('search.html', candidates=get_candidates_by_name(candidate_name))

@app.route('/skill/<skill_name>')
def skill(skill_name):
    return render_template('skill.html', skill_name=skill_name, candidates=get_candidates_by_skill(skill_name))



app.run(debug=True)
