# Simple gardening advice app
# Gives tips based on the month

month = input("Enter a month (1-12): ")

# Convert to integer
month_num = int(month)

# Spring months
if month_num == 3 or month_num == 4 or month_num == 5:
    print("Spring gardening tips:")
    print("- Start planting seeds indoors")
    print("- Prepare your garden beds")
    print("- Begin pruning trees and shrubs")
    print("- Time to fertilize your lawn")

# Summer months
elif month_num == 6 or month_num == 7 or month_num == 8:
    print("Summer gardening tips:")
    print("- Water plants regularly, especially in the morning")
    print("- Harvest vegetables as they ripen")
    print("- Watch out for pests and diseases")
    print("- Mulch to retain moisture")

# Fall months
elif month_num == 9 or month_num == 10 or month_num == 11:
    print("Fall gardening tips:")
    print("- Plant bulbs for spring flowers")
    print("- Rake and compost fallen leaves")
    print("- Harvest remaining vegetables")
    print("- Prepare plants for winter")

# Winter months
elif month_num == 12 or month_num == 1 or month_num == 2:
    print("Winter gardening tips:")
    print("- Plan your garden for next year")
    print("- Prune dormant trees")
    print("- Protect sensitive plants from frost")
    print("- Start seeds indoors if you have space")

else:
    print("Invalid month. Please enter a number between 1 and 12.")

# TODO: should probably make this into functions instead of having everything here
# TODO: add more comments to explain what's happening
# TODO: these hardcoded months could be in a list or dict

