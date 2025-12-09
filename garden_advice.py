# Simple gardening advice app
# Gives tips based on the month the user enters

def get_spring_tips():
    """Prints out spring gardening tips"""
    # This function handles all the spring advice
    print("Spring gardening tips:")
    print("- Start planting seeds indoors")
    print("- Prepare your garden beds")
    print("- Begin pruning trees and shrubs")
    print("- Time to fertilize your lawn")

def get_summer_tips():
    """Prints out summer gardening tips"""
    # Summer is when plants need the most care
    print("Summer gardening tips:")
    print("- Water plants regularly, especially in the morning")
    print("- Harvest vegetables as they ripen")
    print("- Watch out for pests and diseases")
    print("- Mulch to retain moisture")

def get_fall_tips():
    """Prints out fall gardening tips"""
    # Fall is prep time for winter
    print("Fall gardening tips:")
    print("- Plant bulbs for spring flowers")
    print("- Rake and compost fallen leaves")
    print("- Harvest remaining vegetables")
    print("- Prepare plants for winter")

def get_winter_tips():
    """Prints out winter gardening tips"""
    # Winter is mostly planning and protecting plants
    print("Winter gardening tips:")
    print("- Plan your garden for next year")
    print("- Prune dormant trees")
    print("- Protect sensitive plants from frost")
    print("- Start seeds indoors if you have space")

def get_advice(month_num):
    """Gets gardening advice based on month number
    
    Takes a month number (1-12) and calls the appropriate
    function to display tips for that season
    """
    # Check which season the month belongs to
    # Spring months
    if month_num == 3 or month_num == 4 or month_num == 5:
        get_spring_tips()
    # Summer months
    elif month_num == 6 or month_num == 7 or month_num == 8:
        get_summer_tips()
    # Fall months
    elif month_num == 9 or month_num == 10 or month_num == 11:
        get_fall_tips()
    # Winter months (Dec, Jan, Feb)
    elif month_num == 12 or month_num == 1 or month_num == 2:
        get_winter_tips()
    else:
        # Handle invalid input
        print("Invalid month. Please enter a number between 1 and 12.")

# Main part of the program
# Get input from user and convert to number
month = input("Enter a month (1-12): ")
month_num = int(month)
# Call the function to get and display advice
get_advice(month_num)

# TODO: these hardcoded months could be in a list or dict

