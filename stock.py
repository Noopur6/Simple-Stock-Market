class Stock:
    def __init__(self,stock_symbol,type_of_stock,last_dividend,par_value,fixed_dividend=None):
        self.type_of_stock = type_of_stock
        self.fixed_dividend = fixed_dividend if fixed_dividend else 0
        self.last_dividend = last_dividend
        self.par_value = par_value
        self.stock_symbol = stock_symbol