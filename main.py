from config import API_KEY, API_SECRET
from binance.client import Client
import time 
from tradingview_ta import TA_Handler, Interval, Exchange

SYMBOL = 'BTCUSDT'
INTERVAL = Interval.INTERVAL_1_MINUTE
QNTY = 0.0165

client = Client(API_KEY, API_SECRET)


def get_data():
    output = TA_Handler(symbol=SYMBOL,
                        screener='Crypto',
                        exchange = 'Binance',
                        interval = INTERVAL)
    activity = output.get_analysis().summary

    return activity

def place_order(order_type):
    try:
        if (order_type == 'BUY'):
            order = client.create_margin_order(symbol = SYMBOL, side = order_type, type = 'MARKET', quantity = QNTY, isIsolated='TRUE')
            print(order)
        if (order_type == 'SELL'):
            order = client.create_margin_order(symbol = SYMBOL, side = order_type, type = 'MARKET', quantity = QNTY, isIsolated='TRUE')
            print(order)
    except Exception as e:
        print(e)


def main():
    buy = False
    sell = True
    print('bot is started!')
    count = 1
    while True:
        data = get_data()
        print(str(count) + str(data))
        if (data['RECOMMENDATION'] == 'STRONG_BUY' and not buy):
            place_order('BUY')
            buy = not buy
            sell = not sell
        if (data['RECOMMENDATION'] == 'STRONG_SELL' and not sell):
            place_order('SELL')
            buy = not buy
            sell = not sell
        count += 1
        time.sleep(1)




if __name__ == '__main__':
    main()
