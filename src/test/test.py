from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
r = cg.get_coins_markets(vs_currency='usd')



def output(x):
    list = []
    for _ in range(x):
        list.append((int(r[_]['market_cap']), r[_]['name']))

    for i in range(x):
        print(list[i][1], list[i][0])

output(4)
