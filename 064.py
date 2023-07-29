'''
Poszukaj jakiegoś napisanego wcześniej programu, w którym printowałeś na 
ekranie dużo danych i przerób go używając wybranego przez siebie formatowania.
'''

product_price = {"jajka": (8.29, "op."), "mleko": (3.99, "litr"), "chleb": (9.48, "szt."), "masło": (5.75, "szt."), "jabłka": (0.88, "kg")}
shopping_list = ["jajka", "mleko", "chleb", "jajka", "masło", "jajka", "jabłka", "chleb"]

no_duplicates_list = set(shopping_list)
price = 0

print(f'Twoja lista składa się z {len(no_duplicates_list)} produktów: ')

for i in no_duplicates_list:
    if i in product_price:
        price += product_price[i][0]
        print(f'{i:6} - cena: {product_price[i][0]} za {product_price[i][1]}')

result = f'Cena za wszystkie produkty wynosi: {price:.02f}'
print(result)