class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name: str, cuisine: str, menu: dict, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish, quantity):
        if dish not in self.menu:
            return "Dish not available"

        dish_info = self.menu[dish]
        available_quantity = dish_info.get('quantity', 0)
        price = dish_info.get('price', 0)

        if quantity > available_quantity:
            return "Requested quantity not available"

        total_cost = price * quantity
        available_quantity -= quantity
        dish_info['quantity'] = available_quantity
        return total_cost
