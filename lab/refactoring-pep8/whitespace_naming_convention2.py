# By Kami Bigdely
# PEP8 - whitespaces and variable names.

class Pizza:

    def __init__(self, mybread_type, cheese_type, 
                meat_type, pizza_toppings, size):
        self.bread_type= mybread_type
        self.cheese_type = cheese_type
        self.meat_type= meat_type
        self.toppings = pizza_toppings
        self.size = size        
    @classmethod
    
    def create_chicago_pizza(class_type, size):
        bread = 'Deep-dish bread'
        cheese = 'Mozzarella cheese'
        meat_type= 'Italian sausage'
        toppings = ['green bell pepper','mushroom', 
                    'chunky tomato sauce', 'onion']
        return class_type (bread, cheese, meat_type, toppings, size)    
    @classmethod

    def create_california_pizza(class_type, meat_type, size):
        bread = 'Thin crust'
        cheese = 'Feta cheese'
        toppings =['garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper']
        return class_type(bread, cheese, meat_type, toppings, size)

    def print_info(self):
        print('Bread type is: ', self.bread_type)
        print('Cheese type is: ', self.cheese_type)
        print('Meat type is: ', self.meat_type)
        print('Toppings are: ', end='')
        print(', '.join(map(str, self.toppings)))

    
# my_pizza = Pizza.create_chicago_pizza('chicken')
my_pizza = Pizza.create_california_pizza('chicken', 'large')
my_pizza.print_info()