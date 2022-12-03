# Python program to find the maximum of two numbers


def maximum(dia_earth, dia_moon):
    if dia_earth >= dia_moon:
        return dia_earth
    else:
        return dia_moon


# Driver code
dia_earth = 12742
dia_moon = 3475
print(maximum(dia_earth, dia_moon))

# or


dia_earth = 12742
dia_moon = 3475

maximum = max(dia_earth, dia_moon)
if maximum == 12742:
    print("dia_earth")
else:
    print("dia_moon")
print(maximum)
