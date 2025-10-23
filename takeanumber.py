def takeanumber(n):
    lateness=[]
    z=input("TAKE, SERVE, CLOSE, or EOF ")
    while z!="EOF":
        z=input("TAKE, SERVE, CLOSE, or EOF ")
        lateness.append(z)
    a=0
    t=0
    s=0
    while lateness[a]!="EOF":
        if lateness[a]=="TAKE":
            n+=1
            t+=1
        if lateness[a]=="SERVE":
            n+=1
            s+=1
        if lateness[a]=="CLOSE":
            print(t,t-s,n)
takeanumber(23)