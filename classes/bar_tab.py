class BarTab:
    def __init__(self, bar_tab_id, total_entry_fee, drink_total):
        self.bar_tab_id = bar_tab_id
        self.total_entry_fee = total_entry_fee
        self.drink_total = drink_total
        self.drinks = []

    def add_drink_to_list(self, drink):
        if drink != None:
            self.drinks.append(drink)

    def remove_drink_from_list(self, drink):
        if len(self.drinks) > 0:
            if self.drinks.__contains__(drink):
                self.drinks.remove(drink)
            else:
                return "Drink is not in list"
        else:
            return "No drinks currently in list to remove"
