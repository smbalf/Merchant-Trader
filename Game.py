import sys
import pickle
import os
import time
os.system("cls")

"""
Guess we need to create some player files...
Info to include:
  -Player name
  -Company name
  -Current cash value
  -Inventory held
"""


#Defines the bid price calculation
def bid_price(price_change, base=100):
  return round(price_change * base, 3)

#Commodity pid prices
iron_bid = bid_price(1)
tin_bid = bid_price(1.15)
coal_bid = bid_price(0.9)

#Defines the offer price calculation
def offer_price(bid):
  return round(bid + (bid * 0.01), 3)

#Commodity offer prices
iron_offer = offer_price(iron_bid)
tin_offer = offer_price(tin_bid)
coal_offer = offer_price(coal_bid)

#Price list text input
iron = "Iron Ore: " + "   " + str(iron_bid) + "    " + str(iron_offer)
tin = "Tin Ore : " + "   " + str(tin_bid) + "  " + str(tin_offer)
coal = "Coal Ore: " + "   " + str(coal_bid) + "   " + str(coal_offer)

#Commodity price list 
price_list = [iron, 
              tin, 
              coal]

#The commodity display
def comm_display():
  print("")
  print("---------------------------------")
  print("             Bid    Offer")
  for row in price_list:
    print(row)
  print("---------------------------------")
  print("")

#Game Start

print("Welcome to Merchant Trader.")
time.sleep(1)
print("")
input("Press any key to start the game...")
print("")

"""
Need the game start menu here
  - Display player's cash and inventory
  - Press P to see current prices
"""

while True:
  print("Here is a list of current prices:")
  time.sleep(2)
  #Shows the commodity price display
  comm_display()
  time.sleep(2)
  #Player input
  trade = input("Would you like to place a trade? (Y / N)")
  if trade.lower() == "n":
    print("")
    print("You return to the main menu.")
    print("")
    continue
  elif trade.lower() == "y":
      print("")
      break 
#Player decides which commodity to trade
print("Which commodity would you like to trade?")
print("")

"""
Player chooses between Bid and Offer (B/O)
  - Player inputs number they wish to B/O
  - Can't O w/o inventory or can't B w/o cash
print("You have sold " + str(comm_sold) + ".")
or
print("you have bought " + str(comm_bought) + ".")"""