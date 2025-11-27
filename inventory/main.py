from fastapi import FastAPI
from logger import get_logger

app = FastAPI()
logger = get_logger("inventory")

@app.get("/inventory/{item_id}")
def check_inventory(item_id: int):
    if item_id == 0:
        logger.error("Inventory check failed: invalid item ID")
        return {"status": "error", "message": "Invalid item"}
    
    logger.info(f"Inventory OK for item {item_id}")
    return {"status": "success", "item_id": item_id}
