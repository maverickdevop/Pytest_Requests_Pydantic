from pydantic import BaseModel, validator, Field, ValidationError, HttpUrl
from datetime import datetime, date
from typing import Union
from src.enums.global_enums import Team

class PaprikaTags(BaseModel):
    id: str
    name: str
    coin_counter: int
    ico_counter: int

class PaprikaTeam(BaseModel):
    id: str = Field(min_length=1, description="id lenght should not be 0")
    name: str = Field(max_length=255, description="Name should be less than 255 symbols")
    position: Team = Field(description="Team members took from Enum list")

class Paprika(BaseModel):
    id: str
    name: str
    symbol: str
    rank: int
    is_new: bool
    is_active: bool
    type: str
    logo: HttpUrl
    tags: list[PaprikaTags]
    team: list[PaprikaTeam]
    description: str
    message: str
    open_source: bool
    development_status: str
    hardware_wallet: bool
    proof_type: str
    org_structure: str
    hash_algorithm: str
    last_data_at: str
    first_data_at: date
    started_at: date

    # Validate logo path
    @validator("logo")
    def check_logo_path(cls, v):
        try:
            assert ".png" in v

        except ValidationError as e:
            print(e.json())

    # Validate data and data format
    @validator("started_at", "first_data_at", pre=True)
    def validate_started_date_format(cls, v):
        return datetime.strptime(v, '%Y-%m-%dT00:00:00Z')