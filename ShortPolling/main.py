from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time
import threading
import math

app = FastAPI()

jobs = {}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def updatejob(jobid, progress):
    jobs[jobid] = progress
    print(f"Updated {jobid} to {progress}")
    if progress == 100:
        return
    time.sleep(2)
    updatejob(jobid, progress + 10)

@app.post("/submit")
async def submit():
    jobid = "job" + str(round(time.time()))
    jobs[jobid] = 0
    threading.Thread(target=updatejob, args=(jobid, 0)).start()
    return JSONResponse({"jobid": jobid})

@app.get("/status/{jobid}")
async def status(jobid):
    print(f"Got status request for {jobid} with progress {jobs[jobid]}")
    msg = jobs[jobid]
    if msg == 100:
        msg = "Completed"
    return JSONResponse({"progress": msg})


# Client Use 
# curl -X POST http://localhost:8000/submit
# curl -X GET http://localhost:8000/status/job1705266442