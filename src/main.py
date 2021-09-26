from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()#connecting to API

r=cg.get_coins_markets(vs_currency='usd')#getting information with API
n =int(input()) #number of currencies

l=[]
i=int(0)
for x in r:
	i=i+1
	l.append(x['name'])
	if i==n:
		break
	
print(l)