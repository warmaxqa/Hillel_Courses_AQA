alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n' \
                      '"That depends a good deal on where you want to get to, said the Cat".\n' \
                      '"I dont much care where —— said Alice".\n' \
                      '"Then it doesnt matter which way you go, said the Cat. —— so long as I get somewhere, Alice added as an explanation."\n"' \
                      'Oh, youre sure to do that, said the Cat, if you only walk long enough."'

print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800

total_summ = black_sea + azov_sea

print(f'Загальна площа Чорного та Азовського моря складає {total_summ} км2')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_product = 375291
warehouse_1_to_2 = 250449
warehouse_2_to_3 = 222950

# Загальна кількість товарів на складі = y + x + z

#Кількість товарів на першому складі
y = total_product - warehouse_2_to_3

#Кількість товарів на другому складі
x = warehouse_1_to_2 - y

#Кількість товарів на третьому складі
z = total_product - warehouse_1_to_2

print(f'Кількість товарів на першому сладі {y}')
print(f'Кількість товарів на другому складі {x}')
print(f'Кількість товарів на третьому складі {z}')


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

#Щомісячний платіж
monthly_payment = 1179

#Термін
parts_months = 1.5 * 12

#Загальна вартість
total_payment = monthly_payment * parts_months

#Результат
print(f"Вартість комп'ютера: {total_payment} грн")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

#Дані
a = 8019
b = 9907
c = 2789
d = 7248
e = 7128
f = 19224

#Дільники
divider_a = 8
divider_b = 9
divider_c = 5
divider_d = 6
divider_e = 5
divider_f = 9

#Находження залишків
reminder_a = a % divider_a
reminder_b = b % divider_b
reminder_c = c % divider_c
reminder_d = d % divider_d
reminder_e = e % divider_e
reminder_f = f % divider_f

#Результат = підставляєм необхідні значення, отримуємо результат
print(f'Залишок від ділення {a} на {divider_a} дорівнює {reminder_a}')


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

#Дані
pizza_count_large = 4
pizza_price_large = 274

pizza_count_medium = 2
pizza_price_medium = 218

juice_count = 4
juice_price = 35

cake_count = 1
cake_price = 350

water_count = 3
water_price = 21

#Загальна вартість кожного товару
pizza_large_total = pizza_count_large * pizza_price_large
pizza_medium_total = pizza_count_medium * pizza_price_medium
juice_total = juice_count * juice_price
cake_total = cake_count * cake_price
water_total = water_count * water_price

#Загальна вартість товару в цілому
all_amount = pizza_large_total + pizza_medium_total + juice_total + cake_total + water_total

#Вивід результату
print(f'Загальна сумма замовлення: {all_amount} грн')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

#Дані
total_photos = 232
photos_per_page = 8

all_pages = total_photos // 8

print(f'Ігорю знадобиться {all_pages} cторінок, щоб вклеїти всі фото')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

#Дані

distance_km = 1600
fuel_per_100km = 9
tank_capacity = 48

#Кількість необхідного бензину
fuel_needed = (distance_km / 100) * fuel_per_100km

#Кількість заправок
gas_station_needed = (fuel_needed / tank_capacity)

#Вивід результатів
print(f'Для подорожі потрібно {fuel_needed} літрів бензину')
print(f'Родині необхідно заїхату на заправку {gas_station_needed} рази')



