from datetime import datetime

stock_name = ['LT','APOLLOHOSP','TITAN','BAJFINANCE','INDHOTEL','TATACHEM','MCDOWELL','INDUSINDBK','TATAPOWER','ASIANPAINT','HINDUNILVR','GRASIM','ABFRL','BALRAMCHIN','MINDTREE','INFY','LTI','BSOFT','SUNTV','PVR','INOX','ZEEL','AXISBANK','ICICIBANK','HDFCBANK','KOTAKBANK','CHOLAFIN','BPCL','HPCL','ADANIGREEN','TRENT','MARICO','DABUR','JUBLFOOD','INDALCO','VEDL','JSWSTEEL','TATASTEEL','INDIACEM','RAMCOCEM','DLF','TATAMOTOR','MARUTI','RELIANCE','APOLLOTYRE','EICHERMOT','ESCORTS','TVSMOTOR','DELTACORP','GRANULES',]
total_amount = # total amount in trading account
previous_high = []
current_price = []

for i in range(len(stock_name)):
	previous_high[i] = # get the previous day high in historical data from Zerodha

now = datetime.now()
current_time = now
end_time = now.replace(hour = 14, minute = 30, second = 0, microsecond = 0)

while (current_time <= end_time):
	
	for i in previous_high:
		current_price[i] = # get the current price of stock from Zerodha
	
	for i in current_price:
		
		if(current_price[i] >= previous_high[i]):
			present_stock = stock_name[i]
			present_price = current_price[i]
			buy_stock()
			target_price = buy_price + (buy_price/100)
		    stoploss_price = buy_price - (buy_price/100)
			stock = i
			order = True
			break
	
	while(order):
		
		updated_price = # get the current price of bought stock from Zerodha
		
		if (updated_price >= target_price or updated_price <= stoploss_price):
			sell_stock()
			order = False

	del previous_high[stock]
	del stock_name[stock]
	now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

def buy_stock():
	number_shares = total_amount // present_price
	# execute buy order here in Zerodha trading account
	buy_price = # add the bought price from executed order
	print(stock_name, "bought for Rs", number_shares * buy_price)
	return buy_price

def sell_stock():
	# execute sell order here in Zerodha trading account
	sell_price = # add the sold price from executed order
	print(stock_name, "sold for Rs", number_shares * sell_price)


