from model.addition_model import add_list
import multiprocessing
import time
from datetime import datetime

def perform_multiprocessing(batch_id, payload):
    
    pool = multiprocessing.Pool()
    try:
        results = pool.map(add_list, payload)
        response = format_response(batch_id, results)
        print("Response:", response) 
        return response
    finally:
        pool.close()
        pool.join()

def format_response(batch_id, results):
    
    response = {
        "batchid": batch_id,
        "response": results,
        "status": "complete",
        "started_at": str(datetime.now()),
        "completed_at": str(datetime.now())
    }
    return response
