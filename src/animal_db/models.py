"""Module with all models for the service."""

from datetime import date
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field


class Taxonomy(BaseModel):
    """Base model for taxonomy."""

    common_name: str | None = None
    kingdom: str | None = None
    phylum: str | None = None
    subphylum: str | None = None
    class_name: str | None = Field(default=None, alias='class')
    order: str | None = None
    infraorder: str | None = None
    family: str | None = None
    subfamily: str | None = None
    genus: str | None = None
    species: str | None = None
    subspecies: str | None = None

    @property
    def scientific_name(self) -> str | None:
        """Retriever for the scientific name."""
        if self.genus and self.species:
            return f'{self.genus} {self.species}'
        return self.common_name


class Status(Enum):
    """Status for subjects."""

    ACTIVE = 'active'
    LOAN = 'loan'
    PLANNED = 'planned'
    DECEASED = 'deceased'
    UNKNOWN = 'Unknown'


class Sex(Enum):
    """Sex for animals."""

    MALE = 'male'
    FEMALE = 'female'
    UNKNOWN = 'unknown'


class LifeStage(Enum):
    """Universal life stage for animals and colonies."""

    # Pre-birth
    EGG = 'egg'
    LARVA = 'larva'
    PUPA = 'pupa'

    # 2. Younglings
    HATCHLING = 'hatchling'
    BABY = 'baby'
    SPIDERLING = 'spiderling'
    JUVENILE = 'juvenile'

    # 3. Mature
    SUBADULT = 'subadult'
    ADULT = 'adult'
    SENIOR = 'senior'

    # Others
    UNKNOWN = 'unknown'


class Subject(BaseModel):
    """Base model for animals and groups."""

    name: str
    taxonomy: Taxonomy = Taxonomy()
    status: Status = Status.UNKNOWN
    notes: str | None = None
    acquired_date: date | None = None

    def __repr__(self) -> str:
        """Representation of a subject."""
        spieces = (
            self.taxonomy.scientific_name
            if self.taxonomy.scientific_name
            else 'Unknown spieces'
        )
        return f'{self.name} ({spieces})'


class Animal(Subject):
    """Model for a animal."""

    subject_type: Literal['animal'] = 'animal'
    sex: Sex = Sex.UNKNOWN
    life_stage: LifeStage = LifeStage.UNKNOWN
    birth_date: date | None = None


class Colony(Subject):
    """Model for a colony or group of animals."""

    subject_type: Literal['colony'] = 'colony'
    estimated_count: int | None = None
    is_feeder_colony: bool = True
