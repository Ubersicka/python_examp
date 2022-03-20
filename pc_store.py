usd_price_processor = float(input())
usd_price_video_card = float(input())
usd_price_ram = float(input())
quantity_ram = int(input())
discount_percent = float(input())

bgn_price_processor = usd_price_processor * 1.57
bgn_price_video_card = usd_price_video_card * 1.57
bgn_price_ram = usd_price_ram * 1.57
total_price_ram = bgn_price_ram * quantity_ram
price_processor_after_discount = bgn_price_processor - bgn_price_processor * discount_percent
price_video_card_after_discount = bgn_price_video_card - bgn_price_video_card * discount_percent

total_sum = total_price_ram + price_processor_after_discount + price_video_card_after_discount

print(f'Money needed - {total_sum:.2f} leva.')
