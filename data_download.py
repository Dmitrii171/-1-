import yfinance as yf



def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    average_closed_price = data['Close'].mean()
    print(f'Средняя цена закрытия акций за заданный период - {average_closed_price}')

def notify_if_strong_fluctuations(data, threshold):
    diff_in_values = data['Close'].max() - data['Close'].min()
    print(f"Разница между максимальным и минимальным значением цены закрытия составляет - {diff_in_values}")
    if diff_in_values > threshold:
        print("\u001b[31mВНИМАНИЕ!!!Цена акций колебалась более чем на заданный процент за период!")
    else:
        print("Цена акций в пределах нормы!")





