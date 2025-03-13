#!/usr/bin/env python3
"""
blind_auction.py - A simple bidding system where users can place bids.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/12
License: MIT
Dependencies: None (built-in functions only)

Description:
This script collects bids from users, determines the highest bid, and displays 
the name of the highest bidder along with their bid amount.

Usage:
Run the script and follow the prompts to enter bids:
    python blind_auction.py

Example Output:
    What is your name: Alice
    What's your bid: 100
    Are there any other bidders: yes
    What is your name: Bob
    What's your bid: 150
    Are there any other bidders: no

    Highest bidder is Bob
    Bid: 150
"""

def main():
    bidders = {}  # Dictionary to store bidder names and their respective bids
    another = "yes"  # Control variable to continue bidding

    while another == "yes":
        name = input("What is your name: ")  # Prompt user for their name
        bid = input("What's your bid: ")  # Prompt user for their bid
        another = input("Are there any other bidders: ")  # Ask if there's another bidder

        bidders[name] = bid  # Store the name and bid in the dictionary

    highest = 0  # Variable to track the highest bid
    name_highest = "Nobody"  # Variable to track the name of the highest bidder

    for i, j in bidders.items():  # Loop through each bidder in the dictionary
        if int(j) > highest:  # Compare the current bid with the highest bid
            highest = int(j)  # Update the highest bid if the current bid is higher
            name_highest = i  # Update the name of the highest bidder

    # Display the highest bidder and their bid
    print(f"The highest bidder is: Name: {name_highest} \nBid: {highest}")

if __name__ == '__main__':
    main()  # Run the main function when the script is executed