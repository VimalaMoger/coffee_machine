class CheckResourcesSufficient:

    @staticmethod
    def check_resources_sufficient(ingredients, resources):
        """Returns True when order can be made. False if ingredients are insufficient"""

        if resources['water'] >= ingredients['water']:

            if resources['coffee'] >= ingredients['coffee']:

                if 'milk' in ingredients:

                    if resources['milk'] >= ingredients['milk']:
                        return True
                    else:
                        print("Sorry, there is not enough milk")

                return True

            else:
                print("Sorry there is not enough coffee.")

        else:
            print("Sorry there is not enough water.")

        return False