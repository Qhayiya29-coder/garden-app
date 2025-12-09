# Simple gardening advice app
# Gives tips based on the month

def get_spring_tips():
    """Returns spring gardening tips"""
    print("Spring gardening tips:")
    print("- Start planting seeds indoors")
    print("- Prepare your garden beds")
    print("- Begin pruning trees and shrubs")
    print("- Time to fertilize your lawn")

def get_summer_tips():
    """Returns summer gardening tips"""
    print("Summer gardening tips:")
    print("- Water plants regularly, especially in the morning")
    print("- Harvest vegetables as they ripen")
    print("- Watch out for pests and diseases")
    print("- Mulch to retain moisture")

def get_fall_tips():
    """Returns fall gardening tips"""
    print("Fall gardening tips:")
    print("- Plant bulbs for spring flowers")
    print("- Rake and compost fallen leaves")
    print("- Harvest remaining vegetables")
    print("- Prepare plants for winter")

def get_winter_tips():
    """Returns winter gardening tips"""
    print("Winter gardening tips:")
    print("- Plan your garden for next year")
    print("- Prune dormant trees")
    print("- Protect sensitive plants from frost")
    print("- Start seeds indoors if you have space")

def get_advice(month_num):
    """Gets gardening advice based on month number"""
    # Spring months
    if month_num == 3 or month_num == 4 or month_num == 5:
        get_spring_tips()
    # Summer months
    elif month_num == 6 or month_num == 7 or month_num == 8:
        get_summer_tips()
    # Fall months
    elif month_num == 9 or month_num == 10 or month_num == 11:
        get_fall_tips()
    # Winter months
    elif month_num == 12 or month_num == 1 or month_num == 2:
        get_winter_tips()
    else:
        print("Invalid month. Please enter a number between 1 and 12.")

# Main part of the program
month = input("Enter a month (1-12): ")
month_num = int(month)
get_advice(month_num)

# TODO: add more comments to explain what's happening
# TODO: these hardcoded months could be in a list or dict

