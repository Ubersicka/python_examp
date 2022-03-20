price_mominsko_party = float(input())
count_love_quotes = int(input())
count_roses = int(input())
count_key_chain = int(input())
count_caricature = int(input())
count_wishes = int(input())

price_love_quotes = 0.60
price_roses = 7.20
price_key_chain = 3.60
price_caricature = 18.20
price_wishes = 22

sum_price = count_love_quotes * price_love_quotes + count_roses * price_roses + count_key_chain * price_key_chain \
            + count_caricature * price_caricature + count_wishes * price_wishes
count_all = count_love_quotes + count_roses + count_key_chain + count_caricature + count_wishes

if count_all > 25:
        sum_price *= 0.65
hosting = sum_price * 0.10
profit = sum_price - hosting
diff = abs(profit - price_mominsko_party)
if sum_price > price_mominsko_party:
        print(f'Yes! {diff:.2f} lv left.')
else:
        print(f'Not enough money! {diff:.2f} lv needed.')
