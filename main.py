import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")
    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): »")
    period = input("Введите период для данных (например, '1mo' для одного месяца) или введите 'enter', если хотите выбрать конкретные промежутки: ")
    start_date = None
    end_date = None
    if not period:
        start_date = input("Введите дату начала (например - 2022-05-28): ")
        end_date = input("Введите конечную дату (например - 2023-06-28): ")
    else:
        pass

    threshold = int(input("Введите значение порога для анализа данных: "))
    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period, start_date, end_date)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Calculate and display RSI
    stock_data = dd.rsi(stock_data)

    # Calculate and display average_price
    dd.calculate_and_display_average_price(stock_data)

    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Data to CSV
    dd.export_data_to_csv(stock_data, 'csv_data')

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)







if __name__ == "__main__":
    main()
