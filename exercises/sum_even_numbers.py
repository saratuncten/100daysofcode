#calculate the sum of even numbers between 1 and X
print("Enter a number between 1 and 1000\n")
target = int(input())
if target > 1000:
  print("Please input a number between 1 and 1000")
if target < 1:
  print("Please input a number between 1 and 1000")
else:
  #calculate the sum of all even numbers between 1 and Target
  total = 0
  for n in range(1, target + 1):
    if n%2 == 0:
      total += n
  print(f"Sum of even numbers is: {total}")
