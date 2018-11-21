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

#sets the names of the commodities in-game
commodities = ("Iron Ore", "Tin Ore", "Coal Ore")

#Price list text input
iron = commodities[0] + "   " + str(iron_bid) + "    " + str(iron_offer)
tin = commodities[1] + "    " + str(tin_bid) + "  " + str(tin_offer)
coal = commodities[2] + "   " + str(coal_bid) + "   " + str(coal_offer)

#Commodity price list 
price_list = [iron, 
              tin, 
              coal]

#Commodity price display
def comm_display():
  print("Here is a list of current prices: ")
  time.sleep(2)
  print("")
  print("---------------------------------")
  print("             Bid    Offer")
  for row in price_list:
    print(row)
  print("---------------------------------")
  print("")
  time.sleep(2)
  return place_trade()

def place_trade():
  trade = input("Would you like to place a trade? (Y / N)")
  if trade.lower() == "n":
    print("")
    print("You return to the main menu.")
    time.sleep(2)
    print("")
    return game_menu()
  elif trade.lower() == "y":
    print("")
    return game_menu()

  
#Commodity inventory list
inv_list = [commodities[0], 
            commodities[1], 
            commodities[2]]

#Commmodity inventory display
def inventory():
  print(str(company) + "'s Inventory")
  time.sleep(2)
  print("---------------------------------")
  print("Commodity             Quantity")
  print("")
  for row in inv_list:
    print(row)
  print("---------------------------------")
  print("")
  time.sleep(1)
  return game_menu()

#The game initialisation code
def game_start():
  print("")
  input("Press Enter to start...")
  print("")
  time.sleep(1)

#Game welcome
def game_intro():
  print("")
  print("Welcome to Merchant Trader, " + name + ".")
  return game_menu()


#The game main menu
def game_menu():
  print("")
  time.sleep(1)
  print("1. View the current commodities prices")
  print("2. View my current inventory")
  print("")
  menu = input("What would you like to do? ")
  print("")
  if menu == "1":
    return comm_display()
  elif menu == "2":
    return inventory()


#************GAME RUN CODE BEGINS HERE************
game_start()

#Obtain a name for the player
name = input("Please type in your name: ")
time.sleep(1)
print("")

#obtain a name for player's company
company = input("What is the name of your company?: ")
time.sleep(1)

game_menu()

"""
- Add player trading screen
- Player chooses between Bid and Offer [B/O]
- Player inputs quantity they wish to [B/O]
- Can't [O] w/o inventory or can't [B] w/o cash
- print("You have sold " + str(comm_sold) + ".")
  or print("you have bought " + str(comm_bought) + ".")
- save values to player's inventory // player saving in general
"""