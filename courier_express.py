kg_package = float(input())
type_service = input()
km_point_a_to_b = int(input())
price = 0
if type_service == "standard":
    if kg_package < 1:
        price = (km_point_a_to_b * 3) / 100
    elif kg_package < 10:
        price = (km_point_a_to_b * 5) / 100
    elif kg_package < 40:
        price = (km_point_a_to_b * 10) / 100
    elif kg_package < 90:
        price = (km_point_a_to_b * 15) / 100
    elif kg_package < 150:
        price = (km_point_a_to_b * 20) / 100
    total = price
elif type_service == "express":
    if kg_package < 1:
        nadcenka = 3 * 0.0080
        nadcenka_km = kg_package * nadcenka
        total_nadcenka = km_point_a_to_b * nadcenka_km
        price = (km_point_a_to_b * 3) / 100
    elif kg_package < 10:
        nadcenka = 5 * 0.0040
        nadcenka_km = kg_package * nadcenka
        total_nadcenka = km_point_a_to_b * nadcenka_km
        price = (km_point_a_to_b * 5) / 100
    elif kg_package < 40:
        nadcenka = 10 * 0.0005
        nadcenka_km = kg_package * nadcenka
        total_nadcenka = km_point_a_to_b * nadcenka_km
        price = (km_point_a_to_b * 10) / 100
    elif kg_package < 90:
        nadcenka = 15 * 0.0002
        nadcenka_km = kg_package * nadcenka
        total_nadcenka = km_point_a_to_b * nadcenka_km
        price = (km_point_a_to_b * 15) / 100
    elif kg_package < 150:
        nadcenka = 20 * 0.0001
        nadcenka_km = kg_package * nadcenka
        total_nadcenka = km_point_a_to_b * nadcenka_km
        price = (km_point_a_to_b * 20) / 100
    total = price + total_nadcenka
print(f'The delivery of your shipment with weight of {kg_package:.3f} kg. would cost {total:.2f} lv.')
