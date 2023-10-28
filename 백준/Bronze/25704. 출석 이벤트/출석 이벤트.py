N = int(input())
P = int(input())

discounts = []

if N >= 5:
    discounts.append(500)

if N >= 10:
    discounts.append(0.1 * P)

if N >= 15:
    discounts.append(2000)

if N >= 20:
    discounts.append(0.25 * P)

max_discount = max(discounts) if discounts else 0

final_price = P - max_discount

final_price = max(final_price, 0)

print(int(final_price))