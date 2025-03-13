# Blind_auction
Your Blind Auction Script - Difficulty: Easy

## Author:
Carlos Valerio (CarlosValerioM)

## Date:
2025/03/12

## License:
MIT License

## Dependencies:
None (built-in functions only)

## Description:
'blind_auction.py' is a simple Python script that allows users to place bids in an auction. 

It collects bids from users, determines the highest bid, and displays the name of the highest bidder along with the bid amount.

The script asks for the following inputs:
1. The user's name.
2. The bid amount they want to place.
3. Whether there are any other bidders.

After collecting all bids, the script determines the highest bid and prints the name and bid of the highest bidder.

## Usage:

1. Clone this repository:

```bash
git clone https://github.com/CarlosValerioM/blind_auction.git
```
Navigate to the project directory:
```bash
cd blind_auction
```
Run the script:
```bash
python blind_auction.py
```
The script will prompt you for input, and based on your responses, it will calculate the highest bid and display the winner.

## Example Output:
What is your name: Alice

What's your bid: 100

Are there any other bidders: yes

What is your name: Bob

What's your bid: 150

Are there any other bidders: no

Highest bidder is Bob

Bid: 150

## How it works:
The user inputs their name, the amount they are bidding, and whether there are any other bidders. The script continues to collect bids until the user indicates that there are no more bidders.

Once all bids are collected, the script loops through the bids, compares them, and determines the highest bid.

## License:
This project is licensed under the MIT License.
