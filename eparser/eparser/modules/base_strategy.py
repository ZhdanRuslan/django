import abc


class Context:
    """
    Strategy context for different origins
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def parse_vacancy(self, data):
        self._strategy.parse_vacancy(data)


class Strategy(metaclass=abc.ABCMeta):
    """
    Abstract strategy
    """

    @abc.abstractmethod
    def parse_vacancy(self, data):
        pass