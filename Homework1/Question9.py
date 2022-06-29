def max_min(list):
    max = list[0]
    min = list[0]
    for num in list:
        if num > max:
            max = num
        if num < min:
            min = num
    print("En büyük sayı: " , max)
    print("En küçük sayı: " , min)

max_min([-25,1,2,3,4,5,500,6,7,8,-35,9,10])