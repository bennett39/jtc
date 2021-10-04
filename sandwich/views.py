import random
from django.shortcuts import render
from django.http import Http404


MEATS = ['ham', 'turkey']
CHEESES = ['provolone', 'cheddar']
TOPPINGS = ['pickles', 'mayo']


def random(request):
    meat = random.choice(MEATS)
    cheese = random.choice(CHEESES)
    topping = random.choice(TOPPINGS)

    return render(request, 'sandwich/random.html', context={'meat': meat, 'cheese': cheese, 'topping': topping})

def list_ingredient(request, ingredient):
    ingredients = {
        'meats': MEATS,
        'cheeses': CHEESES,
        'toppings': TOPPINGS,
    }
    if ingredient not in ingredients:
        return Http404(f'No such ingredient: {ingredient}')

    return render(request, 'sandwich/ingredients.html', context={'ingredients': ingredients[ingredient]})
