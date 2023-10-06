from custom_exception import InvalidOptionException
from stock import Stock
from trade import Trade
import math

STOCK_DICT = {
    "TEA":Stock("TEA","Common",0,100),
    "POP":Stock("POP","Common",8,100),
    "ALE":Stock("ALE","Common",23,60),
    "GIN":Stock("GIN","Preferred",8,100,2),
    "JOE":Stock("JOE","Common",13,250)
}

TRADES = {}

def calculate_stock_dividend_yield():
    price = input("Enter price : ")
    stock_symbol = input("Enter Stock Symbol: ")
    if price:
        try:
            price = float(price)
        except:
            print("Invalid Value of Price")
            return
    else
        price = 0
    if stock_symbol in STOCK_DICT:
        stock = STOCK_DICT.get(stock_symbol)
        if stock.type_of_stock == "Common":
            div_yield = stock.last_dividend/price
        elif stock.type_of_stock == "Preferred":
            div_yield = stock.fixed_dividend * stock.par_value/price
        else:
            div_yield = 0
        print("For Stock {}, Dividend Yield is Rs. {} ".format(stock_symbol,div_yield))
    else:
        print("No matching Stock found for this symbol")
    
def calculate_stock_pe_ratio():
    price = input("Enter price : ")
    stock_symbol = input("Enter Stock Symbol: ")
    if price:
        try:
            price = float(price)
        except:
            print("Invalid Value of Price")
            return
    else
        price = 0
    if stock_symbol in STOCK_DICT:
        stock = STOCK_DICT.get(stock_symbol)
        print("For Stock {}, P/E Ratio is {} ".format(stock_symbol,price/stock.last_dividend))
    else:
        print("No matching Stock found for this symbol")

def record_stock_trade():
    stock_symbol = input("Enter Stock Symbol : ")
    if stock_symbol not in STOCK_DICT:
        print("No matching Stock found for this symbol")
        return
    type_of_trade = input("Enter Type of Trade : ")
    quantity_share = input("Enter quantity of shares : ")
    traded_price = input("Enter traded price : ")
    if TRADES.get(stock_symbol):
        TRADES[stock_symbol].append(Trade(type_of_trade,quantity_share,traded_price,STOCK_DICT.get(stock_symbol)))
    print("Trade recorded successfully.")

def calculate_volume_weighted_stock_price():
    stock_symbol = input("Enter Stock Symbol : ")
    if stock_symbol not in STOCK_DICT:
        print("No matching Stock found for this symbol")
        return
    now_ts,tp,total_qty = datetime.now(timezone(timedelta(hours=+5,minutes=+30), 'IST')),0,0
    for trade in [tr for tr in TRADES[stock_symbol] if now_ts-tr.execution_time<=15]:
        tp += trade.traded_price*trade.quantity_of_shares
        total_qty += trade.quantity_of_shares

    print("Volume weighted stock price of Stock {} is Rs. {}".format(stock_symbol,tp/total_qty))
    
def calculate_gbce_all_share_index():
    total_price = 1
    for trade_list in TRADES.values():
        tp,total_qty = 0,0
        for trade in trade_list:
            tp += trade.traded_price*trade.quantity_of_shares
            total_qty += trade.quantity_of_shares
        total_price *= tp/total_qty
    print("GBCE All Share Index of all stocks is {}".format(math.pow(total_price,1/len(TRADES))))
        
    
SERVICE_MAPPER = {
    '1':calculate_stock_dividend_yield,
    '2':calculate_stock_pe_ratio,
    '3':record_stock_trade,
    '4':calculate_volume_weighted_stock_price,
    '5':calculate_gbce_all_share_index
}

def get_available_services():
    return ["Enter {} to {}".format(k,v.__name__.replace('_',' ').upper()) for k,v in SERVICE_MAPPER.items()]

def execute_requested_service(service_option):
    if service_option in SERVICE_MAPPER:
       SERVICE_MAPPER.get(service_option)()
    else:
        raise InvalidOptionException("Invalid option selected")