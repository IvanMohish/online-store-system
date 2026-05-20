from fastapi import FastAPI
import requests

app = FastAPI()

orders = []


@app.post("/orders")
def create_order(product_id: int, quantity: int):

    response = requests.get(
        f"http://product_service:8001/products/{product_id}"
    )

    product = response.json()

    if "error" in product:
        return {"error": "Product not found"}

    order = {
        "product": product,
        "quantity": quantity
    }

    orders.append(order)

    return {
        "message": "Order created",
        "order": order
    }


@app.get("/orders")
def get_orders():
    return {
        "student_id": "IvanMohish",
        "orders": orders
    }