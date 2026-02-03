from dotenv import load_dotenv

load_dotenv(".env.local")

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema
from app.routes.auth import router as auth_router
from app.routes.users import router as users

app = FastAPI()

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
app.include_router(auth_router)
app.include_router(users)

@app.get("/health")
def health():
    return {"status": "ok"}