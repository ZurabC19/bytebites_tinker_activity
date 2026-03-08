# ByteBites backend models
#
# Customer  - represents a registered user; tracks name and purchase history
# FoodItem  - represents a single menu entry; stores name, price, category, and popularity rating
# Menu      - manages the full collection of FoodItems; supports filtering by category
# Order     - groups selected FoodItems into a transaction; computes the total cost

from decimal import Decimal


class FoodItem:
    def __init__(self, name: str, price: Decimal, category: str, popularityRating: float):
        self._name = name
        self._price = price
        self._category = category
        self._popularityRating = popularityRating
    
    def getName(self) -> str:
        return self._name
    
    def getPrice(self) -> Decimal:
        return self._price
    
    def getCategory(self) -> str:
        return self._category
    
    def getPopularityRating(self) -> float:
        return self._popularityRating


class Menu:
    def __init__(self):
        self._items = []
    
    def getItems(self) -> list[FoodItem]:
        return self._items
    
    def filterByCategory(self, category: str) -> list[FoodItem]:
        return [item for item in self._items if item.getCategory() == category]
    
    def addItem(self, item: FoodItem) -> None:
        self._items.append(item)
    
    def sortByPrice(self) -> list[FoodItem]:
        return sorted(self._items, key=lambda item: item.getPrice())
    
    def sortByPopularity(self) -> list[FoodItem]:
        return sorted(self._items, key=lambda item: item.getPopularityRating(), reverse=True)


class Order:
    def __init__(self):
        self._items = []
    
    def getItems(self) -> list[FoodItem]:
        return self._items
    
    def getTotalCost(self) -> Decimal:
        return sum((item.getPrice() for item in self._items), Decimal(0))
    
    def addItem(self, item: FoodItem) -> None:
        self._items.append(item)
    
    def removeItem(self, item: FoodItem) -> None:
        self._items.remove(item)

class Customer:
    def __init__(self, name: str):
        self._name = name
        self._purchaseHistory = []
    
    def getName(self) -> str:
        return self._name
    
    def getPurchaseHistory(self) -> list[Order]:
        return self._purchaseHistory
    
    def addOrder(self, order: Order) -> None:
        self._purchaseHistory.append(order)

if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", Decimal("9.99"), "Mains", 4.5)
    soda = FoodItem("Large Soda", Decimal("2.49"), "Drinks", 3.8)
    dessert = FoodItem("Ice Cream", Decimal("4.99"), "Desserts", 4.9)

    menu = Menu()
    menu.addItem(burger)
    menu.addItem(soda)
    menu.addItem(dessert)

    print([i.getName() for i in menu.sortByPrice()])       # cheapest first
    print([i.getName() for i in menu.sortByPopularity()])  # highest rated first
    print([i.getName() for i in menu.filterByCategory("Drinks")])

    order = Order()
    order.addItem(burger)
    order.addItem(soda)
    print(order.getTotalCost())  # 12.48
