classDiagram
    class Customer {
        -name: String
        -purchaseHistory: List~Order~
        +getName() String
        +getPurchaseHistory() List~Order~
        +addOrder(order: Order) void
    }
    class Order {
        -items: List~FoodItem~
        +getItems() List~FoodItem~
        +getTotalCost() Decimal
        +addItem(item: FoodItem) void
        +removeItem(item: FoodItem) void
    }
    class Menu {
        -items: List~FoodItem~
        +getItems() List~FoodItem~
        +filterByCategory(category: String) List~FoodItem~
        +addItem(item: FoodItem) void
    }
    class FoodItem {
        -name: String
        -price: Decimal
        -category: String
        -popularityRating: Float
        +getName() String
        +getPrice() Decimal
        +getCategory() String
        +getPopularityRating() Float
    }
    Customer "1" --> "*" Order : places
    Order "*" --> "*" FoodItem : contains
    Menu "1" --> "*" FoodItem : manages