import tkinter as tk

def convert_miles_to_km():
    try:
        miles = float(entry_miles.get())
        kilometers = miles * 1.60934  # Conversion factor
        label_result.config(text=f"{kilometers:.2f} km")
    except ValueError:
        label_result.config(text="Invalid input!")

# Create the main window
window = tk.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Input for miles
label_miles = tk.Label(window, text="Miles:")
label_miles.grid(row=0, column=0)

entry_miles = tk.Entry(window, width=10)
entry_miles.grid(row=0, column=1)

# Convert button
button_convert = tk.Button(window, text="Convert", command=convert_miles_to_km)
button_convert.grid(row=1, column=0, columnspan=2)

# Result label
label_result = tk.Label(window, text="Result: 0.00 km", font=("Arial", 12, "bold"))
label_result.grid(row=2, column=0, columnspan=2)

# Run the Tkinter event loop
window.mainloop()
