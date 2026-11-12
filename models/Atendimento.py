from abc import ABC, abstractmethod
from Paciente import Paciente

class Atendimento(ABC):
    def __init__(self, tipo: str, paciente: Paciente):
        self.paciente = paciente 
        self.tipo = tipo

    @abstractmethod
    def duracao_minutos(self): ...

    def __str__(self):
        return "Tipo de Atendimento: " + self.tipo + "| Paciente: " + self.paciente.nome + "| Duração do Atendimento: " + self.duracao_minutos()