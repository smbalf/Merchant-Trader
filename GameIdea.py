"""
Commodity Trading Game
----------------------
Inspired by Ocean Trader by Software 2000

Merchant Trader

Requirements:
*Player has to purchase commodity
*Player has to hire transport
*Player has to sell commodity 

Design:
  
  Data:
    Modes:
      *Different modes for game start

    Commodities:
      *Types
      *Price  (at location)
      *Supply (at location)
      *Demand (at location)

    End-Users:
      *Types
      *Purchase price (per user)
      *Demand level
      *Growth (can be negative)
      *Growth/Demand

    Transport:
      *Price  (at location)
      *Supply (at location)
      *Demand (at location)

    Locations:
      *Names
      *Favourite product
      *Growth (can be negative)
      *Growth/Demand ratio

  Functions:
    Simulation:
      *Determine price formula
      *Determine starting Supply and Demand

    Capture Input:
      *Name of company
      *Starting city
      *Choices
"""
