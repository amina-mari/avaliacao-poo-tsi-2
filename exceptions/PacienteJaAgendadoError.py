from .AgendaError import AgendaError

class PacienteJaAgendadoError(AgendaError):
    """Não podemos seguir com o agendamento de um paciente já agendado."""