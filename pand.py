import pandas as pd
import matplotlib.pyplot as plt

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.show()

df = pd.read_csv("read.csv")
countries = df["Country/Territory"].values
percentages = df["World Population Percentage"].values
generate_pie_chart(countries, percentages)

