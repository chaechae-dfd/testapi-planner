from fastapi import APIRouter

event_router=APIRouter(
    prefix="/events",
    tags=["Events"]
)

@events_router.get("/")
async def get_all_events():
    return []

@events_get.get("{id}")
async def get_event():
    return ""

@events_router.post("/")
async def create_event():
    return ""

@event_router.put("/{id}")
async def update_event():
    return ""

@event_router.delete("/{id}")
async def delete_event():
    return ""