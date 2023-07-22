'''
Przed Tobą lista produktów, które trzeba kupić:
- jajka, mleko, chleb, jajka, masło, jajka, jabłka, chleb
Przygotuj aplikację która:
- Będzie miała wbudowany cennik wszystkich produktów.
- Przygotuje listę zakupów, złożoną z unikalnych produktów oraz podanej obok liczby produktów do kupienia.
- Wyliczy wartość zakupów i poda ją w podsumowaniu.
Na moje oko, przyda Ci się lista, słownik i zbiór :)
'''

product_price = {"jajka": (8.29, "op."), "mleko": (3.99, "litr"), "chleb": (9.48, "szt."), "masło": (5.75, "szt."), "jabłka": (0.88, "kg")}
shopping_list = ["jajka", "mleko", "chleb", "jajka", "masło", "jajka", "jabłka", "chleb"]

no_duplicates_list = set(shopping_list)
price = 0

print("Twoja lista składa się z ", len(no_duplicates_list), " produktów: ")

for i in no_duplicates_list:
    if i in product_price:
        price += product_price[i][0]
        print(i, "cena:", product_price[i][0], "za", product_price[i][1], sep="\t")

print("Cena za wszystkie produkty wynosi: ", round(price, 2))