import requests

def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data.get(crypto, {}).get("usd", "Price not available")

if __name__ == "__main__":
    crypto = input("Enter cryptocurrency (e.g., bitcoin, ethereum): ").lower()
    price = get_crypto_price(crypto)
    print(f"The current price of {crypto.capitalize()} is ${price}.")
