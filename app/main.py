from fastapi import FastAPI 
from pydantic import BaseModel
import os 
import aio_pika 
from dotenv import load_dotenv  

app = FastAPI(title="RabbitMQ Lab 7") 

load_dotenv()
RABBIT_URL = os.getenv("RABBIT_URL")

class OrderRequest(BaseModel): 
    order_id: int 
    product: str 
    quantity: int 

@app.post("/orders", status_code=200) 
async def submit_order(order: OrderRequest): 
    connection = await aio_pika.connect_robust(RABBIT_URL) 
    async with connection: 
        channel = await connection.channel(publisher_confirms=True) 
        queue = await channel.declare_queue("orders_queue", durable=True) 

    ##return {"status": "received", "order_id": order.order_id} 