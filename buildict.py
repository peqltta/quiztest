import json
QADict = {}
with open('textlist.txt', 'r', encoding="utf-8") as f:
    x = f.read()
    y = x.replace('\n',': ')
    z = y.split(': ')
    f.close()
Question = ''
for i in z:
    if "Question #" in i:
        Ques = i
        qqq = 1
    elif "Correct A" in i:
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
                Question = Question + ' ' + i
                QADict[Ques] = Question
        elif ccc==1:
            QADict[Ques+"Answer"] = i
            Question = ''
            ccc=0
with open('text.json', 'w+') as out:
    json.dump(QADict, out)
            
