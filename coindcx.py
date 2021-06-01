import streamlit as st
import requests 

url = "https://api.coindcx.com/exchange/ticker"

st.title('Coin Jaadu')
 
response = requests.get(url)
data = response.json()

Options = ['BTCUSDT','ETHUSDT','XRPUSDT','XLMUSDT','ADAUSDT','VETUSDT']
choose = st.sidebar.selectbox("Pick a currency:", Options)

input_inr = st.text_input("Input Indian Rupees:", 0)
input_inr = float(input_inr)
stop_loss = st.text_input("Put Stop Loss:", 0)
stop_loss = float(stop_loss)
Options2 = ['Long','Short']
choose2 = st.selectbox("Choose leverage type:", Options2)


#leverage = 6

user_ticker = choose

#for lis in data:
#    st.write(lis)


for lis in data:
    if lis['market'] == choose:#user input #default
        custom_usdt = float(lis['last_price'])
        
for lis in data:
    if lis['market'] == 'USDTINR':#user input #default
        usdt_price = float(lis['last_price'])        

url2 = "https://api.coindcx.com/exchange/v1/markets_details"
response2 = requests.get(url2)
data2 = response2.json()



    
for lis in data2:
  if lis['coindcx_name'] == choose:
    mlevshort = float(lis['max_leverage_short'])
    mlev = float(lis['max_leverage'])    
    
if choose2 == 'Long':
    leverage = mlev
if choose2 == 'Short':
    leverage = mlevshort
    
st.write(leverage)    

#st.write(data2[0])

if st.sidebar.button('Jaadu'):
    
    stop_loss /= usdt_price
    total_quantity = (input_inr*leverage)/(custom_usdt*usdt_price)
    stop_loss_price = ((custom_usdt*total_quantity) - stop_loss)/total_quantity
    st.write(stop_loss_price)

    

