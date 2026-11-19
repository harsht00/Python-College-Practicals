#use of finally
try:
    print("Processing Transaction")
    amount =int(input())

    if amount > 10000:
        print("Transaction Approved")
except:
    print("Transaction failed")
finally:
    print("Thank you")