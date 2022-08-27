from databases import Database
from httpx import AsyncClient

import settings

http_client = AsyncClient()
database = Database(settings.DB_DSN)
