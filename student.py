import csv
import plotly.express as px

with open("106/student.csv") as f :
    df= csv.DictReader(f)
    fig=px.scatter(df,x="Marks",y="Days")
    fig.show()
