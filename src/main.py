from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

r=cg.get_coins_markets(vs_currency='usd')
n =int(input()) 

l=[]
i=int(0)
for x in r:
	i=i+1
	l.append(x['name'])
	if i==n:
		break
	
print(l)