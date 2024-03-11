import time
from fastapi import HTTPException, APIRouter
from src.line_provider.schemas import Event, events

router = APIRouter(prefix="/api/v1")

@router.post('/event')
async def create_event(event: Event) -> dict:
    if event.event_id not in events:
        events[event.event_id] = event
        return {}

    for p_name, p_value in event.model_dump(exclude_unset=True).items():
        setattr(events[event.event_id], p_name, p_value)

    return {}


@router.get('/event/{event_id}')
async def get_event(event_id: str) -> Event:
    if event_id in events:
        return events[event_id]

    raise HTTPException(status_code=404, detail="Event not found")


@router.get('/events')
async def get_events() -> list[Event] | None:
    return list(e for e in events.values() if time.time() < e.deadline)
