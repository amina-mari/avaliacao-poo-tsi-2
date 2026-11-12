from abc import ABC, abstractmethod
from .Paciente import Paciente

class Atendimento(ABC):
    def __init__(self, paciente: Paciente):
        self._paciente = paciente
        self._tipo_atendimento = type(self).__name__

    @property
    def paciente(self):
        return self._paciente

    @abstractmethod
    def duracao_minutos(self) -> int: ...

    def __str__(self):
        return f"Tipo de Atendimento: {self._tipo_atendimento} | Paciente: {self.paciente.nome} | Duração do Atendimento: {self.duracao_minutos()}"