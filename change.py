#!/usr/bin/env python

def calculate_change(cash, cost):
    if cash < cost:
        print("You need more cash! Please enter an amount greater than your total cost")
    else:
        change=cash-cost
        print("Your change is %.02f thank you for shopping at Isaac's" , change)
