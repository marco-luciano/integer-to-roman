letters = ['M', 'CM','D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
values = [1000, 900,  500, 400, 100,  90, 50, 40, 10, 9,  5, 4,  1]

try :
  num = int(input("Please insert a number between 1 and 3999: "))
except :
  print("An error occured. Please insert a number between 1 and 3999")
  exit()

if (int(num) < 4000 and int(num) >= 1) :
  result = []
  roman_number = ''

  for i in range(len(values)):
    count = num // values[i]
    roman_number += letters[i] * count
    num = num % values[i]

  print(roman_number)
  exit()

else :
  print("Please insert a number between 1 and 3999")
  exit()