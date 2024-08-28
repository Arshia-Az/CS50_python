def main():
    item = input("item: ")
    check_calories = check_nutrition(item)
    if check_calories is None:
        return ""
    else:
        return print(f"calories :{check_calories}")


def check_nutrition(item):
    calories_list = {
        # fruits
        'apple': 130, 'Avocado': 50, 'Sweet Cherries': 100, 'Banana': 110,
        'Cantalope': 50, 'Grapefruit': 60, 'Honeydew Melon': 90,
        'Kiwifruit': 90, 'Sweet Cherries': 100, 'Tangerine': 50,
        'Watermelon': 80,
        # vegetables
        'Asparagus': 20, 'Bell Pepper': 25, 'Broccoli': 45, 'Carrot': 30,
        'Cucumber': 25, "tomato": 25,
        "Blue Crab": 100, "Catfish": 130, "Cod": 90, "Haddock": 100,
        "Halibut": 120, "Lobster": 80, "Ocean Perch": 110, "Orange Roughy": 80,
        "Pollock": 90,"pear":100,
    }
    if item in calories_list:
        calory = calories_list.get(item)
        return calory
if __name__ == "__main__":
    main()
