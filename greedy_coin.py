def Greedy_Coin(n, coin_types):
    count = 0
    for coin in coin_types:
        count += n // coin
        n%=coin
    return count
    
#run
n=1260
coin_types = [500,100,50,10]
Greedy_Coin(n, coin_types)
