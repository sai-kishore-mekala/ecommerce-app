from fastapi import FastAPI
from logger import get_logger

app = FastAPI()
logger = get_logger("payments")

@app.post("/pay")
def process_payment(amount: float, user: str):
    if amount <= 0:
        logger.error("Payment failed: amount invalid")
        return {"status": "error", "message": "Invalid amount"}

    logger.info(f"Payment processed: {amount} by {user}")
    return {"status": "success", "amount": amount}
