from pydantic import BaseModel


class CreatePlanRequest(BaseModel):
    goal: str
    level: str
    duration_weeks: int
    time_per_week: int
    preferred_format: str