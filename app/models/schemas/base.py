from datetime import datetime, timezone

from pydantic import BaseConfig, BaseModel

class Base(BaseModel):
  class Config(BaseConfig):
    allow_population_by_field_name = True
    json_encoders = {
      datetime: lambda dt: dt.replace(tzinfo=timezone.utc)
            .isoformat()
            .replace("+00:00", "Z")
    }