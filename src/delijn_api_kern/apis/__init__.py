
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from delijn_api_kern.api.districten_api import DistrictenApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from delijn_api_kern.api.districten_api import DistrictenApi
from delijn_api_kern.api.entiteiten_api import EntiteitenApi
from delijn_api_kern.api.gemeenten_api import GemeentenApi
from delijn_api_kern.api.haltes_api import HaltesApi
from delijn_api_kern.api.lijnen_api import LijnenApi
from delijn_api_kern.api.lijnkleuren_api import LijnkleurenApi
from delijn_api_kern.api.omleidingen_api import OmleidingenApi
from delijn_api_kern.api.routeplan_api import RouteplanApi
from delijn_api_kern.api.vervoerregios_api import VervoerregiosApi
