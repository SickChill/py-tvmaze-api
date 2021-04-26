class TvMazeException(Exception):
    """Unknown error"""

class ConnectionError(TvMazeException):
    pass


class NotFound(TvMazeException):
    """Not Found"""


class ShowNotFound(NotFound):
    """Show Not Found"""


class EpisodeNotFound(NotFound):
    """Episode Not Found"""


class SeasonNotFound(NotFound):
    """Season Not Found"""


class CastNotFound(NotFound):
    """Cast Not Found"""


class PersonNotFound(NotFound):
    """Person Not Found"""


class CharacterNotFound(NotFound):
    """Character Not Found"""


class CrewNotFound(NotFound):
    """Crew Not Found"""


class AkaNotFound(NotFound):
    """Aka Not Found"""


class CountryNotFound(NotFound):
    """Country Not Found"""


class PeopleNotFound(NotFound):
    """People Not Found"""


class ImageNotFound(NotFound):
    """Image Not Found"""


class CastCreditNotFound(NotFound):
    """Cast Credit Not Found"""


class CrewCreditNotFound(NotFound):
    """Crew Credit Not Found"""


class NetworkNotFound(NotFound):
    """Network Not Found"""


class ExternalNotFound(NotFound):
    """External Not Found"""


class RatingNotFound(NotFound):
    """Rating Not Found"""


class ScheduleNotFound(NotFound):
    """Schedule Not Found"""


class WebChannelNotFound(NotFound):
    """Web Channel Not Found"""
