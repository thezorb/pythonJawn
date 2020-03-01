#Reading CSV files
#There are a ton of options for the read_csv function that can simplify preprocessing of data. Nobody want to waste time cleaning data, so see if you can knock it out when import the initial file.
import pandas as pd
df = pd.read_csv('pizza.csv')

#Need to parse dates? Just pass in the corresponding column name(s).

df = pd.read_csv('pizza.csv', parse_dates=['dates'])

#Only need a few specific columns?

df = pd.read_csv('pizza.csv', usecols=['foo', 'bar'])
