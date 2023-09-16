import sqlite3
import matplotlib.pyplot as plt

years = []
co2 = []
temp = []

con = sqlite3.connect('climate.db')
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
tables = cursor.fetchall()
print(tables)
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData;")
colum = cursor.fetchall()
print(colum)

for colum_info in colum:
    print(colum_info[0])
    years.append(colum_info[0])
    co2.append(colum_info[1])
    temp.append(colum_info[2])

print(years,co2,temp)

con.close()

       

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 