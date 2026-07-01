import requests
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        data = response.json()
        price = float(data['data']['priceUsd'])
        total_amount = value * price
        print(f"${total_amount:,.4f}")
    except requests.RequestException:
        print("Request error occurred")
        sys.exit(1)

if __name__ == "__main__":
    main()