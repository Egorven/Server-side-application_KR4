from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class ErrorResponse(BaseModel):
    error: str
    status_code: int
    timestamp: str


class DetailedErrorResponse(BaseModel):
    error: str
    status_code: int
    timestamp: str
    details: str | None = None


class CustomExceptionA(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=404, detail="Item not found")


class CustomExceptionB(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=409, detail="Item already exists")


@app.exception_handler(CustomExceptionA)
async def custom_exception_a_handler(request: Request, exc: CustomExceptionA):
    print(f"[ERROR] CustomExceptionA caught: {exc.detail}")
    error_response = ErrorResponse(
        error=exc.detail,
        status_code=exc.status_code,
        timestamp=datetime.now().isoformat()
    )
    return JSONResponse(status_code=exc.status_code, content=error_response.model_dump())


@app.exception_handler(CustomExceptionB)
async def custom_exception_b_handler(request: Request, exc: CustomExceptionB):
    print(f"[ERROR] CustomExceptionB caught: {exc.detail}")
    error_response = ErrorResponse(
        error=exc.detail,
        status_code=exc.status_code,
        timestamp=datetime.now().isoformat()
    )
    return JSONResponse(status_code=exc.status_code, content=error_response.model_dump())

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"[ERROR] Unhandled exception: {str(exc)}")
    error_response = DetailedErrorResponse(
        error="Internal server error",
        status_code=500,
        timestamp=datetime.now().isoformat(),
        details=str(exc)
    )
    return JSONResponse(status_code=500, content=error_response.model_dump())


@app.get("/items/{item_id}/")
async def read_item(item_id: int):
    if item_id == 10:
        raise CustomExceptionA()
    return {"item_id": item_id}


@app.post("/items/{item_id}/")
async def create_item(item_id: int):
    if item_id == 1:
        raise CustomExceptionB()
    return {"message": "Item created", "item_id": item_id}

@app.delete("/items/{item_id}/")
async def delete_item(item_id: int):
    result = 1 / 0
    return {"message": f"Item deleted", "item_id": item_id}