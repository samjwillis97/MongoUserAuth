from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Schema


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class DBModelMixin(DateTimeModelMixin):
    id: Optional[int] = None