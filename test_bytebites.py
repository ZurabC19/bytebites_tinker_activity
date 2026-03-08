from decimal import Decimal
from models import FoodItem, Menu, Order, Customer


def test_order_multiple_items_total_cost():
    """An order with multiple items returns the correct total cost."""
    order = Order()
    item1 = FoodItem("Burger", Decimal("10.00"), "Main", 4.5)
    item2 = FoodItem("Soda", Decimal("2.50"), "Drinks", 4.0)
    item3 = FoodItem("Fries", Decimal("3.00"), "Sides", 4.2)
    
    order.addItem(item1)
    order.addItem(item2)
    order.addItem(item3)
    
    assert order.getTotalCost() == Decimal("15.50")


def test_empty_order_returns_zero_total():
    """An empty order returns a total of Decimal("0")."""
    order = Order()
    
    assert order.getTotalCost() == Decimal("0")


def test_order_remove_item():
    """Removing an item from an order removes it and updates the total cost."""
    order = Order()
    item1 = FoodItem("Burger", Decimal("10.00"), "Main", 4.5)
    item2 = FoodItem("Soda", Decimal("2.50"), "Drinks", 4.0)
    item3 = FoodItem("Fries", Decimal("3.00"), "Sides", 4.2)
    
    order.addItem(item1)
    order.addItem(item2)
    order.addItem(item3)
    
    assert order.getTotalCost() == Decimal("15.50")
    assert len(order.getItems()) == 3
    
    order.removeItem(item2)
    
    assert len(order.getItems()) == 2
    assert item2 not in order.getItems()
    assert order.getTotalCost() == Decimal("13.00")


def test_filter_menu_by_category():
    """Filtering a menu by category returns only items in that category."""
    menu = Menu()
    item1 = FoodItem("Burger", Decimal("10.00"), "Main", 4.5)
    item2 = FoodItem("Soda", Decimal("2.50"), "Drinks", 4.0)
    item3 = FoodItem("Iced Tea", Decimal("2.00"), "Drinks", 4.2)
    
    menu.addItem(item1)
    menu.addItem(item2)
    menu.addItem(item3)
    
    drinks = menu.filterByCategory("Drinks")
    assert len(drinks) == 2
    assert item2 in drinks
    assert item3 in drinks
    assert item1 not in drinks


def test_filter_menu_by_category_no_matches():
    """Filtering by a category with no matches returns an empty list."""
    menu = Menu()
    item1 = FoodItem("Burger", Decimal("10.00"), "Main", 4.5)
    item2 = FoodItem("Soda", Decimal("2.50"), "Drinks", 4.0)
    
    menu.addItem(item1)
    menu.addItem(item2)
    
    desserts = menu.filterByCategory("Desserts")
    assert desserts == []


def test_sort_by_price_ascending():
    """sortByPrice returns items in ascending price order."""
    menu = Menu()
    item1 = FoodItem("Burger", Decimal("10.00"), "Main", 4.5)
    item2 = FoodItem("Soda", Decimal("2.50"), "Drinks", 4.0)
    item3 = FoodItem("Fries", Decimal("3.00"), "Sides", 4.2)
    
    menu.addItem(item1)
    menu.addItem(item2)
    menu.addItem(item3)
    
    sorted_items = menu.sortByPrice()
    assert sorted_items[0] == item2  # $2.50
    assert sorted_items[1] == item3  # $3.00
    assert sorted_items[2] == item1  # $10.00


def test_sort_by_popularity_descending():
    """sortByPopularity returns items in descending popularity order."""
    menu = Menu()
    item1 = FoodItem("Burger", Decimal("10.00"), "Main", 4.5)
    item2 = FoodItem("Soda", Decimal("2.50"), "Drinks", 3.0)
    item3 = FoodItem("Fries", Decimal("3.00"), "Sides", 4.8)
    
    menu.addItem(item1)
    menu.addItem(item2)
    menu.addItem(item3)
    
    sorted_items = menu.sortByPopularity()
    assert sorted_items[0] == item3  # 4.8
    assert sorted_items[1] == item1  # 4.5
    assert sorted_items[2] == item2  # 3.0


def test_customer_purchase_history():
    """A customer's purchase history contains orders that were added."""
    customer = Customer("Alice")
    
    order1 = Order()
    item1 = FoodItem("Burger", Decimal("10.00"), "Main", 4.5)
    order1.addItem(item1)
    
    order2 = Order()
    item2 = FoodItem("Soda", Decimal("2.50"), "Drinks", 4.0)
    order2.addItem(item2)
    
    customer.addOrder(order1)
    customer.addOrder(order2)
    
    history = customer.getPurchaseHistory()
    assert len(history) == 2
    assert order1 in history
    assert order2 in history