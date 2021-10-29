import csv
import plotly.express as px

with open("106/coffee.csv") as f :
    df= csv.DictReader(f)
    fig=px.scatter(df,x="Coffee",y="sleep")
    fig.show()
