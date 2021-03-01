# by Kami Bigdely
# Extract Class

class Food:

    def __init__(self, name, prep_time, is_vegeterian, food_type, 
                 cuisine_type, ingredients, recipe):
        self.name = name
        self.prep_time = prep_time
        self.is_vegeterian = is_vegeterian
        self.food_type = food_type
        self.cuisine_type = cuisine_type
        self.ingredients = ingredients
        self.recipe = recipe

    @classmethod

    def butternut_squash_soup(cls):
        name = 'butternut squash soup'
        prep = 45
        vegeterian = True
        food_type = 'soup'
        cuisine = 'North African'
        ingredients = ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk']
        instructions = ['1. Grill the butter squash, onion, carrot and garlic in the oven until'
          'they get soft and golden on top 2. Put all in blender with'
          'butter and coconut milk. Blend them till they become puree. Then move the content into a pot'
               '. Add coconut milk. Simmer for 5 mintues.']
        return cls(name, prep, vegeterian, food_type, cuisine, ingredients, instructions)
    @classmethod

    def shirazi_salad(cls):
        name = 'shiraz salad'
        prep = 5
        vegeterian = True
        food_type = 'salad'
        cuisine = 'Iranian'
        ingredients = ['cucumber', 'tomato', 'onion', 'lemon juice']
        instructions = ['1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 4. add salt 5. Mixed them thoroughly']
        return cls(name, prep, vegeterian, food_type, cuisine, ingredients, instructions)
    @classmethod

    def beef_sausage(cls):
        name = 'Home-made Beef Sausage'
        prep = 60
        vegeterian = False
        food_type = 'deli'
        cuisine = 'All'
        ingredients = ['sausage casing', 'regular ground beef','garlic', 'corriander seeds','black pepper seeds','fennel seed','paprika']
        instructions = ["1. In a blender, blend corriander seeds, black pepper seeds, fennel seeds and garlic to make, the seasonings 2. In a bowl, mix ground beef with the seasoning 3. Add all the content to a sausage stuffer. Put the casing on the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!"]
        return cls(name, prep, vegeterian, food_type, cuisine, ingredients, instructions)


    def get_recipe(self):
        print("Name: ", self.name)
        print("Prep time: ", self.prep_time, "mins")
        print("Is Veggie?", 'Yes' if True else "No")
        print("Food Type: ", self.food_type)
        print("Cuisine: ", self.cuisine_type)
        print('Ingredients are: ', end='')
        print(', '.join(map(str, self.ingredients)))
        print("recipe ", self.recipe)
        print("***")


"""Refractor Notes:
1. create a class for this for easy reading
2. 
""" 
food1 = Food.butternut_squash_soup()
food1.get_recipe()

food2 = Food.shirazi_salad()
food2.get_recipe()

food3 = Food.beef_sausage()
food3.get_recipe()