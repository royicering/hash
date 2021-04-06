import hashlib
import sys


if len(sys.argv)>1:
    msg=sys.argv[1]
    filename = 'password.txt' 
    passwordList =[]
    with open(filename,'r') as filehandle:
        for line in filehandle:
            currenPlace =line[:-1]
            passwordList.append(currenPlace)

    for i in range(0,len(passwordList)):
        x=hashlib.sha256(passwordList[i].encode()).hexdigest()
        x1=hashlib.sha1(passwordList[i].encode()).hexdigest()
        x2=hashlib.md5(passwordList[i].encode()).hexdigest()
        x3=hashlib.sha512(passwordList[i].encode()).hexdigest()
        
        if(x==str(msg)):
            print(passwordList[i]+" by sha256")
            break
        elif(x1==str(msg)):
            print(passwordList[i]+" by sha1")
            break 
        elif(x2==str(msg)):
            print(passwordList[i]+" by md5")
            break 
        elif(x3==str(msg)):
            print(passwordList[i]+" by sha512")
            break 



