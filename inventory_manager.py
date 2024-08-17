import os

class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}, Price: ${self.price:.2f}"

class Inventory:
    def __init__(self, filename="inventory.txt"):
        self.filename = filename
        self.items = self.load_inventory()
    
    def load_inventory(self):
        if not os.path.exists(self.filename):
            return []
        
        items = []
        with open(self.filename, 'r') as file:
            for line in file:
                name, quantity, price = line.strip().split(',')
                items.append(InventoryItem(name, int(quantity), float(price)))
        return items
    
    def save_inventory(self):
        with open(self.filename, 'w') as file:
            for item in self.items:
                file.write(f"{item.name},{item.quantity},{item.price}\n")
    
    def add_item(self, name, quantity, price):
        for item in self.items:
            if item.name == name:
                item.quantity += quantity
                return
        self.items.append(InventoryItem(name, quantity, price))
    
    def remove_item(self, name, quantity):
        for item in self.items:
            if item.name == name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    if item.quantity == 0:
                        self.items.remove(item)
                    return True
                else:
                    print(f"Error: Not enough quantity to remove. Current stock: {item.quantity}")
                    return False
        print(f"Error: Item '{name}' not found in inventory.")
        return False
    
    def list_items(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for item in self.items:
                print(item)

def main():
    inventory = Inventory()
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. List Items")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory.add_item(name, quantity, price)
            inventory.save_inventory()
            print(f"Added {quantity} of {name} to the inventory.")
        
        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            if inventory.remove_item(name, quantity):
                inventory.save_inventory()
                print(f"Removed {quantity} of {name} from the inventory.")
        
        elif choice == '3':
            print("\nCurrent Inventory:")
            inventory.list_items()
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
