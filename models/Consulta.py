from Atendimento import Atendimento

class Consulta(Atendimento):
    def __init__(self, tipo: str, paciente: Paciente, especialidade: str, retorno: bool = False):
        super().__init__(tipo, paciente)
        self.especialidade = especialidade
        self.retorno = retorno

    def duracao_minutos(self) -> int:
        if(self.retorno) return 15
        else return 30

    def tipo_atendimento(self) -> str:
        return "Consulta"