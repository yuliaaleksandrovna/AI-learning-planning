import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set in .env")

supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

def save_learning_plan(request, plan_json):
    data = {
        "title": plan_json["title"],
        "goal": request.goal,
        "level": request.level,
        "duration_weeks": request.duration_weeks,
        "time_per_week": request.time_per_week,
        "preferred_format": request.preferred_format,
        "plan_json": plan_json,
    }

    result = supabase.table("learning_plans").insert(data).execute()
    return result.data[0]


def get_learning_plans():
    result = (
        supabase
        .table("learning_plans")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )
    return result.data
def get_learning_plan_by_id(plan_id: str):
    result = (
        supabase
        .table("learning_plans")
        .select("*")
        .eq("id", plan_id)
        .single()
        .execute()
    )
    return result.data
def delete_learning_plan_by_id(plan_id: str):
    result = (
        supabase
        .table("learning_plans")
        .delete()
        .eq("id", plan_id)
        .execute()
    )
    return result.data