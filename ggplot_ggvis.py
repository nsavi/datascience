import pandas as pd 
from plotnine import ggplot
df = pd.read_csv("E:/weather.csv")
print(df)
ggplot(df)



import pandas as pd 
from plotnine import ggplot, aes
df = pd.read_csv("E:/weather.csv")
ggplot(df) + aes(x='month',y='avg_low')


import pandas as pd
from plotnine import ggplot, aes, geom_col
df = pd.read_csv("E:/weather.csv")
ggplot(df) + aes(x='month', y='avg_low' + geom_col())
