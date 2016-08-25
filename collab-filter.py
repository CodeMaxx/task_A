import csv
data = list(csv.reader(open('movie-ratings.csv')))
headers = data[0][1:]
def evalmap(x):
    return list(map(eval,x))
def tupler(x):
    return (x[0],evalmap(x[1:])
ratings = list(map(tupler,data[1:]))
data = list(csv.reader(open('user_preference.csv')))[0]
upref = (data[0],list(map(eval,data[1:])))
def diff(x,y):
    for i in range(min(len(x),len(y))):
        z = []
        if (x[i]!=-1) and (y[i]!=-1):
            z.append(x[i]-y[i])
    return z
from math import sqrt
def euclidDistFromUser(x):
    return sqrt(sum(map(lambda t: t*t, diff(x[1],upref[1]))))
sortedRatings = sorted(ratings, key = euclidDistFromUser)
# print(headers)
# print(ratings)
# print(upref)
