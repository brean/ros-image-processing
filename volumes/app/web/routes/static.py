"""Static routes.

For development only, use nginx in production, see
https://docs.aiohttp.org/en/stable/deployment.html
"""
import os
import logging
from aiohttp import web

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.abspath(os.path.join(BASE_PATH, '..', 'static'))


async def static_fav_handler(request):
    """Get favicon for the browser."""
    return web.FileResponse(os.path.join(STATIC_PATH, 'img', 'favicon.ico'))


def setup(app, dev):
    """Configure static paths for DEVELOPMENT environemnt.

    The documentation says you should not provide static files using
    aiohttp in production and use a full webserver (e.g. nginx) instead.

    see https://docs.aiohttp.org/en/stable/deployment.html .
    """
    if not dev:
        return
    logging.info('using the development environment.')
    app.router.add_static('/static', path=STATIC_PATH)
    app.add_routes([
        web.get('/favicon.ico', static_fav_handler),
    ])
