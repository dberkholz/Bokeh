#!/Users/pwang/anaconda/python.app/Contents/MacOS/python
import pandas
from bokeh.functional import *
df = pandas.read_csv("auto-mpg2.csv")
g = ggplot(df, aes("displ", "mpg", color="green")) + facet_grid("cyl", "origin") + geom_point()

with open("grid.html", "w") as f:
    f.write(g.to_html())


