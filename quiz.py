from flask import Flask, render_template, request
import random, copy
import json
application = Flask(__name__)
with open('QADict.json') as f:
    QADict = json.load(f)
    f.close()
@application.route('/')
def main():
    return render_template('index.html')
@application.route('/login')
def loginpage():
    return render_template('login.html')
@application.route('/quiz', methods=['POST'])
def quizprog():
    global CorrectAnswer
    Question = ""
    Answers = []
    Reference = ''
    CorrectAnswer = ""
    idkwhattodohere=0
    prog = request.form['qn']
    if request.form['btn'] == 'Next':
        try:
            pronum = int(prog)
            pronum+=1
            if pronum > 671:
                pronum = 671
            prog = str(pronum)
        except:
            prog = 1
    elif request.form['btn'] == 'Back':
        try:
            pronum = int(prog)
            pronum-=1
            if pronum > 671:
                pronum = 671
            prog= str(pronum)
        except:
            prog=1
    Question = QADict["Question #"+str(prog)]
    Answers = [QADict["Question #"+str(prog)+"A"],QADict["Question #"+str(prog)+"B"],QADict["Question #"+str(prog)+"C"],QADict["Question #"+str(prog)+"D"]]
    try:
        Answers.append(QADict["Question #"+str(prog)+"E"])
    except:
        idkwhattodohere+=1
    CorrectAnswer = QADict["Question #"+str(prog)+"Answer"]
    try:
        Reference = QADict["Question #"+str(prog)+"Ref"]
    except:
        idkwhattodohere+=1
    return render_template('mainorder.html', q = Question, o = Answers, c = CorrectAnswer, l = Reference, p = prog)
@application.route('/quiz', methods=['GET'])
def quizfirst():
    global CorrectAnswer
    Question = ""
    Answers = []
    Reference = ''
    CorrectAnswer = ""
    idkwhattodohere=0
    prog = 1
    Question = QADict["Question #"+str(prog)]
    Answers = [QADict["Question #"+str(prog)+"A"],QADict["Question #"+str(prog)+"B"],QADict["Question #"+str(prog)+"C"],QADict["Question #"+str(prog)+"D"]]
    try:
        Answers.append(QADict["Question #"+str(prog)+"E"])
    except:
        idkwhattodohere+=1
    CorrectAnswer = QADict["Question #"+str(prog)+"Answer"]
    try:
        Reference = QADict["Question #"+str(prog)+"Ref"]
    except:
        idkwhattodohere+=1
    return render_template('mainorder.html', q = Question, o = Answers, c = CorrectAnswer, l = Reference, p = prog)
if __name__ == '__main_-':
    application.run(host='0.0.0.0')