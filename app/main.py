from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.users.router import router_auth, router_users
from app.bookings.router import router as router_bookings
from app.pages.router import router as router_pages
from app.hotels.router import router as router_hotels

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_bookings)
app.include_router(router_pages)
app.include_router(router_users)
app.include_router(router_auth)
app.include_router(router_hotels)
