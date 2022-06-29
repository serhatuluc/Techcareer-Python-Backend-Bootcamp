def sumofodd(list):
    toplam = 0
    for num in list:
        if num % 2 == 1:
            toplam += num 
    print(toplam)

sumofodd([1, 2, 3, 4, 5, 6, 7, 9, 11, 126,267,544, 1773, 1258,4637])