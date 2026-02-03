import uuid

def unique_email() -> str:
    return f"user-{uuid.uuid4()}@example.com"