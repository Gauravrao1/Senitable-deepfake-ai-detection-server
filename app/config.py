import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "sentinel_ai")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-this-in-production")
    ALLOWED_ORIGINS: list = [
        origin.strip()
        for origin in os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
        if origin.strip()
    ]
    ALLOWED_ORIGIN_REGEX: str = os.getenv(
        "ALLOWED_ORIGIN_REGEX",
        r"https://[a-z0-9-]+(?:-[a-z0-9]+)?\.vercel\.app",
    )
    MAX_FILE_SIZE: int = 50 * 1024 * 1024  # 50MB
    UPLOAD_DIR: str = os.getenv(
        "UPLOAD_DIR",
        "/tmp/sentinelai/uploads"
        if os.getenv("VERCEL")
        else os.path.join(os.path.dirname(__file__), "..", "uploads"),
    )


settings = Settings()
