from dataclasses import dataclass


@dataclass(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str
