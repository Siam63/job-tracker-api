from fastapi import FastAPI, HTTPException, status
from app.schemas import JobCreate, JobResponse
from app import models

app = FastAPI(title="Job Tracker API")

@app.get("/")
def root():
    return {"Message": "Job Tracker API is running..."}


@app.post("/jobs", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
def create_job(job: JobCreate):
    new_job = {
        "id": models.job_id_counter,
        "filename": job.filename,
        "file_type": job.file_type,
        "status": "queued",
        "message": "Job created successfully"
    }

    models.jobs.append(new_job)
    models.job_id_counter += 1

    return new_job


@app.get("/jobs")
def get_jobs():
    return models.jobs


@app.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: int):
    for job in models.jobs:
        if job["id"] == job_id:
            return job

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Job not found."
    )


@app.put("/jobs/{job_id}/status", response_model=JobResponse)
def update_job_status(job_id: int, new_status: str):
    allowed_statuses = {"queued", "processing", "completed", "failed"}

    if new_status not in allowed_statuses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid job status."
        )

    for job in models.jobs:
        if job["id"] == job_id:
            job["status"] = new_status
            job["message"] = f"Job status updated to {new_status}"
            return job

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Job not found"
    )


@app.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    for job in models.jobs:
        if job["id"] == job_id:
            models.jobs.remove(job)
            return {"message": "Job deleted successfully"}

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )