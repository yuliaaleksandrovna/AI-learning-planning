from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import CreatePlanRequest
from app.fake_llm import generate_fake_learning_plan
from app.db import (
    save_learning_plan,
    get_learning_plans,
    get_learning_plan_by_id,
    delete_learning_plan_by_id,
)

app = FastAPI(title="AI Learning Planner API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # для MVP можно так
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend is running"}


@app.post("/plans")
def create_plan(request: CreatePlanRequest):
    plan_json = generate_fake_learning_plan(request)
    saved_plan = save_learning_plan(request, plan_json)

    return {
        "id": saved_plan["id"],
        "title": plan_json["title"],
        "duration_weeks": plan_json["duration_weeks"],
        "weeks": plan_json["weeks"],
        "created_at": saved_plan["created_at"],
    }


@app.get("/plans")
def list_plans():
    plans = get_learning_plans()

    return [
        {
            "id": plan["id"],
            "title": plan["title"],
            "goal": plan["goal"],
            "level": plan["level"],
            "duration_weeks": plan["duration_weeks"],
            "created_at": plan["created_at"],
        }
        for plan in plans
    ]


@app.get("/plans/{plan_id}")
def get_plan(plan_id: str):
    plan = get_learning_plan_by_id(plan_id)

    return {
        "id": plan["id"],
        "title": plan["title"],
        "goal": plan["goal"],
        "level": plan["level"],
        "duration_weeks": plan["duration_weeks"],
        "time_per_week": plan["time_per_week"],
        "preferred_format": plan["preferred_format"],
        "plan_json": plan["plan_json"],
        "created_at": plan["created_at"],
    }


@app.delete("/plans/{plan_id}")
def delete_plan(plan_id: str):
    deleted_plan = delete_learning_plan_by_id(plan_id)

    if not deleted_plan:
        return {"message": "Plan not found"}

    return {"message": "Plan deleted successfully"}