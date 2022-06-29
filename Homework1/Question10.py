def sonuc(mid,final,mid_percent,final_percent):
    if mid_percent + final_percent != 100:
        return "Yüzdelik oranların toplamı 100 olması gerekir"

    final_not = mid * mid_percent/100 + final * final_percent/100
    return final_not

print(sonuc(70,30,40,60))