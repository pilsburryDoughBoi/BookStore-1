def my_function(greeting):
  print("Thank you for choosing The Book Warehouse for donations! We are pleased to see what books you will be donating today")
my_function("greeting")


formatslist = ["paperback, hardcover , audiobook"]
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

if  numcopies == 0:
 print("0 copies. Must donate at least 1 book")

if numcopies >= 0:
  answer = input("Thank you for your donation. Would you like to donate again? [Y/N] ")
  def yes_no(answer):
   print("Thank you for your donation. Would you like to donate again? [Y/N] ")
  yes = set(['yes','y', 'ye', ''])
  no = set(['no','n'])
     
  while True:
    choice = input(answer).lower()
    if choice in yes:
       return my_function True
    elif choice in no:
       return my_function False

#if answer == 'n':
#  print("Thanks for donating")
#elif answer == 'y': 
 # print("One moment we are processing your next donation")
#else: 
 #print("Please type y or n ")

