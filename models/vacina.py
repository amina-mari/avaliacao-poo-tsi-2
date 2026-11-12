from dataclasses import dataclass


@dataclass
class Vacina:
    vacina: str
    doses: int = 1

    @property
    def tempo_total_minutos(self) -> int:
        return self.doses * 10
