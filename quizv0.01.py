with open('textlist.txt', 'r', encoding="utf-8") as f:
    x = f.read()
    y = x.replace('\n',': ')
    z = y.split(': ')
    f.close()
    
for i in z:
    if "Question #" in i:
        input("Press Enter to continue..")
        print("\n"+i)
    elif "Correct Answer" in i:
        input(" ")
        print(i)
    elif "Reference" in i:
        input("Press Enter to continue..")
        print(i)
    else:
        print(i)
