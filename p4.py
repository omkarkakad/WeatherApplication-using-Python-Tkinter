from tkinter import *
from tkinter.messagebox import *
import requests

API_KEY = "c7e467bac686be669f21974637a9eb1e"

root=Tk()
root.geometry("520x700+300+30")
root.title("Weather Application")
root.configure(bg="#E0F7FA")
root.iconbitmap("weather.ico")


#Def det_weather

def get_weather():
	city= search_ent.get().strip()
	if not city:
		showwarning("Missing Input","Please enter a city name")
		return

	try:
		url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
		res=requests.get(url)
		print(res)
		data=res.json()
		print(data)	
		if data.get("cod") != 200:
			raise Exception(data.get("message","Error fetching data"))
	
		#Extract data
		temp=data['main']['temp']
		humidity=data['main']['humidity']
		wind=data['wind']['speed']
		condition=data['weather'][0]['description'].title()
		city_name=data['name']
		country=data['sys']['country']

		#Update UI

		weather_icon.configure(text="🌤️" if "cloud" in condition.lower() else "☀️")
		temp_label.configure(text=f"{temp}°C")
		city_label.configure(text=f"{city_name}, {country}")
		desc_label.configure(text=condition)
		lbl_temp_val.configure(text=f"{temp}°C")
		lbl_humidity_val.configure(text=f"{humidity}%")
		lbl_wind_val.configure(text=f"{wind} km/h")

		
		
		


	except Exception as e :
		showerror("Error", str(e))

	

#Title
title=Label(root,text="☀️ Weather App",font=("Arial",30,"bold"),fg="black",bg="#0288D1",height=1)
title.pack(fill=X)

#Search Frame
search_frame = Frame(root, bg="#E0F7FA")
search_frame.pack(pady=10)

#Search Entry
search_ent=Entry(search_frame,font=("Arial",30,"bold"),width=20,relief="solid",bd=2)
search_ent.grid(row=0,column=0,padx=20,pady=20)

#Submit Button
btn=Button(root,text="Get Weather",font=("Arial",20,"bold"),bg="black",fg="#E0F7FA",command=get_weather)
btn.pack(pady=10)

#Weather Display section

weather_frame=Frame(root,bg="#E0F7FA")
weather_frame.pack(pady=20)

weather_icon=Label(weather_frame,text="☁️",font=("Arial",60), bg="#E0F7FA")
weather_icon.pack()

temp_label=Label(weather_frame,text="--°C",font=("Arial",30,"bold"),bg="#E0F7FA")
temp_label.pack()

city_label=Label(weather_frame,text="City, Country",font=("Arial",18),bg="#E0F7FA")
city_label.pack()

desc_label=Label(weather_frame,text="Description",font=("Arial",12,"bold"),bg="#E0F7FA", fg="#555")
desc_label.pack()


#Weather Metrics

metrics_frame=Frame(root,bg="black",pady=20,padx=15)
metrics_frame.pack(pady=20)

Label(metrics_frame,text="🌡️ Temp",font=("Arial",15,"bold"),bg="black",fg="#E0F7FA").grid(row=0,column=0,padx=10)
lbl_temp_val=Label(metrics_frame,text="--",font=("Arial",15,"bold"),bg="black",fg="#E0F7FA")
lbl_temp_val.grid(row=1,column=0)

Label(metrics_frame,text="💧 Humidity",font=("Arial",15,"bold"),bg="black",fg="#E0F7FA").grid(row=0,column=1,padx=10)
lbl_humidity_val=Label(metrics_frame,text="--",font=("Arial",15,"bold"),bg="black",fg="#E0F7FA")
lbl_humidity_val.grid(row=1,column=1)

Label(metrics_frame,text="🌬️ Wind",font=("Arial",15,"bold"),bg="black",fg="#E0F7FA").grid(row=0,column=2,padx=10)
lbl_wind_val=Label(metrics_frame,text="--",font=("Arial",15,"bold"),bg="black",fg="#E0F7FA")
lbl_wind_val.grid(row=1,column=2)






root.mainloop()

















