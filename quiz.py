from flask import Flask, render_template
from waitress import serve
import random, copy
import json
application = Flask(__name__)
with open('QADict.json') as f:
    QADict = json.load(f)
    f.close()
@application.route('/')
def quiz():
    Question = ""
    Answers = []
    CorrectAnswer = ""
    Reference = ""
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




"""   
def is_correct():
    if UserAnswer = CorrectAnswer:
        return True
    if Useranswer != CorrectAnswer:
        return False

def shuffle(q):
    selected_keys = []
    i = 0
    while i < len(q):
        current_selection = random.choice(q.keys())
        if current_selection not in selected_keys:
            selected_keys.append(current_selection)
            i = i+1
    return selected_keys
questions_shuffled = shuffle(questions)










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