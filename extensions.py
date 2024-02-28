import requests
import json

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            url = f"https://api.exchangerate-api.com/v4/latest/{base}"
            response = requests.get(url)
            data = json.loads(response.text)
            price = data['rates'][quote] * amount
            return price
        except KeyError:
            raise APIException(f"Invalid currency code. Please check and try again.")
        except Exception as e:
            raise APIException(f"An error occurred: {str(e)}")