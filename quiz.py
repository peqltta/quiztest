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
@application.route('/quiz')
def quiz():
    global CorrectAnswer
    global numran
    Question = ""
    Answers = []
    Reference = ''
    CorrectAnswer = ""
    idkwhattodohere=0
    numran = random.randrange(1,671)
    Question = QADict["Question #"+str(numran)]
    Answers = [QADict["Question #"+str(numran)+"A"],QADict["Question #"+str(numran)+"B"],QADict["Question #"+str(numran)+"C"],QADict["Question #"+str(numran)+"D"]]
    try:
        Answers.append(QADict["Question #"+str(numran)+"E"])
    except:
        idkwhattodohere+=1
    CorrectAnswer = QADict["Question #"+str(numran)+"Answer"]
    try:
        Reference = QADict["Question #"+str(numran)+"Ref"]
    except:
        idkwhattodohere+=1
    return render_template('main.html', q = Question, o = Answers, c = CorrectAnswer, l = Reference)

if __name__ == '__main_-':
    application.run(host='0.0.0.0')