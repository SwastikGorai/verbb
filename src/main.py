from fastapi import FastAPI
from verbbadmin.route import router as verbadmin_router
# from schools.route import router as schools_router

app = FastAPI()

app.include_router(verbadmin_router, tags=["verbadmin"])
# app.include_router(schools_router, prefix="/schools", tags=["schools"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
