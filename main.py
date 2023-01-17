import os
import sys
a = sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print(str(a))

from fastapi import FastAPI
from app.routes import router


app = FastAPI()

app.include_router(router)