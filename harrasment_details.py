from tkinter import ttk
import sqlite3
from datetime import datetime
import geocoder
from geopy.geocoders import Nominatim

import tkinter as tk
def hd():
    def submit_form():
        # Get form data
        incident_description = incident_entry.get()
        safety_tips = safety_entry.get()
        date = date_entry.get()
        selected_types = [type_var.get() for type_var in type_vars]

        # Capture live location

        location = get_location()
        #print(type(location))
        #location = location[1:-1].split(",")


        # Import module


        # Initialize Nominatim API
        geolocator = Nominatim(user_agent="geoapiExercises")

        # Assign Latitude & Longitude
       # Latitude =str(location[0])
       # Longitude = str(location[1])

        # Displaying Latitude and Longitude
        #print("Latitude: ", Latitude)
      #  print("Longitude: ", Longitude)

        # Get location with geocode
        #loc = geolocator.geocode(Latitude + "," + Longitude)

        # Display location
       # print("\nLocation of the given Latitude and Longitude:")
       # print(loc)

        # Store data in SQLite database
        conn = sqlite3.connect('incident_reports.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS incident_reports 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      incident_description TEXT,
                      safety_tips TEXT,
                      date TEXT,
                      selected_types TEXT,
                      location TEXT,
                      timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        c.execute('''INSERT INTO incident_reports 
                     (incident_description, safety_tips, date, selected_types, location) 
                     VALUES (?, ?, ?, ?, ?)''',
                     (incident_description, safety_tips, date, str(selected_types), location))
        conn.commit()
        conn.close()

        # Print confirmation message
        print("Incident report submitted.")

    def get_location():
        # Use geocoder to get live location
        location = geocoder.ip('me').latlng
        return str(location)

    root3 = tk.Tk()
    root3.title("Report Incident")

    shareincident_label = ttk.Label(root3, text="SHARE INCIDENT")

    # Incident Description
    incident_label = ttk.Label(root3, text="Describe the Incident:")
    incident_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    incident_entry = ttk.Entry(root3, width=40)
    incident_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

    # Safety Tips
    safety_label = ttk.Label(root3, text="Safety Tips:")
    safety_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    safety_entry = ttk.Entry(root3, width=40)
    safety_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

    # Date
    date_label = ttk.Label(root3, text="Enter Date:")
    date_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
    date_entry = ttk.Entry(root3, width=20)
    date_entry.grid(row=2, column=1, padx=5, pady=5)

    # Types of Sexual Violence
    types_label = ttk.Label(root3, text="What type of sexual violence did you experience?")
    types_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    type_vars = []
    types = ["Rape/Sexual Assualt", "Chain Snatching/Robbery", "Physical Assault", "Domestic Violence", "Stalking", "Ogling/Staring", "Taking Photos Without permission"]

    for i, type_name in enumerate(types):
        type_var = tk.IntVar()
        type_check = ttk.Checkbutton(root3, text=type_name, variable=type_var)
        type_check.grid(row=4+i, column=0, columnspan=3, padx=5, pady=2, sticky=tk.W)
        type_vars.append(type_var)

    # Submit Button
    submit_button = ttk.Button(root3, text="Submit", command=submit_form)
    submit_button.grid(row=11, column=0, columnspan=3, pady=10)

    root3.mainloop()