import time

#defines the bid price calculation
def bid_price(price_change, base=100):
  return round(price_change * base, 3)

#commodity pid prices
iron_bid = bid_price(1)
tin_bid = bid_price(1.15)
coal_bid = bid_price(0.9)

#defines the offer price calculation
def offer_price(bid):
  return round(bid + (bid * 0.01), 3)

#commodity offer prices
iron_offer = offer_price(iron_bid)
tin_offer = offer_price(tin_bid)
coal_offer = offer_price(coal_bid)

#price list text input
iron = "Iron Ore: " + "   " + str(iron_bid) + "    " + str(iron_offer)
tin = "Tin Ore : " + "   " + str(tin_bid) + "  " + str(tin_offer)
coal = "Coal Ore: " + "   " + str(coal_bid) + "   " + str(coal_offer)

#commodity price list 
price_list = [iron, 
              tin, 
              coal]

#the commodity display
def comm_display():
  print("")
  print("---------------------------------")
  print("             Bid    Offer")
  for row in price_list:
    print(row)
  print("---------------------------------")
  print("")

#GameStart

print("Welcome to Merchant Trader.")
time.sleep(1)
print("")
input("Press any key to start the game...")
print("")
#need some kinda menu here
while True:
  print("Here is a list of today's prices:")
  time.sleep(2)
  #shows the commodity price display
  comm_display()
  time.sleep(3)
  #player input
  trade = input("Would you like to place a trade? (Y / N)")
  if trade.lower() == "n":
    print("")
    print("You return to the main menu.")
    print("")
    continue
  elif trade.lower() == "y":
      print("")
      break 
#player decides which commodity to trade
print("Which commodity would you like to trade?")
print("")
print("")
#player decides bid or offer
#player can't offer w/o having stock or purchase more than can afford
#print("you have bought " + commodity bought + ".")