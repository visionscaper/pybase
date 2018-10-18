from basics.logging import get_logger


class Base:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._valid = True
        self._log = get_logger(self.__class__.__name__)

    def instance_valid(self):
        return self._valid

