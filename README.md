# FastAPI inferring Depends

A wrapper around FastAPI's Depends function that infers its return type from its input

## Example

```python
from fastapi_inferring_depends import Depends
from fastapi import FastAPI

router = FastAPI()


async def answer_to_everything_dependency():
    return 42


@app.get("/answer")
async def get_answer_to_everything(
    answer_to_everything=Depends(answer_to_everything_dependency),
):
    # type of answer_to_everything is 'int' (inferred from dependency)
    return {"answer": answer_to_everything}
```
