coins = 100
P_even = 1
P_odd = 0
for i in range(coins):
    P_heads = 1 / (2 * i + 1)
    P_odd = P_odd * (1 - P_heads) + (1 - P_odd) * P_heads
print(P_odd)