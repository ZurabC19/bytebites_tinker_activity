classDiagram
    class Customer {
        -name: String
        -purchaseHistory: Order[]
        +addOrder(order: Order): void
        +getPurchaseHistory(): Order[]
        +getName(): String
    }

    class FoodItem {
        -name: String
        -price: Decimal
        -category: String
        -popularityRating: Float
        +getName(): String
        +getPrice(): Decimal
        +getCategory(): String
        +getPopularityRating(): Float
    }

    class Menu {
        -items: FoodItem[]
        +addItem(item: FoodItem): void
        +removeItem(item: FoodItem): void
        +getItems(): FoodItem[]
        +filterByCategory(category: String): FoodItem[]
    }

    class Order {
        -customer: Customer
        -items: FoodItem[]
        -orderDate: Date
        +addItem(item: FoodItem): void
        +removeItem(item: FoodItem): void
        +getItems(): FoodItem[]
        +getTotalCost(): Decimal
        +getCustomer(): Customer
    }

    Customer "1" --> "*" Order : places
    Order "*" --> "*" FoodItem : contains
    Menu "1" --> "*" FoodItem : manages