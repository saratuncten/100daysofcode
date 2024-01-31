#print each number from 1 to 100 (including 100)
#when the number is divisible by 3, print Fizz, when the number is divisible by 5 print "Buzz"
#if the nmber is divisble by both 3 and 5, print FizzBuzz

for n in range(1,101):
  if n%3 == 0 and n%5 == 0:
    print("FizzBuzz\n")
  elif n%3 == 0:
    print("Fizz\n")
  elif n%5 == 0:
    print("Buzz\n")
  else:
    print(f"{n}\n")
