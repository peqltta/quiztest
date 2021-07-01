with open('textlist.txt', 'r', encoding="utf-8") as f:
    x = f.read()
    y = x.replace('\n',': ')
    z = y.split(': ')
    f.close()
    
for i in z:
    print(i)
    input(" ")