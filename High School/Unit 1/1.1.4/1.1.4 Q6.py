#   a114_divisible.py

# get two numbers from user
nub1 = int(input("give me a number"))
nub2 = int(input("give me another number"))

# loop whle the numbers are not divisible (the remainder is 0)
while (nub1%nub2 != 0):

  # inform user of result 
  print("Hmmm...")
  print("Thats not right...")
  
  # gather user input again
  nub1 = int(input("Give me a diffrent number"))
  nub2 = int(input("Give me another number"))
  
# inform user of result 
print("There we go!")