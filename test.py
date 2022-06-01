import os.path

with open("us-cities.txt") as f:
    cities = [line.rstrip('\n') for line in f]

with open('niches.txt') as f:
    niches = [line.rstrip('\n') for line in f]

for i in niches:
    for j in cities:
        completeName = os.path.join(save_path, i + '/', j +".csv")         
        print(completeName)