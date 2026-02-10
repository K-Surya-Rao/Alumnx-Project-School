from fastapi import APIRouter
from pydantic import BaseModel

class Twosumrequest(BaseModel):
    nums:list[int]
    target:int

router= APIRouter(
    prefix= "/twosum",
    tags= ["twosum"]
)

@router.post("/")
def twosum(request: Twosumrequest):
    lookup ={}
    for i, n in enumerate(request.nums):
        diff= request.target-n
        if diff in lookup:
            return {"indices" : [lookup[diff],i] }
        lookup [n]=i

    return {"indices":[]}