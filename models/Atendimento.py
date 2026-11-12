from abc import ABC, abstractmethod
from Paciente import Paciente

class Atendimento(ABC):
    def __init__(self, paciente: Paciente):
        self.paciente = paciente

    @abstractmethod
    def duracao_minutos(self) -> int: ...

    @abstractmethod
    def tipo_atendimento(self) -> str: ...

    def __str__(self):
        return "Tipo de Atendimento: " + self.tipo_atendimento() + "| Paciente: " + self.paciente.nome + "| Duração do Atendimento: " + self.duracao_minutos()