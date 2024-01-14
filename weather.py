import requests
import tkinter as tk
from tkinter import messagebox
from pprint import pprint


def get_weather(api_key, city):
    base_url = "https://api.tomorrow.io/v4/timelines?location=40.75872069597532,-73.98529171943665&fields=temperature&timesteps=1h&units=metric&apikey=ga75kNtydxjYG6nZhp0eXaB2vvCERbWM"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # You can change this to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")
        return None


def display_weather(api_key, city):
    weather_data = get_weather(api_key, city)
    if weather_data:
        result_str = f"Weather in {city}:\n"
        result_str += f"Temperature: {weather_data['main']['temp']} °C\n"
        result_str += f"Description: {weather_data['weather'][0]['description']}\n"
        result_str += f"Humidity: {weather_data['main']['humidity']}%\n"
        result_str += f"Wind Speed: {weather_data['wind']['speed']} m/s"
        messagebox.showinfo("Weather Information", result_str)
    else:
        messagebox.showerror("Error", "Weather data not available.")


class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather Bot")
        self.geometry("300x150")

        self.api_key = "ga75kNtydxjYG6nZhp0eXaB2vvCERbWM"

        self.city_label = tk.Label(self, text="Enter City:")
        self.city_entry = tk.Entry(self)
        self.city_label.pack(pady=5)
        self.city_entry.pack(pady=5)

        self.get_weather_button = tk.Button(self, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            display_weather(self.api_key, city)
        else:
            messagebox.showwarning("Warning", "Please enter a city.")


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
