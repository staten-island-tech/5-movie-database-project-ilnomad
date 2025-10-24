def takeanumber(n):
    lateness=[]
    z=input("TAKE, SERVE, CLOSE, or EOF ")
    lateness.append(z)
    while not z=="EOF":
        z=input("TAKE, SERVE, CLOSE, or EOF ")
        lateness.append(z)
    a=0
    t=0
    s=0
    while not lateness[a]=="EOF":
        if lateness[a]=="TAKE":
            n+=1
            t+=1
            if n>=999:
                n=1
        elif lateness[a]=="SERVE":
            s+=1
            if n>=999:
                n=1
        elif lateness[a]=="CLOSE":
            print(t,t-s,n)
            if n>=999:
                n=1
            t=s=0
        a+=1
takeanumber(990)