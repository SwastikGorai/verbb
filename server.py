import os
import uvicorn
from src.main import app

if __name__ == "__main__":
    port = os.getenv("PORT") or 8181
    uvicorn.run(app, host="0.0.0.0", port=int(port))