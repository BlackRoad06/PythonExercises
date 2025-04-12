hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price
print(f"Total price is {total_price}")

average_price = total_price / len(hairstyles)
print(f"Average Haircut Price: {round(average_price, 2)}")

new_prices = [item - 5 for item in prices]
print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print(f"Total Revenue: {total_revenue}")

average_daily_revenue = total_revenue / 7
print(f"The daily average is: {average_daily_revenue}")

cuts_under_30  = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)
