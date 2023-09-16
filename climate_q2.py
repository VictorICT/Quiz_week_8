import matplotlib.pyplot as plt
import pandas as pd

years = []
co2 = []
temp = []

reviews_df = pd.read_csv(r"climate.csv")
# print(type(reviews_dt))

# text = reviews_df.head(10)
# print(text)

yeardatas = reviews_df.Year
# print(yeardatas)

for yeardata in yeardatas:
    # print(yeardata)
    years.append(yeardata)

# print(years)

co2datas = reviews_df.CO2

for co2data in co2datas:
    co2.append(co2data)

tempdatas = reviews_df.Temperature  

for tempdata in tempdatas:
    temp.append(tempdata)

# print(years,co2,temp)

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
plt.savefig("co2_temp_2.png") 

