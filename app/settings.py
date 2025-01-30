from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str = "database.db"
    DB_DRIVER: str = "sqlite"

    @property
    def db_url(self):
        db_path = Path(self.DB_NAME).absolute()
        return f"{self.DB_DRIVER}:///{db_path}"
