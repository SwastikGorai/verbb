from fastapi import FastAPI
from src.verbbadmin.route import router as verbadmin_router
from src.schools.route import router as schools_router

app = FastAPI()

app.include_router(verbadmin_router, tags=["verbadmin"])
app.include_router(schools_router, prefix="/schools", tags=["schools"])

