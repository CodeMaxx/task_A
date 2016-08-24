import csv
data = list(csv.reader(open('movie-ratings.csv')))
headers = data[0][1:]
ratings = {} # dict
for row in data[1:]:
    ratings[row[0]]=row[1:]
data = list(csv.reader(open('user_preference.csv')))[0]
upref = {data[0]:data[1:]}
# print(headers)
# print(ratings)
# print(upref)
