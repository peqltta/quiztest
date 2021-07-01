with open('textlist.txt', 'r', encoding="utf-8") as f:
    x = f.read()
    y = x.replace('\n',': ')
    z = y.split(': ')
    f.close()
print("\x1b[1;31;40m"+"Welcome to the AWS Cloud Practitioner 2021 Complete Quiz."+"\x1b[0m") 
for i in z:
    if "Question #" in i:
        input("\x1b[2;30;44m"+"Press Enter to continue.."+"\x1b[0m")
        print("\n"+"\x1b[6;30;42m"+i+"\x1b[0m")
    elif "Correct Answer" in i:
        input("\x1b[1;32;40m"+"Input your Answer..   "+"\x1b[0m")
        print("\x1b[1;34;40m"+i+"\x1b[0m")
    elif "Reference" in i:
        input("\x1b[2;30;44m"+"Press Enter to continue.."+"\x1b[0m")
        print(i)
    else:
        print(i)
