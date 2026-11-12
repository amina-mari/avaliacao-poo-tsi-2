from Atendimento import Atendimento
from Paciete import Paciente

class Exame(Atendimento):
    def __init__(self, paciente: Paciente, tipo: str, jejum: bool):
        super().__init__(paciente)
    self.tipo = tipo
    self.jejum = jejum

    def duracao_minutos():
        if(jejum) return 30
        else retun 20
    
    def tipo_atendimento(self) -> str:
        return "Exame"
