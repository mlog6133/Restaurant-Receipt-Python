'''

NAME:   Marquis Logan

DATE:   September 19, 2022

ASSN:   ASSIGNMENT A5

DESC:   THE FOLLOWING PYTHON MODULE PRINTS OUT A RECEIPT FROM FAMOUS
        RESTAURANT, YOUR OWN. THE USER WILL ENTER THE PRICE OF THEIR
        APPETIZER, THEIR ENTREE, AND THEIR DESSERT.  THEY WILL ALSO
        ENTER THE AMOUNT OF THEIR TIP, 0%, 10%, 15%, OR 20%.
        
        YOUR CODE WILL SHOW ALL THE ITEMS AND THEIR PRICES, THE FINAL
        SUBTOTAL, A 10% TAX (ON THE SUBTOTAL), THE TIP AMOUNT, AND THE
        FINAL AMOUNT TO BE CHARGED.
        
'''
print('The Delicious Steakhouse Receipt!')
print('--------------------------------')
# ASK THE USER FOR THE PRICE OF THEIR APPETIZER AND STORE THE FLOATING
# POINT VALUE IN THE OBJECT, appetizer.  THEY CAN ENTER 0.00 IF THEY
# DID NOT ORDER AN APPETIZER.
appetizer = float(input(f"Enter the price of your appetizer (0.00 if you didn't indulge):\t$ "))


# ASK THE USER FOR THE PRICE OF THEIR ENTREE AND STORE THE FLOATING
# POINT VALUE IN THE OBJECT, entree.  THEY CAN ENTER 0.00 IF THEY
# DID NOT ORDER AN ENTREE.
entree = float(input(f"Enter the price of your entree (0.00 if you didn't indulge):  \t$ "))

# ASK THE USER FOR THE PRICE OF THEIR DESSERT AND STORE THE FLOATING
# POINT VALUE IN THE OBJECT, dessert.  THEY CAN ENTER 0.00 IF THEY
# DID NOT ORDER AN DESSERT.
dessert = float(input(f"Enter the price of dessert (0.00 if you didn't indulge): \t$ "))


# CALCULATE THE SUBTOTAL AND STORE IT AS A FLOATING POINT VALUE IN
# THE OBJECT, subtotal.
subtotal = appetizer + entree + dessert
print(f"Your subtotal is:\t\t\t\t\t\t$","{:.2f}".format(subtotal))


# CALCULATE THE TAX AMOUNT AS A FLOATING POINT OBJECT, tax_amount.
tax_amount = 0.1
tax_total = subtotal * tax_amount
print(f'Tax (10%):\t\t\t\t\t', '\t\t$',"{:.2f}".format(tax_total))

# ASK THE USER FOR THEIR TIP AMOUNT, 0, 10, 15, OR 20 AND STORE THE
# INTEGER VALUE IN THE OBJECT, tip_percent.  THEY CAN ENTER 0 IF THEY
# DID NOT GIVE A TIP.
tip_percent = int(input("Please select your tip percentage e.g 0, 5, 10, 15, 20: 1\t% "))
tip_amount = subtotal * tip_percent * 0.01
if (tip_percent == 0) or \
   (tip_percent == 5) or \
   (tip_percent == 10) or \
   (tip_percent == 15) or \
   (tip_percent == 20):
    print(f'Tip:\t\t\t\t\t\t\t','\t$',"{:.2f}".format(tip_amount))
print('----------------------------------------------------------------------')    

# CALCULATE THE TOTAL AMOUNT BY ADDING THE SUBTOTAL, THE TAX AMOUNT, AND
# THE TIP AMOUNT, AND STORE THIS FLOATING POINT VALUE IN AN OBJECT NAMED
# total
total = subtotal + tax_total + tip_amount
print(f"Your total is:\t\t\t\t\t", '\t\t$', "{:.2f}".format(total))
print('Thanks for dining at the Delicious Steakhouse, see you soon!')


###############
### THE END ###
###############




