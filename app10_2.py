from typing import Annotated, Optional

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from fastapi import FastAPI, Request
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation error",
            "details": [
                {
                    "field": err["loc"][-1],
                    "message": err["msg"]
                } 
                for err in exc.errors()
            ]
        }
    )

class User(BaseModel):
    username: str
    age: Annotated[int, Field(gt=18)]
    email: EmailStr
    password: Annotated[str, Field(min_length=8, max_length=16)]
    phone: Optional[str] = "Unknown"

@app.post("/users/")
async def create_user(user: User):
    return user
