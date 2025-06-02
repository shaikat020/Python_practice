from currency_converter import CurrencyConverter

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyConverter()
    result = c.convert(amount, from_currency, to_currency)
    return result

amount= float(input("Enter the amount to convert : "))


from_currency= input("Enter the currency to convert from : ").upper()

to_currency= input("Enter the currency to convert from : ").upper()

convert_amount = convert_currency(amount, from_currency, to_currency)

print(f"{amount} {from_currency} = {convert_amount} {to_currency}")