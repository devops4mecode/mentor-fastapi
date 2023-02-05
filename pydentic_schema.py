from pydantic import BaseModel

class Items(BaseModel):
    sku: str
    brand_name: str
    title: str
    thumbnail: str
    available_price: str
    mrp: str


def schema_helper(task) -> dict:
    '''
    helper to make the mongo query into dict form
    '''
    return {
        "id": str(task["_id"]),
        "SKU": task["sku"],
        "Brand Name": task["brand_name"],
        "Title": task["title"],
        "Thumbnail":  task["thumbnail"],
        "Available Price":  task["available_price"],
        "MRP":  task["mrp"],
    }
    
