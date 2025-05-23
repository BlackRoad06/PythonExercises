class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "Menu: {name}, Available Time: {start_time}AM - {end_time}PM.".format(name = self.name, start_time = self.start_time, end_time = self.end_time)
  
  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      if item in self.items:
        total_price += self.items[item]
    return total_price





brunch = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}


brunch1 = Menu("Brunch", brunch, 11, 16)

order1 = ["pancakes", "home fries", "coffee"]


early_bird1 = Menu("Early Bird", early_bird, 15, 18)

early_bird_order = ["salumeria plate", "mushroom ravioli (vegan)"]




class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu


dinner1 = Menu("Dinner", dinner, 17, 23)
kids1 = Menu("Kids", kids, 11, 21)

flagship_store = Franchise("1232 West End Road", [brunch1, early_bird1, dinner1, kids1])

new_installment = Franchise("12 East Mulberry Street", [brunch1, early_bird1, dinner1, kids1])


print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))



class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Take a’ Arepa", arepas_items, 10, 20)

basta_business = Business("Basta Fazoolin' with my Heart",[flagship_store, new_installment])


arepas_place = Franchise("123 Fitzegard Avenue", [arepas_menu])


business = Business("Take a' Arepa", [arepas_place])

print(business.name)
print(business.franchises[0])
print(business.franchises[0].menus)
print(business.franchises[0].address)

print(basta_business.name)
print(basta_business.franchises[0])
print(basta_business.franchises[1])
print(basta_business.franchises[0].menus)
print(basta_business.franchises[1].menus)