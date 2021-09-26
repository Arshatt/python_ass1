from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

r = cg.get_coins_markets(vs_currency='usd')

def output(x):
    l = []
    for _ in range(x):
        l.append((int(r[_]['market_cap']), r[_]['name']))

    for i in range(x):
        print(l[i][1], l[i][0])

output(4)
