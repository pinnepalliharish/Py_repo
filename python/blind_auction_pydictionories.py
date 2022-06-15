
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bid={}

def bidding_auction(bidding):
    high_bid=0
    high_bidder=""
    for bidder in bidding:
        value=bidding[bidder]
        if value>high_bid:
            high_bid=value
            high_bidder=bidder
    print(f"the highest bidder is {high_bidder} of bid $ {high_bid}")



bidding_done=False
while not bidding_done:
    name=(input("what's your name? "))
    bid_amount=(float(input("what's your bid? ")))
    bid[name]=bid_amount
    option=input("Is there any other bidders left , type yes or no : ")
    if option=="no":
        bidding_done=True
        bidding_auction(bid)
    elif option=="yes":
        print(" type :clear()")


