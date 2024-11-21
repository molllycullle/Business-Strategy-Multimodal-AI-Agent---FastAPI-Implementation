import pandas as pd
import matplotlib.pyplot as plt

class DataAnalyst:
    def analyze_market_data(self, data_path):
        # Read CSV file
        data = pd.read_csv(data_path)

        # Process sales data by region and category
        region_summary = data.groupby('Region')['Sales'].sum()
        category_summary = data.groupby('Product_Category')['Sales'].sum()

        # Plot sales over time
        data['Date'] = pd.to_datetime(data['Date'])
        data.plot(x='Date', y='Sales', kind='line', title='Sales Over Time')
        plt.xlabel('Date')
        plt.ylabel('Sales')
        plt.savefig('data/sales_plot.png')  # Save plot
        plt.close()  # Close plot to avoid multiple figure windows

        return region_summary, category_summary, 'data/sales_plot.png'


if __name__ == "__main__":
    analyst = DataAnalyst()
    region_summary, category_summary, plot_path = analyst.analyze_market_data('data/sample_market_data.csv')
    print("Region-wise Sales Summary:\n", region_summary)
    print("Category-wise Sales Summary:\n", category_summary)
    print("Plot saved at:", plot_path)
