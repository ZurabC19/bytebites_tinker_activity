# ByteBites backend models
#
# Customer  - represents a registered user; tracks name and purchase history
# FoodItem  - represents a single menu entry; stores name, price, category, and popularity rating
# Menu      - manages the full collection of FoodItems; supports filtering by category
# Order     - groups selected FoodItems into a transaction; computes the total cost


class FoodItem:
    def __init__(self, name, price, category, popularityRating):
        self._name = name
        self._price = price
        self._category = category
        self._popularityRating = popularityRating
    
    def getName(self):
        pass
    
    def getPrice(self):
        pass
    
    def getCategory(self):
        pass
    
    def getPopularityRating(self):
        pass


class Menu:
    def __init__(self):
        self._items = []
    
    def getItems(self):
        pass
    
    def filterByCategory(self, category):
        pass
    
    def addItem(self, item):
        pass


class Order:
    def __init__(self):
        self._items = []
    
    def getItems(self):
        pass
    
    def getTotalCost(self):
        pass
    
    def addItem(self, item):
        pass
    
    def removeItem(self, item):
        pass


class Customer:
    def __init__(self, name):
        self._name = name
        self._purchaseHistory = []
    
    def getName(self):
        pass
    
    def getPurchaseHistory(self):
        pass
    
    def addOrder(self, order):
        pass

