class Item:
    def calculate_total_price(self,a,b):
        return a*b
    
item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quintity = 5

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quintity = 2

print(item1.calculate_total_price(item1.price,item1.quintity))

print(type(item1))