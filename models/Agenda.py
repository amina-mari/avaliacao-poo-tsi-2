from Atendimento import Atendimento
from Paciente import Paciente
from exceptions import HorarioIndisponivelError
from exceptions import PacienteJaAgendadoError

class Agenda():
    limite_minutos = 240

    def __init__(self, atendimentos: list[Atendimentos]): ...
        self._atendimentos = atendimentos

    @property
    def atendimentos(self) -> list[Atendimentos]:
        return self._atendimentos
        
    @property
    def minutos_ocupados(self) -> int:
        return sum([atendimento.duracao_minutos() for atendimento in self.atendimentos])

    def agendar(self, atendimento: Atendimento):
        if (self.minutos_ocupados() + atendimento.duracao_minutos() > limite_minutos):
            excedimento_horario = self.minutos_ocupados() + atendimento.duracao_minutos() - limite_minutos
            raise HorarioIndisponivelError(f"O atendimento excede o horário da agenda em {excedimento_horario} minutos")
        
        for at in self.atendimentos:
            if(at.paciente.nome == atendimento.paciente.nome):
                raise PacienteJaAgendadoError(f"O paciente {atendimento.paciente.nome} já está agendado na Agenda para este atendimento: {at}")
        
        self._atendimentos.append(atendimento)