from coffee_maker import CoffeeMaker
from coffee_model import CoffeeModel
from utils.coffee_machine_logo import logo
from report import Report
from utils.ingredients_menu import MENU, resources
import sys

def coffee_machine_app():

    user_input = input("What would you like? (espresso/latte/cappuccino): or type 'off' to stop ")
    if user_input == 'off':
        sys.exit(0)
    if user_input in ['espresso', 'latte', 'cappuccino']:
        coffee_style = CoffeeModel(MENU, resources)
        coffee_maker = CoffeeMaker(coffee_style)
        coffee_maker.make_coffee(user_input)
    else:
        coffee_machine_app()

    show_report = input("Would you want to see report? type 'report' ")
    if show_report == 'report':
        print(Report.get_report(resources))
    coffee_machine_app()

if __name__ == '__main__':
    print(logo)
    coffee_machine_app()