# Author Gregory Mertens
# Date Sept 20th 2025
# Program will import data from CSV file and print out the data in a text window and graphs.
# I confirm that this program has not been copied from any other student or website.

import csv
import matplotlib.pyplot as plt
#def to read the provided CSV file
def read_prices_from_csv(filename):
    prices = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                try:
                    prices.append(float(value))
                except ValueError:
                    print(f"Skipping invalid entry: {value}")
    return prices

#def to analyze prices, and provide information
def analyze_prices(prices):
    average_price = sum(prices) / len(prices)
    max_price = max(prices)
    min_price = min(prices)
    highest_Week = prices.index(max_price) + 1
    lowest_Week = prices.index(min_price) + 1

    week_under_1 = sum(1 for price in prices if price < 1.00)
    week_between_1_and_105 = sum(1 for price in prices if 1.00 <= price <= 1.05)
    week_between_105_and_110 = sum(1 for price in prices if 1.05 < price <= 1.10)
    week_between_110_and_115 = sum(1 for price in prices if 1.10 < price <= 1.15)
    week_above_115 = sum(1 for price in prices if price > 1.15)

    print(f"Average price: {average_price:.2f}")
    print(f"Highest price: {max_price:.2f} (Week {highest_Week})")
    print(f"Lowest price: {min_price:.2f} (Week {lowest_Week})")
    print(f"Weeks under $1.00: {week_under_1}")
    print(f"Weeks between $1.00 and $1.05: {week_between_1_and_105}")
    print(f"Weeks between $1.05 and $1.10: {week_between_105_and_110}")
    print(f"Weeks between $1.10 and $1.15: {week_between_110_and_115}")
    print(f"Weeks above $1.15: {week_above_115}")
    return {
        "Under $1.00": week_under_1,
        "$1.00–$1.05": week_between_1_and_105,
        "$1.05–$1.10": week_between_105_and_110,
        "$1.10–$1.15": week_between_110_and_115,
        "Above $1.15": week_above_115
    }
#Def to create and show charting
def charts(prices, ranges): #used AI to figure out how to combine both charts in a single window, instead of pie showing after closing line
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Line chart for weekly prices
    ax1.plot(range(1, len(prices)+1), prices, marker='o', linestyle='-', color='blue')
    ax1.set_title('Weekly Widget Prices')
    ax1.set_xlabel('Week Number')
    ax1.set_ylabel('Price ($)')
    ax1.grid(True)

    # Pie chart for price ranges
    labels = list(ranges.keys())
    sizes = list(ranges.values())
    ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax2.set_title("Price Range Distribution")

    plt.tight_layout()
    plt.show()




def main():
    filename = "weeklyPrices.csv"
    prices = read_prices_from_csv(filename)
    ranges = analyze_prices(prices)
    charts(prices, ranges)

    print("Program complete")
    input("Press enter to exit")



main()

