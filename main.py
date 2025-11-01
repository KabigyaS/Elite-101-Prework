
#Welcome the user
print("Welcome to the Store Chatbot!")
name = input("What is your name? ")

# Example product inventory
Clothing = [
    {"type": "T-shirt", "Count": 2},
    {"type": "Jacket", "Count": 2},
    {"type": "Pant", "Count": 3}
]

print("Nice to meet you, " + name)
print("How can I help you today?")
print("1. Return an Item")
print("2. Exchange an Item")
print("3. Check Product Availability")
print("4. Customer Support")
print("5. Exit")
choice = int(input("Which option do you choose? "))

#Options
if choice == "1":
    product = input("Which item would you like to return? ")
    reason = input("Can you tell us why you’re returning the " + product + "? ")
    for x in Clothing:
        if x["type"]==product:
            x["Count"] +=1 
    print("Thank you! We’ve started your return for the " + product + ".")
    print("You’ll receive an email with return instructions within 24 hours.")

elif choice == "2":
    product = input("Which item would you like to exchange? ").lower()
    newItem = input("What would you like to exchange it for? ").lower()
    print("Let me check availability for " + newItem + "...")
    for x in Clothing:
        if x["type"]==product:
            x["Count"] -=1 
        elif x["type"]==newItem:
            x["Count"] +=1 
    print("Good news! The " + newItem + " is available.")
    print("Your exchange request for the " + product + " has been submitted.")
    print("We’ll email you shipping details shortly.")

elif choice == "3":
    print("You chose to check product availability.")
    product = input("What product are you looking for? ")
    found = False
    for x in Clothing:
        if x["type"].lower() == product.lower():
            print("Yes, we have " + str(x["Count"]) + " " + product + "(s) in stock.")
            found = True
            break
    if not found:
        print("Sorry, we don’t currently have that item in stock.")

elif choice == "4":
    print("You chose Customer Support.")
    print("You can reach our support team at Store@gmail.com or call 111-111-1111.")
    issue = input("Would you like to describe your issue briefly? ")
    print("Thanks for letting us know. We'll make sure someone follows up about: " + issue)

elif choice == "5":
    print("Thank you for visiting CoreStore! Have a great day, " + name + "!")

else:
    print("Sorry, that’s not a valid option. Please try again.")