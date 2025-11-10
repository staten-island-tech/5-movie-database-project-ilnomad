import json
movies = open("./movies.json", encoding="utf8")
movielist = json.load(movies)

def title():
    i=0
    for h in movielist:
        i+=1
        print(movielist[i]["title"])
def yearafter():
    z=0
    x=input("What year ")
    x=int(x)
    for h in movielist:
        if x<=movielist[z]["year"]:
            print(movielist[z]["title"])
            a+=1
        z+=1
    if a==0:
        print("nothin")
def yearrange():
    x=int(input("Min "))
    y=int(input("Max "))
    z=0
    for h in movielist:
        if x<=movielist[z]["year"]<=y:
            print(movielist[z]["title"])
            a+=1
        z+=1
    if a==0:
        print("nothin")
def yeargiven():
    x=int(input("Year given "))
    z=0
    for h in movielist:
        if x==movielist[z]["year"]:
            print(movielist[z]["title"])
            a+=1
        z+=1
    if a==0:
        print("nothin")
def specificmovie():
    x=input("Movie search ")
    z=0
    for h in movielist:
        if movielist[z]["title"]==x:
            print(movielist[z]["title"])
            a+=1
        z+=1
    if a==0:
        print("nothin")
def genresearch():
    genres=input("genres ")
    z=0
    i=0
    a=0
    for h in movielist:
        for h in movielist[z]["genres"]:
            if genres==movielist[z]["genres"][i]:
                a+=1
                print(movielist[z]["title"])
            i+=1
        i=0
        z+=1
    if a==0:
        print("nothin")

genresearch()