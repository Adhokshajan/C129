import csv
data = []
with open("C:\\Users\\Murali\\Desktop\\Adhok\\python\\final.csv" , "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
planet_data = data[1:]

#converting all planet name to ;lower case
for data_point in planet_data :
    data_point[2]=data_point[2].lower()
#sorting planet name in alpha order 
planet_data.sort(key = lambda  planet_data :   planet_data[2])

with open("final_sorted.csv", "a+") as f:
     csvwriter = csv.writer(f)
     csvwriter.writerow(headers)
     csvwriter.writerows(planet_data)