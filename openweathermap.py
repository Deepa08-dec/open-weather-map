import requests
from datetime import datetime, timedelta
import time

class VirtualAssistant:
    def _init_(self, weather_api_key):
        self.weather_api_key = weather_api_key
        self.reminders = []

    def set_reminder(self, message, delay_seconds):
        reminder_time = datetime.now() + timedelta(seconds=delay_seconds)
        self.reminders.append((message, reminder_time))
        print(f"Reminder set for {reminder_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def check_reminders(self):
        current_time = datetime.now()
        for reminder in self.reminders:
            if reminder[1] <= current_time:
                print(f"Reminder: {reminder[0]}")
                self.reminders.remove(reminder)

    def answer_question(self, question):
        # Basic example of answering a simple question
        if question.lower() == "what is your name?":
            return "I am your virtual assistant."
        else:
            return "I'm sorry, I don't know the answer to that question."

    def get_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
            return f"The weather in {city} is {weather_description} with a temperature of {temperature:.2f}°C."
        else:
            return "Unable to fetch weather information."

# Example usage
if _name_ == "_main_":
    weather_api_key = "75737f85a5768cd5f707b0e6c37144a3"  # Replace with your OpenWeatherMap API key
    assistant = VirtualAssistant(weather_api_key)

    # Set a reminder
    assistant.set_reminder("Meeting with team", 10)  # Reminder after 10 seconds

    # Check reminders in a loop
    while True:
        assistant.check_reminders()
        time.sleep(1)  # Check every second

    # Answer a question
    print(assistant.answer_question("What is your name?"))

    # Get weather information
    print(assistant.get_weather("New York"))
