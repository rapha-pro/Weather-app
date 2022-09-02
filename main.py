import requests
from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
from PIL import ImageTk, Image

window = Tk()
window.title("Weather app ~by Raphael")
window.geometry("900x500+300+200")
# window.resizable(0, 0)

logo_img = ImageTk.PhotoImage(Image.open("Shared images/logo2.png"))

def getweather():
    global logo_img
    logo_img
    logo.config(image=logo_img)


    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        timezone = TimezoneFinder()
        result = timezone.timezone_at(lng=location.longitude, lat=location.latitude)
        print("result:", result)

        home=pytz.timezone(result)
        print("home:", home)
        local_time=datetime.now(home)
        print("local time:", local_time)
        current_time = local_time.strftime("%I:%M %p")
        print("current time:", current_time)
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather infos
        API_KEY = "4a0a77c6d65c2cbe5e8c97391e524fd6"

        # where to send the request
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

        request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            condit = data['weather'][0]['main']
            weather = data["weather"][0]['description']
            temperature = data["main"]["temp"] - 273.15
            temperature="{:.0f}".format(temperature)
            feel = int(data["main"]['feels_like'] - 273.15)
            pres = data['main']['pressure']
            wi = data['wind']['speed']
            humid = data["main"]["humidity"]
            print(data)
            town = data['name']
            code = data['sys']['country']

            temperat.config(text=(str(temperature)+"°"))
            condition.config(text=(condit,"|","FEELS","LIKE",str(feel)+"°"))

            country.config(text=(town+", "+code))
            win.config(text=wi)
            hum.config(text=humid)
            cond.config(text=weather)
            press.config(text=pres)

        else:
            print("An error occured!")

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid entry!!")

# search box
search_image = PhotoImage(file="Shared images/search.png")
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfield = Entry(window, justify="center", width=19, font=("poppins", 25, "bold"),
                  bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()


#search_icon
search_icon = PhotoImage(file="Shared images/search_icon.png")
myimage_icon = Button(image=search_icon, cursor="hand2", borderwidth=0, bg="#404040",
                      command=getweather)
myimage_icon.place(x=400, y=34, width=55, height=50)

# bind enter key
window.bind("<Return>", lambda event: getweather())

# City
country = Label(font=("arial", 32, "bold"))
country.place(x=500, y=50)

# logo
logo_image = ImageTk.PhotoImage(Image.open("Shared images/blank.png"))
logo = Label(image=logo_image)
logo.place(x=170, y=100)

# Bottom box
frame_image = PhotoImage(file="Shared images/box.png")
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)


# time
name = Label(window, font=("Poppins", 15, "bold"))
name.place(x=30, y=100)

clock = Label(window, font=("Helvetica", 20))
clock.place(x=30, y=130)


# label titles
wind = Label(window, text="WIND", font=("Helvetica", 15, "bold"),
             fg="white", bg="#1ab5ef")
wind.place(x=120, y=400)


humidity = Label(window, text="HUMIDITY", font=("Helvetica", 15, "bold"),
                 fg="white", bg="#1ab5ef")
humidity.place(x=250, y=400)


condition = Label(window, text="CONDITION", font=("Helvetica", 15, "bold"),
                  fg="white", bg="#1ab5ef")
condition.place(x=420, y=400)


pressure = Label(window, text="PRESSURE", font=("Helvetica", 15, "bold"),
             fg="white", bg="#1ab5ef")
pressure.place(x=650, y=400)


# Values
temperat = Label(font=("arial", 70, "bold"), fg="#ee666d")
temperat.place(x=405, y=150)

condition = Label(font=("arial", 15, "bold"))
condition.place(x=405, y=250)


# label values
win = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
win.place(x=126, y=430)

hum = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
hum.place(x=275, y=430)

cond = Label(text="...", font=("arial", 18, "bold"), bg="#1ab5ef")
cond.place(x=420, y=432)

press = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
press.place(x=667, y=430)


window.update()

# Center window each time it's launched
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y-40}")

window.mainloop()