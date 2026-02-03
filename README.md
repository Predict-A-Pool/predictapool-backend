# Predict-A-Pool Backend

This is the backend codebase for Predict-A-Pool

The project includes the following stack:
- Docker to deploy the app
- Docker compose to coordinate frontend, backend, and db
- Alembic to make database modifications, and SQLAlchemy for ORM
- Dotenv to store everything in .env files instead of polluting our local machine's environment variables
- GraphQL to provide data to frotnend