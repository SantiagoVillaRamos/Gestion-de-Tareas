import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from infrastructure.web.routers.router import router
from domain.exceptions.task_exceptions import TaskNotFoundError

@asynccontextmanager
async def lifesfan(app: FastAPI):
    print(f"Iniciando la aplicación en el puerto 8006")
    yield
    print(f"Finalizando la aplicación en el puerto 8006")   
    

app = FastAPI(
    title="Gestion de Tareas API",
    lifespan=lifesfan,
    description="API para la gestión de tareas utilizando FastAPI",
)

app.include_router(router)


@app.exception_handler(TaskNotFoundError)
async def task_not_found_handler(request: Request, exc: TaskNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc)}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": f"Ocurrió un error interno del servidor: {str(exc)}"}
    )


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Gestion de Tareas API!"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8006, reload=True)
    
    