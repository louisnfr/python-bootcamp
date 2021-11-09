cookbook = {
'sandwich': {'ingredients': {'ham', 'bread', 'cheese', 'tomatoes'}, 'meal': 'lunch', 'prep_time': 10},
'cake': {'ingredients': {'flour', 'sugar', 'eggs'}, 'meal': 'dessert', 'prep_time': 60},
'salad': {'ingredients': {'avocado', 'arugula', 'tomatoes', 'spinach'}, 'meal': 'lunch', 'prep_time': 10},
}


def print_recipe(recipe):
	print("recipe for ", recipe, ':', sep="")
	print("ingredients:", cookbook[recipe]['ingredients'])
	print("to be eaten for", cookbook[recipe]['meal'])
	print("takes", cookbook[recipe]['prep_time'], "minutes to make")

#def add_recipe(name, ingredients, meal, prep_time)

print_recipe("sandwich")

