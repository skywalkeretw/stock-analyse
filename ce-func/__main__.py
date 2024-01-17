import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


def get_dynamic_stock_list():
    # Fetch a dynamic stock list based on criteria (e.g., high trading volume)
    # You can replace this with your own criteria for selecting interesting stocks
    dynamic_stocks = yf.download('SPY', period='1d')  # Fetch S&P 500 stocks as an example
    dynamic_stocks = dynamic_stocks[dynamic_stocks['Volume'] > dynamic_stocks['Volume'].mean()]
    
    return dynamic_stocks.index.tolist()

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Close']

def generate_stock_recommendations(stock_list, lookback_months):
    recommendations = []
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=lookback_months * 30)).strftime('%Y-%m-%d')

    for stock in stock_list:
        try:
            # Get stock data for the specified date range
            data = get_stock_data(stock, start_date, end_date)

            # Basic recommendation logic (you can replace this with more sophisticated analysis)
            if data.iloc[-1] > data.iloc[-2] > data.iloc[-3]:
                recommendations.append(f"Consider buying {stock} as its recent trend is positive.")
            else:
                recommendations.append(f"Consider monitoring {stock} for potential investment opportunities.")

        except Exception as e:
            recommendations.append(f"Error processing {stock}: {e}")

    return recommendations


def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Close']

def generate_stock_recommendations(stock_list, lookback_months):
    recommendations = []
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=lookback_months * 30)).strftime('%Y-%m-%d')

    for stock in stock_list:
        try:
            # Get stock data for the specified date range
            data = get_stock_data(stock, start_date, end_date)

            # Basic recommendation logic (you can replace this with more sophisticated analysis)
            if data.iloc[-1] > data.iloc[-2] > data.iloc[-3]:
                recommendations.append(f"Consider buying {stock} as its recent trend is positive.")
            else:
                recommendations.append(f"Consider monitoring {stock} for potential investment opportunities.")

        except Exception as e:
            recommendations.append(f"Error processing {stock}: {e}")

    return recommendations


def main(params):

    # Fetch dynamic stock list
    stock_list = get_dynamic_stock_list()
    print(stock_list)
    # Number of months to look back
    lookback_months = 6

    # Generate stock recommendations
    recommendations = generate_stock_recommendations(stock_list, lookback_months)

    # Display recommendations
    for recommendation in recommendations:
        print(recommendation)

    return {
        "body": ""
    }

main({})