import random
print("")
print("Welcome to the Cloud Practitioner Quiz. 65 Questions. For Multiple choice answer in alphabetical order i.e AB, CE, BD")
QADict = {}
with open('textlist.txt', 'r', encoding="utf-8") as f:
    x = f.read()
    y = x.replace('\n',': ')
    z = y.split(': ')
    f.close()
for i in z:
    if "Question #" in i:
        Ques = i
        qqq = 1
    elif "Correct Answer" in i:
        qqq = 0
        ccc = 1
    elif "Reference" in i:
        ccc = 0
        rrr = 1
    elif "Explanation" in i:
        rrr = 0
        eee = 1
    elif "https://" in i:
        QADict[Ques+"Ref"] = i
    else:
        if qqq==1:
            if "A. " in i:
                QADict[Ques+"A"] = i
            elif "B. " in i:
                QADict[Ques+"B"] = i
            elif "C. " in i:
                QADict[Ques+"C"] = i
            elif "D. " in i:
                QADict[Ques+"D"] = i
            elif "E. " in i:
                QADict[Ques+"E"] = i
            else:
                QADict[Ques] = i
        elif ccc==1:
            QADict[Ques+"Answer"] = i
        elif rrr==1:
            QADict[Ques+"Ref"] = i
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
            print(QADict["Question #"+str(numran)+"Ref"])
            print("")
