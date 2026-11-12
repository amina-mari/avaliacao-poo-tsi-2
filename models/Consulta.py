from .Atendimento import Atendimento
from .Paciente import Paciente

class Consulta(Atendimento):
    def __init__(self, paciente: Paciente, especialidade: str, retorno: bool = False):
        super().__init__(paciente)
        self.especialidade = especialidade
        self.retorno = retorno

    def duracao_minutos(self) -> int:
        if(self.retorno): 
            return 15
        else: 
            return 30