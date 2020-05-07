from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np

url = 'https://www.worldometers.info/coronavirus/'

r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, features='html.parser')

#print(soup.prettify())
print(soup.title.text)
datadiv=soup.find("div", {"id": "nav-today"})
print(datadiv)
elementsfull =[]
row=0
for tr in datadiv.findAll("tr"):
    elements=[]
    column=0
    for td in tr.findAll("td"):
        if(td.text!=''):
            elements.append(td.text)
            column+=1
            #print('column: ', column)   

    elementsfull.append(elements)        
    #print('row: ', row)        
    row+=1

#creating a dataframe for the data
covid_df = pd.DataFrame(data=elementsfull)
print(covid_df)
covid_df=covid_df.drop(12,axis=1)
covid_df.columns

covid_df.head()
df_covid.rename(columns={0:'Country',1:'Total Cases',3:'Total Deaths',5:'Total Recovered'},inplace=True)
covid_df=covid_df.drop()

#cleaning the data
df_covid = covid_df.iloc[9:223]
df_covid=df_covid.drop([2,4,6,7,8,9,10,11,12],axis=1)
df_covid.reset_index(inplace = True) 

#converting into csv
df_covid=df_covid.drop('index',axis=1)
df_covid.to_csv('covid_data_new.csv',sep=',')
df_covid['Total Recovered'].iloc[212]=0
