
def validate_ingredients(ingredients: str) -> str:
    valid_elements = {"fire", "water", "earth", "air"}
    ingredients_list = ingredients.split()

    all_valid = True
    for ing in ingredients_list:
        if ing not in valid_elements:
            all_valid = False
            break

    if all_valid:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
