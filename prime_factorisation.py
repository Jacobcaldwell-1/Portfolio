''' 
As a bit of context: This peice of code was a challenge, in two ways, firstly because I was challenged to make it, secondly I had no idea what prime factorisation was beforehand, which made this a little tricky.
I am pround of this code because in figuring out how to get it to work I used a lot of new ways of doing things; how to use modulus, f strings and the append operator.
'''

def check(number):
  remainders = [int] * number

  for i in range (1,number):
    remainders[i] = number % i
  zero_count = 0

  for i in range (0, len(remainders)):
    if remainders[i] == 0:
     zero_count = zero_count + 1
  if zero_count > 2 or zero_count == 2:
      prime = False

  else:
      prime = True
  return prime

original = int(input("please enter value for prime factorization: "))
while original < 2:
    original = int(input("please enter a number greater than 1 for prime factorization: "))
number = original
divisor_list = []
while number > 1:
  divisor = 2
  condition = False
  while condition == False:
    r = number % divisor
    if r != 0: 
      divisor += 1
      primecheck = check(divisor)
      while primecheck == False:
        divisor += 1
        primecheck = check(divisor)
        if divisor > number:
          print("Error, divisor has become too large.")
          
    else:
      condition = True
  divisor_list.append(divisor)
  number = number / divisor
print(f"The prime factorization of {original} is {divisor_list}")
