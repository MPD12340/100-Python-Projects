import requests

api_url = 'https://dummyjson.com/products'


def getData():
    response = requests.get(api_url)
    data = response.json()
    total = data["total"]
    products = data["products"]
    skip = data["skip"]
    limit = data["limit"]
    return total, skip, limit


if __name__ == "__main__":
    total, limit, skip = getData()
    print(total, skip, limit)
