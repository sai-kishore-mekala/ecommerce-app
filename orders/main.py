from fastapi import FastAPI
from logger import get_logger

app = FastAPI()
logger = get_logger("orders")

@app.post("/orders")
def create_order(order_id: int, user: str):
    try:
        logger.info(f"Order created: {order_id} by {user}")
        return {"status": "success", "order_id": order_id}
    except Exception as e:
        logger.error(f"Order error: {str(e)}")
        return {"status": "error", "message": str(e)}
