products = [
    {
        "id": 1,
        "name": "IPHONE 13",
        "category": "Electronics",
        "price": 2500,
        "colors": ["gray", "black"],
        "size": ["small", "medium", "large"],
        "stock": [
            {"gray-small": 25, "gray-medium": 30, "gray-large": 34},
            {"black-small": 23, "black-medium": 23, "black-large": 25}
        ],
    },
    {
        "id": 2,
        "name": "IPHONE 15",
        "category": "Electronics",
        "price": 2500,
        "colors": ["gray", "black"],
        "size": ["small", "medium", "large"],
        "stock": [
            {"gray-small": 25, "gray-medium": 30, "gray-large": 34},
            {"black-small": 23, "black-medium": 23, "black-large": 25}
        ],
    },
    {
        "id": 3,
        "name": "IPHONE 16",
        "category": "Electronics",
        "price": 2500,
        "colors": ["gray", "black"],
        "size": ["small", "medium", "large"],
        "stock": [
            {"gray-small": 25, "gray-medium": 30, "gray-large": 34},
            {"black-small": 23, "black-medium": 23, "black-large": 25}
        ],
    }
]


products[2]["name"] = "IPHONE 16 PROMAX"

# Access stock of products[2]
print("Accessing stock of Product 3 (IPHONE 16 PROMAX):")
print(products[2]["stock"]) 
print("")

# Access index 3 of stock for products[2] 
print("Accessing index 0 of stock in Product 3:")
print(products[2]["stock"][0])  
print("")

# Change the quantity of "black-small" for products[2]
print("Updated stock for Product 3:")
print(products[2]["stock"])

# Changing the quantity of "black-small"
black_small_index = 1
products[2]["stock"][black_small_index]["black-small"] = 20
print("Stock updated successfully:")
print(products[2]["stock"])  # Print the updated stock list