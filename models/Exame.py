from .Atendimento import Atendimento
from .Paciente import Paciente

class Exame(Atendimento):
    def __init__(self, paciente: Paciente, tipo: str, jejum: bool = False):
        super().__init__(paciente)
        self.tipo = tipo
        self.jejum = jejum

    def duracao_minutos(self):
        if(self.jejum):
            return 30
        else:
            return 20
