from dataclasses import dataclass, field


@dataclass
class Video:
    title: str
    resolution: str = "raw"
    applied_steps: list[str] = field(default_factory=list)