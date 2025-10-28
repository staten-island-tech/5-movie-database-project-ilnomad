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
        z+=1
def yearrange():
    x=int(input("Min "))
    y=int(input("Max "))
    z=0
    for h in movielist:
        if x<=movielist[z]["year"]<=y:
            print(movielist[z]["title"])
        z+=1
def yeargiven():
    x=int(input("Year given "))
    z=0
    for h in movielist:
        if x==movielist[z]["year"]:
            print(movielist[z]["title"])
        z+=1
def specificmovie():
    x=input("Movie search ")
    z=0
    for h in movielist:
        if movielist[z]["title"]==x:
            print(movielist[z]["title"])
        z+=1
def genresearch():
    genres=input("genres ")
    z=0
    i=0
    for h in movielist:
        for h in movielist[z]["genres"]:
            if genres==movielist[z]["genres"][i]:
                print(movielist[z]["title"])
            i+=1
        i=0
        z+=1
specificmovie()