#!/Users/pwang/anaconda/python.app/Contents/MacOS/python
import pandas
import bokeh

from bokeh.functional import *

df = pandas.read_csv("auto-mpg.csv")

plot = ggplot(df, aes("displ", "mpg")) + geom_point()
with open("one.html", "w") as f:
    f.write(plot.to_html())

