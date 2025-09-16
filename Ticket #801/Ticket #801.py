import tkinter as tk
import requests
import threading

def get_weather():
    city = entry.get()
    data = requests.get(f"https://wttr.in/{city}?format=3").text
    label.config(text=data, font=('arial', 20, 'bold'), anchor='center')
    

root = tk.Tk()
root.geometry("300x300")
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Weather", command=lambda:threading.Thread(target=get_weather()).start())
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
