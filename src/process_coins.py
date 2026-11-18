class ProcessCoins:

    def __init__(self):
        self.total_payment = 0

    def process_coins(self):
        """Returns the total from coins inserted"""
        valid_coins = { 25 : "Quarter", 10 : "Dime", 5 : "Nickel", 1 : "Penny"}
        flag = True
        print(f"{valid_coins}")
        for key in valid_coins.keys():
            while flag:
                try:
                    how_many = int(input(f"How many {valid_coins[key]}s do you have? "))
                    self.total_payment += key * how_many
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    flag = True
        return self.total_payment / 100