from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

@dataclass
class Base(DataClassJsonMixin):
    pass

@dataclass
class RRSet(Base):
    subname: str
    type: str
    ttl: str
    records: str

@dataclass
class Domain(Base):
    name: str
    minimum_ttl: int
