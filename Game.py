#Started 19th November 2018 by Sam Balf
#Python "Trading Tycoon" game inspired by Ocean Trader developed by Software 2000
#version_1 completed: 

import sys
import pickle
import os
import time
os.system("cls")

class Player:
  def __init__(self, name, company, balance=100000, inventory=0):
    self.name = name
    self.company = company 
    self.balance = balance
    self.inventory = inventory  

  def player_info(self):
    print(self.company + "'s Corporate Sheet")
    print("--------------------------------")
    print("Current balance: $" + str(self.balance))
    print("Current inventory: " + str(self.inventory))
    print("--------------------------------")
    #p.player_info() <- OUTPUT


#sets the names of the commodities in-game
commodities = ("Iron Ore", "Tin Ore", "Coal Ore")

#Defines the bid price calculation (rounding = 3)
def bid_price(price_change, base=100):
  return round(price_change * base, 3)

#Defines the offer price calculation (rounding = 3)
def offer_price(bid_price):
  return round(bid_price + (bid_price * 0.01), 3)

#Commodity bid prices
iron_bid = bid_price(1)
tin_bid = bid_price(1.15)
coal_bid = bid_price(0.9)

#Commodity offer prices
iron_offer = offer_price(iron_bid)
tin_offer = offer_price(tin_bid)
coal_offer = offer_price(coal_bid)

#Price list text input
iron = commodities[0] + "     " + str(iron_bid) + "      " + str(iron_offer)
tin = commodities[1] + "      " + str(tin_bid) + "    " + str(tin_offer)
coal = commodities[2] + "     " + str(coal_bid) + "     " + str(coal_offer)

#Commodity price list 
price_list = [iron, 
              tin, 
              coal]

#Commodity price display
def comm_display():
  print("Here is a list of current prices: \n")
  time.sleep(2)
  print("---------------------------------")
  print("             Bid      Offer")
  for row in price_list:
    print(row)
  print("---------------------------------\n")
  time.sleep(2)
  return place_trade()

def place_trade():
  trade = input("Would you like to place a trade? (Y / N)")
  if trade.lower() == "n":
    print("\nYou return to the main menu.\n")
    time.sleep(2)
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
  print("Commodity             Quantity\n")
  for row in inv_list:
    print(row)
  print("---------------------------------\n")
  time.sleep(1)
  return game_menu()

#The game initialisation code
def game_start():
  input("\nPress Enter to start...\n")

#Game welcome
def game_intro():
  print("\nWelcome to Merchant Trader, " + name + ".")
  return game_menu()

#The game main menu
def game_menu():
  time.sleep(1)
  print("\n1. View the current commodities prices")
  print("2. View my company balance and inventory\n")
  menu = input("What would you like to do?\n ")
  if menu == "1":
    return comm_display()
  elif menu == "2":
    return inventory()


#************GAME RUNS BEGINS HERE************
#Screen.wrapper(merchant_trader)
game_start()

name = input("What is your name?  \n")
company = input("What is your company name?\n"  )
p = Player(name, company)

game_intro()
