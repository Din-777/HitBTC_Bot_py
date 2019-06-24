import time
import queue
import pandas as pd
from hitbtc import HitBTC
from trading.trading import Trading

tzLocal = tz.tzlocal()
pKey = 'YGzq3GQP9vIybW8CcT6+e3pBqX8Tgbr6'
sKey = 'B37LaDlfa70YM9gorzpjYGQAZVRNXDj3'

hitbtc = HitBTC()
hitbtc.start()
time.sleep(2)
hitbtc.login(key=pKey, secret=sKey)
time.sleep(1)

trading = Trading()

hitbtc.request_balance()
hitbtc.subscribe_candles(symbol='BTCUSD', period='M1', limit=5)


while True:
    try:
        data = hitbtc.recv()
        if 'snapshotCandles' in data:
            df = pd.DataFrame(data=data[2]['data'])
            df.timestamp = pd.to_datetime(df.timestamp).dt.tz_convert('Asia/Oral')
            df.index = df['timestamp']
        if 'updateCandles' in data:
            d=data[2]['data'][0]
            ser = pd.Series(d)
            ser.timestamp = pd.to_datetime(ser.timestamp).tz_convert('Asia/Oral')
            ser.name = ser.timestamp
            if df['timestamp'][-1] != ser['timestamp']:             
                df = df.append(ser)
                print(df)
            else:
                df.iloc[-1] = ser
                print('update')
    except queue.Empty:
        continue

hitbtc.stop()