from dataclasses import dataclass


@dataclass
class Blog:
    _title: str
    _description: str

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description        
