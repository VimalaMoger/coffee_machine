class ProcessCoins:

    def __init__(self):
        self.total_payment = 0

    def process_coins(self):
        """Returns the total from coins inserted"""

        valid_coins = { "Quarter" : 25, "Dime" : 10, "Nickel" : 5, "Penny" : 1}
        flag = True
        print(f"{valid_coins}")
        for key in valid_coins.keys():
            while flag:
                try:
                    how_many = int(input(f"How many {key}s do you have? "))
                    self.total_payment += valid_coins[key] * how_many
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    flag = True
        return self.total_payment / 100