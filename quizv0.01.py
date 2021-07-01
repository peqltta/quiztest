import time
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
        
with open('textlist.txt', 'r', encoding="utf-8") as f:
    x = f.read()
    y = x.replace('\n',': ')
    z = y.split(': ')
    f.close()
print("\x1b[1;31;40m"+"Welcome to the AWS Cloud Practitioner 2021 Complete Quiz."+"\x1b[0m")
progress = 1
print("\x1b[1;32;40m"+"Input Progress (Question start #)"+"\x1b[0m")
progress = input()
timeinp = 0
while not timeinp:
    try:
        print("\x1b[1;32;40m"+"How long per question? (Default 83s -- 90 Minutes / 65 Questions)"+"\x1b[0m")
        timeinp = int(input())
    except Exception as e:
        print('Please enter an integer in seconds')    
started = "no"
for i in z:
    if "no" in started:
        if ("Question #"+progress) not in i:
            continue
        if ("Question #"+progress) in i:
            started = "yes"
    if "yes" in started:
        if "Question #" in i:
            input("\x1b[2;30;44m"+"Press Enter to continue.."+"\x1b[0m")
            print("")
            print("\n"+"\x1b[6;30;42m"+i+"\x1b[0m")
        elif "Correct Answer" in i:
            print("")
            countdown(timeinp)
            ans = input("\x1b[1;32;40m"+"Input your Answer..   "+"\x1b[0m")
            print("")
            print("\x1b[1;36;40m"+"Your Answer: "+ans+"\x1b[0m")
            print("")
            print("\x1b[1;33;40m"+i+"\x1b[0m")
        elif "Reference" in i:
            input("\x1b[2;30;44m"+"Press Enter to continue.."+"\x1b[0m")
            print("")
            print("\x1b[2;30;43m"+i+"\x1b[0m")
        elif "Explanation" in i:
            print("\x1b[1;32;40m"+i+"\x1b[0m")
            print("")
        elif "https://" in i:
            print("\x1b[2;30;43m"+i+"\x1b[0m")
            print("")
        else:
            print("\x1b[1;31;40m"+i+"\x1b[0m")
