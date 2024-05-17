from fastapi import FastAPI, HTTPException
from typing import List, Union
from datetime import datetime
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

class AdditionRequest(BaseModel):
    batchid: str
    payload: List[List[Union[int, float]]]


class AdditionResponse(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: str
    completed_at: str

def add_list(numbers):

    result = sum(numbers)
    return result


@app.post("/addition/")
async def addition(request: AdditionRequest):
    try:
        logging.debug(f"Received request: {request}")
        results = [add_list(sublist) for sublist in request.payload]
        response = AdditionResponse(
            batchid=request.batchid,
            response=results,
            status="complete",
            started_at=str(datetime.now()),
            completed_at=str(datetime.now())
        )
        logging.debug(f"Sending response: {response}")
        return response
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))
