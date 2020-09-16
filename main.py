import requests
from matplotlib import pyplot as plt
from matplotlib import style
val=requests.get("http://api.openweathermap.org/data/2.5/forecast?q=Mumbai&appid=003832f2bc364889038919c9938d9952")
counter=0
finaldata={}
while True:
 try:
     temp=(val.json()['list'][counter]['main']['temp'])-273.15
     humidity=val.json()['list'][counter]['main']['humidity']
     date=((val.json()['list'][counter]['dt_txt']).split(" "))[0]
     counter+=1
     finaldata[date]=(round(temp,2),humidity)
 except:
    break
x=list(finaldata.keys())
temp_y=[]
humidity_y=[]
for i in finaldata.values():
     temp_y.append(i[0])
     humidity_y.append(i[1])
fig1,(ax1,ax2) = plt.subplots(nrows=2, ncols=1)
ax1.plot(x, temp_y, color='r',label='Temperature/Date')
ax2.plot(x, humidity_y,color='g',label='Humidity/Date')
ax1.legend()
ax1.set_title('Weather Forecast')
ax1.set_ylabel('Temperature')
ax2.legend()
ax2.set_xlabel('Date')
ax2.set_ylabel('Humidity')
plt.tight_layout()
ax1.grid(True,color='k')
ax2.grid(True,color='k')
plt.show()