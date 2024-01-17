import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

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

    # List of stocks to analyze
    stock_list = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']

    # Number of months to look back
    lookback_months = 6

    # Generate stock recommendations
    recommendations = generate_stock_recommendations(stock_list, lookback_months)

    # Display recommendations
    for recommendation in recommendations:
        print(recommendation)

    return {
        body: ""
    }
