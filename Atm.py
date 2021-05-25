class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def cashWithdrawal(self,amount):
        new_amount = 100000 - amount
        print("You Have Withdrawn :" + str(amount) + " Your remaining balance is :"+ str(new_amount))




    def balanceEnquiry(self):
        print("Your Balance is : 100000")
   
def main():
    card_Number = input("Please insert your card number : ")
    pin_Number = input("Please enter your pin number : ")

    new_user = Atm(card_Number,pin_Number)
    print("Choose Your Activity")
    print("1.Balance Enquiry  2.Cash Wothdrawal")

    activity = int(input("Enter activity number :- "))

    if(activity == 1 ):
        new_user.balanceEnquiry()

    elif(activity == 2):
        amount = int(input("Enter amount you want to Withdraw :- "))
        new_user.cashWithdrawal(amount)

    else:
        print("Enter a valid number : ")

if __name__ == "__main__":
    main()

