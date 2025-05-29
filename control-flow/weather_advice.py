# this script gives advice based on the weather input
usersInput = input("What's the weather like today? (sunny/rainy/cold):. ").lower()

# Check the weather and provide advice suing match case
if usersInput == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif usersInput == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif usersInput == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")


# Check the weather and provide advice suing match case
# match usersInput:
#     case "sunny":
#         print("Wear a t-shirt and sunglasses.")
#     case "rainy":
#         print(" Don't forget your umbrella and a raincoat.")
#     case "cold":
#         print(" Make sure to wear a warm coat and a scarf..")
#     case _:
#         print(" Sorry, I don't have recommendations for this weather.")

