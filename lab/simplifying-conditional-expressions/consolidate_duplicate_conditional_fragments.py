# by Kami Bigdely
# Consolidate duplicate conditional fragments
def add(mix, something):
    mix.append(something)
    return mix

def mixer_ice_with_cream():
    print('mixed ice with cream.')
    return ['ice', 'cream']

def make_drink(drink, addons):
    if 'coffee' in drink:
        mix = ['coffee']
        mix = add(mix, addons)
        # mix = add(mix, addons)
    if 'strawberry milkshake' in drink:
        mix = ['strawberry']
        mix = mixer_ice_with_cream() + add(mix, addons)
        # mix = add(mix, 'strawberry')
        # mix = add(mix, addons)
    return mix

final_drink = make_drink('strawberry milkshake', ['milk','sugar'])
print(final_drink)

coffee_drink = make_drink('coffee', ['whipped cream', 'caramel'])
print(coffee_drink)
