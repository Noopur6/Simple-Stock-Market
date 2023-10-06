from datetime import datetime,timezone, timedelta
from custom_exception import InvalidQuantityOfShare, InvalidTradeTypeException

class Trade:
    def __init__(self,type_of_trade,quantity_of_shares,traded_price,stock):
    
        if type_of_trade not in ("buy","sell"):
            raise InvalidTradeTypeException("Type of Trade must be either buy or sell")
        self.type_of_trade = type_of_trade
        
        try:
            if float(quantity_of_shares) < 0:
                raise InvalidQuantityOfShare("Invalid value of quantity of shares")
            self.quantity_of_shares = float(quantity_of_shares)
        except:
            raise InvalidQuantityOfShare("Invalid value of quantity of shares")
        
        try:
            if float(traded_price) < 0:
                raise InvalidQuantityOfShare("Invalid value of traded price")
            self.traded_price = float(traded_price)
        except:
            raise InvalidQuantityOfShare("Invalid value of traded price")
    
        self.execution_time = datetime.now(timezone(timedelta(hours=+5,minutes=+30), 'IST'))
        self.stock = stock
