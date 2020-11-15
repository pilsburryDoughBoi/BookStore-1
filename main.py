def my_function(greeting):
  print("Thank you for choosing The Book Warehouse for donations! We are pleased to see what books you will be donating today")
my_function("greeting")


formatslist = ["paperback", "hardcover", "audiobook"]
i = 0
while i < len(formatslist):
  print(formatslist[i])
  i = i + 1

genre = input("Enter genre of the book:")
print("genre: " + genre)

novelname = input("Enter book name:")
print("Book name is: " + novelname)

numcopies = input("Enter amount of copies donated:")
print("Amount donated: " + numcopies + " Success")


numcopies = input("")
while numcopies < 6:
  print(numcopies)
  if numcopies == 0:
    break
    print("0 copies. Must donate at least 1 book")
while numcopies > 6:
  print(numcopies)
  numcopies += 1
  print("Thank you for your donation")
finalaction = input("Would you like to donate again? ")
print(finalaction)

a = "yes" 
b = "no"

if b > a:
  print("Thanks for donating")
else:
  print("One moment we are processing your next donation")