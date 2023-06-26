# pandas; openpyxl; twilio
import pandas as pd
from twilio.rest import Client

account_sid = "AC48ed502d9216291d34a381ee0ebbbee1"
auth_token = "0f88f158528b53081fbbd2827f42a179"
client = Client(account_sid, auth_token)

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in meses:
    tbVendas = pd.read_excel(f'{mes}.xlsx')
    if (tbVendas['Vendas'] > 55000).any():
        vendedor = tbVendas.loc[tbVendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tbVendas.loc[tbVendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} o vendedor: {vendedor} bateu a meta de R$55.000,00 com {vendas} vendas!')
        message = client.messages.create(
            to="+numero",
            from_="+numeroTwilio",
            body=f'No mês {mes} o vendedor: {vendedor} bateu a meta de R$55.000,00 com {vendas} vendas!')
        print(message.sid)
