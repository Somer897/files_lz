import matplotlib.pyplot as plt
import pandas as pd

#open parquet
table = pd.read_parquet('titanic.parquet')
#save as csv
table.to_csv('titanic.csv')

#open new file
df = pd.read_csv('titanic.csv')

#group with class and survived
a = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)

#for making gisto with percent instead number
surv = a.div(a.sum(axis=1), axis=0) * 100 

#make gisto
surv.plot(kind='bar', stacked=True)

#make X and Y names, Title and other
plt.title('Выживаемость пассажиров от класса') 
plt.xlabel('Класс') 
plt.ylabel('% выживаемости') 
plt.xticks(rotation=0)
plt.legend(['Не выжил', 'Выжил']) 
plt.tight_layout()

#show our gisto
plt.show()