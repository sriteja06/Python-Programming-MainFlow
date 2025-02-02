import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Function to fetch exchange rates
def fetch_exchange_rates():
    try:
        # Replace with your API key and URL (e.g., https://open.er-api.com/v6/latest/USD)
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url)
        data = response.json()
        if data["result"] == "success":
            return data["rates"]
        else:
            messagebox.showerror("Error", "Failed to fetch exchange rates!")
            return {}
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return {}

# Function to perform conversion
def convert_currency():
    try:
        amount = float(entry_amount.get())
        target_currency = currency_combobox.get()
        if target_currency == "":
            messagebox.showwarning("Warning", "Please select a target currency!")
            return
        converted_amount = amount * rates[target_currency]
        result_label.config(text=f"Converted Amount: {converted_amount:.2f} {target_currency}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount!")

# Function to refresh exchange rates
def refresh_rates():
    global rates
    rates = fetch_exchange_rates()
    if rates:
        messagebox.showinfo("Success", "Exchange rates updated!")

# Initialize main application window
app = tk.Tk()
app.title("USD Currency Converter")
app.geometry("400x300")

# Fetch initial exchange rates
rates = fetch_exchange_rates()

# GUI Layout
label_title = tk.Label(app, text="USD Currency Converter", font=("Arial", 16))
label_title.pack(pady=10)

frame_input = tk.Frame(app)
frame_input.pack(pady=10)

label_amount = tk.Label(frame_input, text="Amount in USD:")
label_amount.grid(row=0, column=0, padx=5, pady=5)

entry_amount = tk.Entry(frame_input, width=20)
entry_amount.grid(row=0, column=1, padx=5, pady=5)

label_currency = tk.Label(frame_input, text="Target Currency:")
label_currency.grid(row=1, column=0, padx=5, pady=5)

currency_combobox = ttk.Combobox(frame_input, values=list(rates.keys()))
currency_combobox.grid(row=1, column=1, padx=5, pady=5)

convert_button = tk.Button(app, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

refresh_button = tk.Button(app, text="Refresh Rates", command=refresh_rates)
refresh_button.pack(pady=5)

result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
app.mainloop()