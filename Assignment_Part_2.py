while True:
    try:
      num1 = int(input('Enter Number 1:'))
      break
    except ValueError:
       print('Oops! That was no a valid number.  Try again...')

while True:
    try:
      num2 = int(input('Enter Number 2:'))
      break
    except ValueError:
       print('Oops! That was no a valid number.  Try again...')

print('Product:', num1 * num2)

try:
  print('Quotient:', num1 / num2)
except ZeroDivisionError:
   print('Oops!  You tried to divide by Zero.')