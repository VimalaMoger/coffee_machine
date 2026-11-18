class TransactionSuccessful:

    profit = 0

    def __init__(self, total_payment):
        self.total_payment = total_payment

    def transaction_successful(self, cost, resources):
        """Returns True when payment is accepted. False if money is not sufficient."""
        if self.total_payment < cost:
            print(f"Sorry that's not enough money. Money refunded: ${self.total_payment}")
            return False
        elif self.total_payment > cost:
            change = round(self.total_payment - cost, 2)
            TransactionSuccessful.profit += cost
            resources['Money'] = f"${TransactionSuccessful.profit}"
            print(f"Payment complete! Total inserted: ${self.total_payment}.")
            print(f"${self.total_payment} - ${cost} = ${change}")
            print(f"Here is ${change} dollars in change.")
            return True
        else:
            print(f"Payment complete! Total inserted: {self.total_payment} cents.")
            return  True