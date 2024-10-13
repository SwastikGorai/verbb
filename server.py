import os
import uvicorn
from src.main import app

if __name__ == "__main__":
    port = os.getenv("PORT") or 8080
    uvicorn.run(app, host="127.0.0.1", port=int(port))