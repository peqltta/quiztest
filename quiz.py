from flask import Flask, render_template, request
import random, copy
import json
application = Flask(__name__)
with open('QADict.json') as f:
    QADict = json.load(f)
    f.close()
CorrectAnswer = ''
UserAnswer = ""
@application.route('/')
def quiz():
    global CorrectAnswer
    global numran
    Question = ""
    Answers = []
    global Reference
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
@application.route('/answer', methods=['GET'])
def submit():
    lin = ''
    dat = ''
    correct = 'no'
    data = request.form
    for x in data.values():
        dat+=dat+x
    response = 'Correct: ' + correct + ' Correct Answer: '+ CorrectAnswer
    try:
        lin = Reference
    except:
        lin = 'No Link'
    return render_template('answer.html', c = CorrectAnswer, l = lin, d = dat)

if __name__ == '__main_-':
    application.run(host='0.0.0.0')

"""
for i in range(1,65):
    numran = random.randint(1,671)
    print(QADict["Question #"+str(numran)])
    print("")
    print(QADict["Question #"+str(numran)+"A"])
    print(QADict["Question #"+str(numran)+"B"])
    print(QADict["Question #"+str(numran)+"C"])
    print(QADict["Question #"+str(numran)+"D"])
    try:
        print(QADict["Question #"+str(numran)+"E"])
    except:
        hi = 1
    print("")
    correct = 0
    while correct == 0:    
        ans = input("Please Input your Answer ")
        print("")
        if ans == QADict["Question #"+str(numran)+"Answer"]:
            print("You are right! ")
            print("")
            correct = 1
        else:
            print("Wrong guess again! ")
            print("")
            print("Heres a link that might help:")
            try:
                print(QADict["Question #"+str(numran)+"Ref"])
            except:
                print("No link?")
            print("")

"""