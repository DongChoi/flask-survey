from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey


app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.get('/survey_start')
def display_start():
    """ Display start page for Survey Start """

    # lines below are handled in a separate route when user clicks the button
    # instructions = survey.instructions
    # title = survey.title
    # #survey = survey
    return render_template('survey_start.html', survey = survey)


@app.post('/session_start')
def create_session():
    """ Create session cookie and redirect to question page """

    session["question"] = 0
    current_question = session["question"]

    session["responses"] = []
    response_list = session["responses"]
    # could also check len of responses instead
    return redirect(f"/question/{current_question}")



@app.get('/question/<int:current_question>')
def display_question(current_question):
    """ Renders template for next question """


    question_num = session["question"]

    #should be redirecting not rendering
    # could shorten it by injecting survey and pluck choices from jinja on template page
    # if current question != actual question, redirect them, else render correct pg

    return render_template('question.html', question_num=survey.questions[question_num], choices=survey.questions[question_num].choices)


@app.post('/answer')
def add_response():
    """ Add response to session responses and increment question counter"""

    response = request.form["answer"]
    response_list = session["responses"]


    response_list.append(response)
    session["responses"] = response_list

    session["question"] += 1
    next_question = session["question"]



    if session["question"] < len(survey.questions):
        return redirect(f"/question/{next_question}")
    else:
        return redirect("/completion")

@app.get('/completion')
def show_thanks():
    """ Show the client some thanks """

    return render_template('completion.html')