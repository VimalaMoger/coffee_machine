from check_resources_sufficient import CheckResourcesSufficient
from transaction_successfull import TransactionSuccessful
from update_resources import UpdateResources
from src.process_coins import ProcessCoins

class CoffeeMaker:
    def __init__(self, coffee_style):
        self.coffee_style_menu = coffee_style.menu
        self.resources = coffee_style.resources

    def make_coffee(self, user_input):
        ingredients = self.coffee_style_menu[user_input]['ingredients']
        cost = self.coffee_style_menu[user_input]['cost']
        resources = self.resources
        if CheckResourcesSufficient.check_resources_sufficient(ingredients, resources):
            if TransactionSuccessful(ProcessCoins().process_coins()).transaction_successful(cost, resources):
                UpdateResources.update_resources(ingredients, resources)
                print(f"☕Here is your {user_input}. Enjoy!")


