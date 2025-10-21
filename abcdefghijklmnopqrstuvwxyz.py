import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)

def title():
    for h in data:
        print(data{"title"})
def yeargiven():
    print("a")
    x=input("What year ")
    x=int(x)
    for h in data:
        z+=1
        if x==data[z]["year"]:
            print(data[z]["name"])
title()