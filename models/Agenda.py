from .Atendimento import Atendimento
from .Paciente import Paciente
from exceptions.HorarioIndisponivelError import HorarioIndisponivelError
from exceptions.PacienteJaAgendadoError import PacienteJaAgendadoError

class Agenda():
    def __init__(self, limite_minutos: int = 240) -> None: 
        self.limite_minutos = limite_minutos
        self._atendimentos: tuple[Atendimento] = ()

    @property
    def atendimentos(self) -> list[Atendimento]:
        return self._atendimentos
        
    @property
    def minutos_ocupados(self) -> int:
        return sum([atendimento.duracao_minutos() for atendimento in self.atendimentos])

    def agendar(self, atendimento: Atendimento) -> None:
        for at in self.atendimentos:
            if(at.paciente == atendimento.paciente):
                raise PacienteJaAgendadoError(f"O paciente {atendimento.paciente.nome} já está agendado na Agenda para este atendimento: {at}")
        
        if (self.minutos_ocupados + atendimento.duracao_minutos() > self.limite_minutos):
            excedimento_horario: int = self.minutos_ocupados + atendimento.duracao_minutos() - self.limite_minutos
            raise HorarioIndisponivelError(f"O atendimento excede o horário da agenda em {excedimento_horario} minutos")
               
        lista_atendimentos = list(self._atendimentos)
        lista_atendimentos.append(atendimento)
        self._atendimentos = tuple(lista_atendimentos)