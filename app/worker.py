import asyncio 
import json 
import os 
import aio_pika 
from dotenv import load_dotenv 
 
load_dotenv() 
RABBIT_URL = os.getenv("RABBIT_URL") 

async def main(): 
    connection = await aio_pika.connect_robust(RABBIT_URL) 
    async with connection: 
        channel = await connection.channel() 
        await channel.set_qos(prefetch_count=1) 
        queue = await channel.declare_queue("orders_queue", durable=True) 
        print("Waiting for orders...") 