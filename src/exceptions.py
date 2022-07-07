from typing import Union
from delijn_api_zoek import exceptions as _zoek_exceptions
from delijn_api_kern import exceptions as _kern_exceptions


class DelijnApiError(Exception):
    """Bundle exceptions from the 2 api's"""
    def __init__(self, exception):
        self.exception: Union[_zoek_exceptions, _kern_exceptions] = exception
        super().__init__(self.exception)
