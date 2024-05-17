# FastAPI Addition Service

This project is a simple FastAPI-based web service that performs addition on lists of integers. The service accepts a JSON payload containing a batch ID and a list of integer lists, and returns the sum of each list.

## Features

- FastAPI for creating the web service.
- Multiprocessing for handling multiple addition operations concurrently.
- Pydantic for request and response validation.
- Logging for debugging and monitoring.
- Unit tests using `unittest`.

## Project Structure

│
├── controller/
│ └── addition_controller.py
│
├── model/
│ └── addition_model.py
│
├── tests/
│ └── test_main.py
│
├── main.py
