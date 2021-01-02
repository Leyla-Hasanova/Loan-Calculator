from tkinter import messagebox
import tkinter as tk
import os

ui_settings = {
    'general': {
        'title': 'Loan Calculator',
        'width': 500,
        'height': 300,
    },
    'rate_label': {
        'text': 'Interest rate',
        'width': 250,
        'height': 50,
        'x': 0,
        'y': 0
    },
    'rate_input': {
        'width': 250,
        'height': 50,
        'x': 250,
        'y': 0
    },
    'years_label': {
        'text': 'Number of years',
        'width': 250,
        'height': 50,
        'x': 0,
        'y': 50
    },
    'years_input': {
        'width': 250,
        'height': 50,
        'x': 250,
        'y': 50
    },
    'loan_amount_label': {
        'text': 'Loan Amount',
        'width': 250,
        'height': 50,
        'x': 0,
        'y': 100
    },
    'loan_amount_input': {
        'width': 250,
        'height': 50,
        'x': 250,
        'y': 100
    },
    'monthly_payment_label': {
        'text': 'Monthly Payment',
        'width': 250,
        'height': 50,
        'x': 0,
        'y': 150
    },
    'monthly_payment_output': {
        'width': 250,
        'height': 50,
        'x': 250,
        'y': 150
    },
    'total_payment_label': {
        'text': 'Total Payment',
        'width': 250,
        'height': 50,
        'x': 0,
        'y': 200
    },
    'total_payment_output': {
        'width': 250,
        'height': 50,
        'x': 250,
        'y': 200
    },
    'calculate_button': {
        'text': 'Calculate',
        'width': 250,
        'height': 50,
        'x': 250,
        'y': 250
    }
}
win = tk.Tk()
win.geometry(str(ui_settings['general']['width']) + 'x' + str(ui_settings['general']['height']))
win.resizable(0, 0)
win.title(ui_settings['general']['title'])


def calculate_total_amount(loan_amount, number_of_years, interest_rate):
    total_amount = loan_amount * (1 + interest_rate / 100 * number_of_years)
    return round(total_amount, 2)


def calculate_monthly_payment(loan_amount, number_of_years, interest_rate):
    number_of_payments = number_of_years * 12
    return round(calculate_total_amount(loan_amount, number_of_years, interest_rate) / number_of_payments, 2)


inputs = []

rate_label = tk.Label(win, text=ui_settings['rate_label']['text'])
rate_input = tk.Entry(win)
inputs.append(rate_input)
rate_label.place(
    width=ui_settings['rate_label']['width'],
    height=ui_settings['rate_label']['height'],
    x=ui_settings['rate_label']['x'],
    y=ui_settings['rate_label']['y']
)
rate_input.place(
    width=ui_settings['rate_input']['width'],
    height=ui_settings['rate_input']['height'],
    x=ui_settings['rate_input']['x'],
    y=ui_settings['rate_input']['y']
)

years_label = tk.Label(win, text=ui_settings['years_label']['text'])
years_input = tk.Entry(win)
inputs.append(years_input)
years_label.place(
    width=ui_settings['years_label']['width'],
    height=ui_settings['years_label']['height'],
    x=ui_settings['years_label']['x'],
    y=ui_settings['years_label']['y']
)
years_input.place(
    width=ui_settings['years_input']['width'],
    height=ui_settings['years_input']['height'],
    x=ui_settings['years_input']['x'],
    y=ui_settings['years_input']['y']
)

loan_amount_label = tk.Label(win, text=ui_settings['loan_amount_label']['text'])
loan_amount_input = tk.Entry(win)
inputs.append(loan_amount_input)
loan_amount_label.place(
    width=ui_settings['loan_amount_label']['width'],
    height=ui_settings['loan_amount_label']['height'],
    x=ui_settings['loan_amount_label']['x'],
    y=ui_settings['loan_amount_label']['y']
)
loan_amount_input.place(
    width=ui_settings['loan_amount_input']['width'],
    height=ui_settings['loan_amount_input']['height'],
    x=ui_settings['loan_amount_input']['x'],
    y=ui_settings['loan_amount_input']['y']
)

monthly_payment_label = tk.Label(win, text=ui_settings['monthly_payment_label']['text'])
monthly_payment = tk.StringVar()
monthly_payment_output = tk.Label(win, textvariable=monthly_payment)
monthly_payment_label.place(
    width=ui_settings['monthly_payment_label']['width'],
    height=ui_settings['monthly_payment_label']['height'],
    x=ui_settings['monthly_payment_label']['x'],
    y=ui_settings['monthly_payment_label']['y']
)
monthly_payment_output.place(
    width=ui_settings['monthly_payment_output']['width'],
    height=ui_settings['monthly_payment_output']['height'],
    x=ui_settings['monthly_payment_output']['x'],
    y=ui_settings['monthly_payment_output']['y']
)

total_payment_label = tk.Label(win, text=ui_settings['total_payment_label']['text'])
total_payment = tk.StringVar()
total_payment_output = tk.Label(win, textvariable=total_payment)
total_payment_label.place(
    width=ui_settings['total_payment_label']['width'],
    height=ui_settings['total_payment_label']['height'],
    x=ui_settings['total_payment_label']['x'],
    y=ui_settings['total_payment_label']['y']
)
total_payment_output.place(
    width=ui_settings['total_payment_output']['width'],
    height=ui_settings['total_payment_output']['height'],
    x=ui_settings['total_payment_output']['x'],
    y=ui_settings['total_payment_output']['y']
)





def calculate():
    for input in inputs:
        try:
            if int(input.get()) <= 0:
                messagebox.showerror(title='Error', message='Wrong input!')
                break
        except:
            messagebox.showerror(title='Error', message='Wrong input!')
            break

    rate = int(rate_input.get())
    years = int(years_input.get())
    loan = int(loan_amount_input.get())
    monthly = calculate_monthly_payment(loan, years, rate)
    total = calculate_total_amount(loan, years, rate)
    monthly_payment.set(str(monthly))
    total_payment.set(str(total))

    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(location, 'results.txt'), 'a')

    result = 'Interest rate: ' + str(rate)
    result += '; Number of years: ' + str(years)
    result += '; Loan Amount: ' + str(loan)
    result += '; Monthly Payment: ' + str(monthly)
    result += '; Total Payment: ' + str(total) + '\n'
    f.write(result)
    f.close()


calculate_button = tk.Button(win, text=ui_settings['calculate_button']['text'], command=calculate)
calculate_button.place(
    width=ui_settings['calculate_button']['width'],
    height=ui_settings['calculate_button']['height'],
    x=ui_settings['calculate_button']['x'],
    y=ui_settings['calculate_button']['y']
)

win.mainloop()
