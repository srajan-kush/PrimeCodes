a = input("Enter a string: ")
a = a.casefold()
b = reversed(a)
if list(a) == list(b):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

print(list(a))

# txt = "Hello, And Welcome To My World!"

# x = txt.casefold()

# print(x)

