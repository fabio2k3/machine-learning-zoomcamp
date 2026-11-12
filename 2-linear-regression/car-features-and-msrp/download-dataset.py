import urllib.request

url = "https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv"
output = "data.csv"

urllib.request.urlretrieve(url, output)
print(f"Descargado en: {output}")