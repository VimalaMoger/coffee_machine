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
                    coin_in_cents =  int(input(f"Please insert ({valid_coins[key]} in cents): "))
                    if key == coin_in_cents:
                        how_many = int(input(f"How many {valid_coins[key]}s do you have? "))
                        self.total_payment += coin_in_cents * how_many
                        break
                    else:
                        print(f"Invalid coin denomination. Please insert {key}.")
                        flag = True
                except ValueError:
                    print("Please enter a valid number.")
                    flag = True
        return self.total_payment / 100