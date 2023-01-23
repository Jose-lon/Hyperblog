import csv
import matplotlib.pyplot as plt

with open("./read.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    header = next(reader)
    data = []
    for i in reader:
        iterable = zip(header, i)
        dict = {key: value for key, value in iterable}
        data.append(dict)
'''
total = []
names =[]
for item in data:
    for key in item:
        if key == "World Population Percentage":
            total.append(float(item[key]))
            names.append(item["Country/Territory"])
'''
data = list(filter(lambda item: float(item["World Population Percentage"]) > 0.75, data))
names =  list(map(lambda x: x['Country/Territory'], data))
total = list(map(lambda x: x['World Population Percentage'], data))
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.show()
generate_pie_chart(names, total)