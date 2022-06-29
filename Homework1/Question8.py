def triangle(x,y,z):
    if x == y and x == z:
        print("eşkenar üçgen")
    elif x == y or y == z or x == z:
        print("ikizkenar üçgen")
    else:
        print("çeşitkenar üçgen")

triangle(5,5,5)
triangle(5,5,4)
triangle(6,5,4)