"""basic setup for routing."""
from . import static, overview
import aiohttp


def setup(app: aiohttp.web.Application, dev: bool):
    """Configure routing for aiohttp Application.

    :param app: The default web-application the routes will be added to.
    """
    static.setup(app, dev)
    overview.setup(app, dev)
