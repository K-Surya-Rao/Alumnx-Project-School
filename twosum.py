from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import uvicorn


#initialize fastAPI app
app = FastAPI(
    title = "TwoSum",
    description= "End point to Solve Two Sum DSA Problem"

)


#request model

class TwoSumRequest(BaseModel):
    nums:List[int]=Field(
        description= "Array of integers",
        example = [2,7,11,15]
    )
    target: int =Field(
        description = "Target Sum",
        example =9
    )

#response model
class TwoSumResponse(BaseModel):
    indices: Optional [List[int]]=Field (None, description ="indices of two numbers")
    values: Optional [List[int]]= Field (None, description="values at those indices")
    found : bool =Field(description="whether solution was found")
    message: str =Field(description="result message")
    algorithm: str =Field(default="Hash Map 0(n)", description="Algorithm used")

#algo implementation
def solve_two_sum (nums: List[int], target:int)->Optional [List[int]]:
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target-num
        if complement in hash_map:
            return [hash_map[complement], i]
        
        hash_map[num]=i

    return None


#API endpoints

@app.get("/")
def home():
    return {
         "message": "Two Sum API - Solve DSA problems via REST",
         "endpoints": {
            "POST /two-sum": "Solve Two Sum problem",
            "GET /health": "Health check"
        },
        "example": {
            "request": {
                "nums": [2, 7, 11, 15],
                "target": 9
            },
            "response": {
                "indices": [0, 1],
                "values": [2, 7],
                "found": True
            }
        }
    }

@app.get("/")
def home():
    return {"message": "Two Sum API running"}

@app.head("/")
def head_root():
    return

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.head("/health")
def health_head():
    return


@app.post("/twosum", response_model=TwoSumResponse)
def two_sum_endpoint(request: TwoSumRequest):
    """
    Solve the Two Sum problem
    
    Given an array of integers and a target, find two numbers that add up to target.
    
    **Algorithm:** Hash Map approach
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Example Request:**
    ```json
    {
        "nums": [2, 7, 11, 15],
        "target": 9
    }
    ```
    
    **Example Response:**
    ```json
    {
        "indices": [0, 1],
        "values": [2, 7],
        "found": true,
        "message": "Found: nums[0] + nums[1] = 2 + 7 = 9"
    }
    ```
    """
    
    # Validate input
    if len(request.nums) < 2:
        raise HTTPException(
            
            detail="Array must have at least 2 numbers"
        )
    
    # Solve the problem
    result = solve_two_sum(request.nums, request.target)
    
    if result:
        idx1, idx2 = result[0], result[1]
        val1, val2 = request.nums[idx1], request.nums[idx2]
        
        return TwoSumResponse(
            indices=result,
            values=[val1, val2],
            found=True,
            message=f"Found: nums[{idx1}] + nums[{idx2}] = {val1} + {val2} = {request.target}",
            algorithm="Hash Map O(n)"
        )
    else:
        return TwoSumResponse(
            indices=None,
            values=None,
            found=False,
            message=f"No solution found for target {request.target}",
            algorithm="Hash Map O(n)"
        )




# Run the server
if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Two Sum API Server Starting...")
    print("=" * 60)
    print("📚 Swagger UI:  http://localhost:8000/swagger")
    print("📖 ReDoc:       http://localhost:8000/redoc")
    print("🏥 Health:      http://localhost:8000/health")
    print("=" * 60)
    print("\nPress CTRL+C to stop the server\n")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )

