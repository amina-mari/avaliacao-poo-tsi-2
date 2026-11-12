from .AgendaError import AgendaError

class HorarioIndisponivelError(AgendaError):
    """Infelizmente esse agendamento não pôde ser concluído porque ele estoura o nosso limite de tempo de atendimento."""