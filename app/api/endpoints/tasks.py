from fastapi import APIRouter
import asyncio
from app.models.tasks import Task
router = APIRouter(prefix="/tasks",tags=["tasks"])

tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Learn Git releases", "completed": False},
]

async def get_task_list():
    await asyncio.sleep(1)
    return tasks


@router.get("/",response_model=list[Task])
async def get_all_tasks():
    tasks = await get_task_list()
    return tasks
