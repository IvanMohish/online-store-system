from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 25000},
    {"id": 2, "name": "Mouse", "price": 800},
]


@app.get("/products")
def get_products():
    return {
        "student_id": "IvanMohish",
        "products": products
    }


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {"error": "Product not found"}