class account:
    custid = 0
    giftcard_no = 0
    trans_no = 0
    def __init__(self,name,depAmt):
        account.custid += 1
        self.custName = 'anu'
        self.custid = account.custid 
        self.depAmt = depAmt
        self.balance = depAmt
        self.giftcard_list = []
        self.trans_list = []
    def create_giftcard(self,amt,pin):
        account.giftcard_no+=1
        self.giftcard_no = account.giftcard_no
        self.giftcard_bal = amt
        self.giftcard_pin = pin
        self.giftcard_list.append([self.giftcard_no,self.giftcard_pin,self.giftcard_bal,"Active"])
        self.balance -= amt
        return self.giftcard_no
    def giftcard_topup(self,cardno,amt):
        self.giftcard_bal += amt
        for card in self.giftcard_list:
            if(card[0] == cardno):
                card[2]+=amt
                break
        self.balance -= amt
    def giftcard_close(self,cardno,pin):
        for card in self.giftcard_list:
            if(card[0] == cardno):
                if(card[1] == pin):
                    self.balance += card[2]
                    card[2] = 0
                    card[3] = "Closed"
                    print("Your Gift Card is closed successfully!!")
                    return
                else:
                    print("Wrong Pin Entered!")
                    print("Try Again")
                    return
    def purchase_item(self,cardno,amt,pin):
        for card in self.giftcard_list:
            if(card[0] == cardno):
                if(pin != card[1]):
                    print("Wrong pin, try again!")
                    return
                elif(amt>card[2]):
                    print("Not enough balance, please topup and try again!")
                    return
                else:
                    card[2]-=amt
                    account.trans_no+=1
                    self.trans_list.append([account.trans_no,card[0],amt])
                    print("Purchase is Successful!!")
                    return
custList = []
def account_summary():
    print("-------------------------------------------------------------------")
    print("custID \t Balance")
    print("-------------------------------------------------------------------")
    for i in range(len(custList)):
        print(custList[i].custid,"\t",custList[i].balance)
        print("-------------------------------------------------------------------")
def create_account():
    print("Name : ",end = "")
    name = input()
    print("Deposit Amt : ",end = "")
    depAmt = int(input())
    custList.append(account(name,depAmt))
    print("Your account has been created successfully!!")
    print("Your CUSTOMER ID is ",custList[-1].custid)
    print("Account Summary:")
    account_summary()
def giftcard_creation():
    print("Let's create a gift card for you!!")
    print("Enter your customer ID : ",end = "")
    custid = int(input())
    print("Enter the gift card ammount : ",end = "")
    amt = int(input())
    for cust in custList:
        if(cust.custid == custid):
            if(amt > cust.balance):
                print("Sorry, your account does not have enough balance!")
                return
            else:
                print("Set up a four digit pin for ur gift card : ",end = "")
                pin = int(input())
                cardno = cust.create_giftcard(amt,pin)
                print("Your GIFT CARD NUMBER is : ",cardno)
            break
    print("Gift Card Summary:")
    giftcard_summary()
    print("Account Summary:")
    account_summary()
def giftcard_summary():
    print("----------------------------------------------------------------------------")
    print("Card No","\t","Cust Id","\t","PIN",'\t',"Gift Card Balance","\t","Status")
    print("----------------------------------------------------------------------------")
    for cust in custList:
        if(cust.giftcard_list):
            for card in cust.giftcard_list:
                print(card[0],"\t\t",cust.custid,"\t\t",card[1],"\t\t",card[2],"\t\t",card[3])
                print("-------------------------------------------------------------------")
def giftcard_topup():
    print("Gift Card top up!")
    print("Enter your CUSTOMER ID : ",end="")
    custid = int(input())
    print("Enter your CARD NO : ",end="")
    cardno = int(input())
    print("Enter the top up amount : ",end = "")
    amt = int(input())
    for cust in custList:
        if(cust.custid == custid):
            if(amt>cust.balance):
                print("Sorry, your account does not have enough balance!")
                return
            else:
                if (not cust.giftcard_list):
                    print("You don't have any gift cards")
                    print("Create one now...")
                    return
                else:
                    for card in cust.giftcard_list:
                        if(card[0] == cardno and card[-1] == "Inactive" ):
                            print("Your don't have an active giftcard on the given card number")
                            break
                        else:
                            cust.giftcard_topup(cardno,amt)
                            break
            break
    print("Gift Card Summary:")
    giftcard_summary()
    print("Account Summary:")
    account_summary() 
def giftcard_close():
    print("To Close Gift Card:")
    print("Enter your CUSTOMER ID : ",end="")
    custid = int(input())
    print("Enter your GIFT CARD NO : ",end="")
    cardno = int(input())
    print("Enter your PIN : ",end="")
    pin = int(input())
    for cust in custList:
        if(cust.custid == custid):
            cust.giftcard_close(cardno,pin)
            break
    print("Gift Card Summary:")
    giftcard_summary()
    print("Account Summary:")
    account_summary()
def transaction_summary():
    print("-------------------------------------------------------------------")
    print("Txn No","\t","Card No","\t","Amount")
    print("-------------------------------------------------------------------")
    for cust in custList:
        if(cust.trans_list):
            for trans in cust.trans_list:
                print(trans[0],"\t",trans[1],"\t\t",trans[2])
                print("-------------------------------------------------------------------")
def purchase_item():
    print("To purchase your favourite!!")
    print("Enter your CUSTOMER ID : ",end="")
    custid = int(input())
    print("Enter your GIFT CARD NO : ",end="")
    cardno = int(input())
    print("Enter the amount : ",end="")
    amt = int(input())
    print("Enter your PIN : ",end="")
    pin = int(input())
    for cust in custList:
        if(cust.custid == custid):
            cust.purchase_item(cardno,amt,pin)
            break
    print("Gift Card Summary:")
    giftcard_summary()
    print("Transaction Summary:")
    transaction_summary()


print("Hi, Welcome to XYZ Bank!!")

cont = 'y'
while(cont == 'y' or cont == 'Y'):
    print("-------------------------------------------------------------------")
    print("What do you like to do today?")
    print("1.Create Account")
    print("2.Create Gift Card")
    print("3.Top Up Gift Card")
    print("4.Close Gift Card")
    print("5.Purchase Item")
    print("6.EXIT")
    print("-------------------------------------------------------------------")
    print("Type your Option : ",end="")
    option = int(input())
    print("-------------------------------------------------------------------")
    if(option == 1):
        create_account()
    elif(option == 2):
        giftcard_creation()
    elif(option == 3):
        giftcard_topup()
    elif(option == 4):
        giftcard_close()
    elif(option == 5):
        purchase_item()
    else:
        print("Exiting Services!!")
        cont = 'n'
    if(option!=6):
        print("Do you want to continue?? y/n :")
        cont = input()