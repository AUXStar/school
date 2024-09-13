from fastapi import FastAPI

def include_routers(app:FastAPI):
    from . import transaction,user
    app.include_router(transaction.api)
    app.include_router(user.api)
