class UpdateResources:

    @staticmethod
    def update_resources(ingredients, resources):
        """Update the resources once the order is completed."""
        if resources['water'] >= ingredients['water']:
            if resources['coffee'] >= ingredients['coffee']:
                water = resources['water'] - ingredients['water']
                coffee = resources['coffee'] - ingredients['coffee']
                resources['water']= water
                resources['coffee'] = coffee
                if 'milk' in ingredients:
                    if resources['milk'] >= ingredients['milk']:
                        milk = resources['milk'] - ingredients['milk']
                        resources['milk'] = milk