#!/usr/bin/env python3

# Created by: Mr. Coxall (borrowed by Joseph)
# Created on: Oct 04
# This program calculates total from subtotal and tax of Nova Scotia

# imports constants since there are no constants in python
import constants


def main():
    # this function calculates total from subtotal and tax

    # input, the subtotal from the user
    sub_total = float(input("Enter the subtotal: $ "))

    # process, calculate both the tax and total
    tax = sub_total * constants.HST
    total = sub_total + tax

    # output, the calculated results (tax and total)
    print("")
    print("The HST is ${0:,.2f}, and the total cost is: ${1:,.2f}".format(tax, total))


if __name__ == "__main__":
    main()
