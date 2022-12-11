from requests import get as rget
from flask import Flask
from bs4 import BeautifulSoup as bs
app = Flask(__name__)

@app.route("/")
def index():
      return """
      /btc for current price of bitcoin
      <br>
      /celo for current price of celo
      <br>
      /tsla for current price of tokenized tesla stonk
      <br>
      /eth for current price of ethereum
      <br>
      /euro for current price of euro coin
      <br>
      /sona for current price of tether gold
      """

@app.route('/sona')
def sona():
      url = "https://coinmarketcap.com/currencies/tether-gold/"
      response = rget(url)
      content = response.content
      soup = bs(content,'lxml')
      divPrice = soup.find_all('div',class_ = "priceValue")
      currentPrice = divPrice[0].find('span').text.replace("$","").replace(",","")
      return currentPrice

@app.route('/celo')
def celo():
      url = "https://coinmarketcap.com/currencies/celo/"
      response = rget(url)
      content = response.content
      soup = bs(content,'lxml')
      divPrice = soup.find_all('div',class_ = "priceValue")
      currentPrice = divPrice[0].find('span').text.replace("$","").replace(",","")
      return currentPrice

@app.route('/tsla')
def tsla():
      url = "https://coinmarketcap.com/currencies/tesla-tokenized-stock-bittrex/"
      response = rget(url)
      content = response.content
      soup = bs(content,'lxml')
      divPrice = soup.find_all('div',class_ = "priceValue")
      currentPrice = divPrice[0].find('span').text.replace("$","").replace(",","")
      return currentPrice

@app.route('/eth')
def eth():
      url = "https://coinmarketcap.com/currencies/ethereum/"
      response = rget(url)
      content = response.content
      soup = bs(content,'lxml')
      divPrice = soup.find_all('div',class_ = "priceValue")
      currentPrice = divPrice[0].find('span').text.replace("$","").replace(",","")
      return currentPrice

@app.route('/euro')
def euro():
      url = "https://coinmarketcap.com/currencies/euro-coin/"
      response = rget(url)
      content = response.content
      soup = bs(content,'lxml')
      divPrice = soup.find_all('div',class_ = "priceValue")
      currentPrice = divPrice[0].find('span').text.replace("$","").replace(",","")
      return currentPrice

@app.route('/btc')
def btc():
      url = "https://coinmarketcap.com/currencies/bitcoin/"
      response = rget(url)
      content = response.content
      soup = bs(content,'lxml')
      divPrice = soup.find_all('div',class_ = "priceValue")
      currentPrice = divPrice[0].find('span').text.replace("$","").replace(",","")
      return currentPrice

if __name__ == '__main__':
      app.run('127.0.0.1',8004,debug=False)
