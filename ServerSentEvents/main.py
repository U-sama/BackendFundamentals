from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
import asyncio

# Client Code on browser

# let sse = new EventSource("http://localhost:8080/stream");
# sse.onmessage = console.log


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/stream")
async def stream():
    async def event_generator():
        i = 0
        while True:
            yield dict(data=f"hello from server ---- [{i}]")
            i += 1
            await asyncio.sleep(1)
    return EventSourceResponse(event_generator())
