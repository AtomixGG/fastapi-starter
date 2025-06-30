from pydantic import BaseModel
# Step 3: Define the Pydantic model

class ItemBase(BaseModel):
    title: str
    description: str
    price: float

class ItemCreated(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    class Config:
        from_attributes = True