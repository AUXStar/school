from fastapi import FastAPI

def include_routers(app:FastAPI):
    from . import transaction
    app.include_router(transaction.api)
