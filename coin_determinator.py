coins = [1, 5, 7, 9, 11]
currency = 6


def get_coins(currency):
    if currency in coins:
        return 1
    else:
        numcoin = 0
        numcoins = 99999
        for coin in coins[::-1]:
            if coin <= currency:
                numcoin += currency // coin
                currency = currency % coin
            if currency == 0:
                numcoins = min(numcoin, numcoins)
    return numcoins


print(get_coins(16))
