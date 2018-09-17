#Erin Smith
#Dictionaary Project 9/17/18

cakes = []
cupcakes = []
pastries = []
def first(shape,size,flavor):
    cakes = {
        'shape' : shape,
        'size' : size,
        'flavor' : flavor
        }
    cakes.append(cakes)
    return "Your order %s has been placed" % cakes

def second(size,flavor,frosting):
    cupcakes = {
        'size' : size,
        'flavor' : flavor,
        'frosting' : frosting
        }
    cupcakes.append(cupcakes)
    return "Your order %s has been placed" % cupcakes

def third(name,flavor,topping):
    pastry = {
        'name' : name,
        'flavor' : flavor,
        'topping' : topping
        }
    pastries.append(pastry)
    return "Your order 5s has been placed" % pastry
#Make the user have more than one order(so loop an if cmd for orders)
#add all total orders to a seperate list
