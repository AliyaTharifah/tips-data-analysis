import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("tips.csv") 

plt.title("Scatter Plot") 
plt.xlabel('Day') 
plt.ylabel('Tip') 
plt.scatter(df['day'], df['tip'])  
plt.show() 

# Persentase Laki-laki & Perempuan
plt.figure(figsize=(6, 4))
df['sex'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'pink'])
plt.title('Proporsi Laki-laki vs Perempuan')
plt.ylabel('') 
plt.show()

# Bar Chart Hari
plt.figure(figsize=(6, 4))
df['day'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Jumlah Pengunjung per Hari')
plt.xlabel('Hari')
plt.ylabel('Jumlah Orang')
plt.xticks(rotation=0) 
plt.show()