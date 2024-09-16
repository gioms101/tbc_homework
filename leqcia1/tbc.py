import tkinter as tk

CURRENCIES = ["USD", "GEL", "EUR"]
currency_rate = {
    "EUR/USD": 1.06, "USD/EUR": 0.87,
    "EUR/GEL": 2.91, "GEL/EUR": 0.33,
    "USD/GEL": 2.64, "GEL/USD": 0.36,
    "GEL/GEL": 1, "USD/USD": 1,
    "EUR/EUR": 1
}

window = tk.Tk()
window.title("Exchange App")

def get_result():
    try:
        amount = float(from_inpt.get())
        final_result = amount * currency_rate[f"{currency1.get()}/{currency2.get()}"]
        result_of_exchange['text'] = f"Converted: {final_result:.2f} {currency2.get()}"
        result_of_exchange['font'] = ("Arial", 10, "bold")
        result_of_exchange["fg"] = "green"
    except ValueError:
        result_of_exchange['text'] = "Please enter a number."

def reset_func():
    from_inpt.delete(0, tk.END)
    result_of_exchange['text'] = ""

from_inpt = tk.Entry(window)
from_inpt.place(relx=0.4, rely=0.381)

label1 = tk.Label(window, text="From",font=("Arial", 10, "bold"))
label1.place(relx=0.503, rely=0.33)

currency1 = tk.StringVar()
currency1.set("USD")

dropmenu1 = tk.OptionMenu(window, currency1, *CURRENCIES)
dropmenu1.place(relx=0.498, rely=0.37)

new_label = tk.Label(window, text="To",font=("Arial", 10, "bold"))
new_label.place(relx=0.56, rely=0.33)

currency2 = tk.StringVar()
currency2.set("GEL")

dropmenu2 = tk.OptionMenu(window, currency2, *CURRENCIES)
dropmenu2.place(relx=0.55, rely=0.37)

btn_convert = tk.Button(window, text="Convert",padx=10, font=('calibri', 10, 'bold'),command=get_result)
btn_convert.place(relx=0.4, rely=0.5)

result_of_exchange = tk.Label(window, text="")
result_of_exchange.place(relx=0.4, rely=0.447)

btn_reset = tk.Button(window, text="Reset",font=('calibri', 10, 'bold'), padx=10,command=reset_func)
btn_reset.place(relx=0.458, rely=0.5)

window.mainloop()