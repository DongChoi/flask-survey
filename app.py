from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

SURVEY_RESPONSES = []
questions_counter = 0
@app.get('/survey_start')
def display_start():
    """ Display start page for Survey Start """

    instructions = survey.instructions
    title = survey.title
    return render_template('survey_start.html', title = title, instructions = instructions)


"""make questions html separate per question doing question/0, question/1"""
@app.get(f'/question/{questions_counter}')
def display_question(questions_counter):



    return render_template(f"/question/{questions_counter}", question=survey.questions[questions_counter], choices=survey.questions[questions_counter].choices)
