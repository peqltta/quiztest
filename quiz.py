import time
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print("Do not press anything. " + timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("")       
with open('textlist.txt', 'r', encoding="utf-8") as f:
    x = f.read()
    y = x.replace('\n',': ')
    z = y.split(': ')
    f.close()
print("Welcome to the AWS Cloud Practitioner 2021 Complete Quiz.")
progress = 1
print("Input Progress (Question start #)")
progress = input()
timeinp = 0
while not timeinp:
    try:
        print("How long per question? (Default 83s -- 90 Minutes / 65 Questions)")
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
            input("Press Enter to continue..")
            print("")
            print("\n"+i)
        elif "Correct Answer" in i:
            print("")
            countdown(timeinp)
            ans = input("Input your Answer..   ")
            print("")
            print("Your Answer: "+ans)
            print("")
            print(i)
        elif "Reference" in i:
            input("Press Enter to continue..")
            print("")
            print(i)
        elif "Explanation" in i:
            print(i)
            print("")
        elif "https://" in i:
            print(i)
            print("")
        else:
            print(i)
