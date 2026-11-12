from dataclasses import dataclass


@dataclass(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Paciente):
            return NotImplemented
        return self.nome == outro.nome and self.cartao_sus == outro.cartao_sus
