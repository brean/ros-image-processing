#!/usr/bin/env python3
import os
import argparse
import asyncio
import jinja2
import aiohttp_jinja2
from aiohttp import web
from web.routes.setup import setup as routes_setup


async def create_app(dev: bool = True) -> web.Application:
    """Connect to database and create web application."""
    app = web.Application()
    setup_jinja2(app)
    routes_setup(app, dev)
    if not dev:
        # not a development server - we need to run directly
        parser = argparse.ArgumentParser()
        parser.add_argument('--port', default=4000)
        parser.add_argument('--host', default='0.0.0.0')
        parser.add_argument('--path', default='/tmp/navigation_editor')
        server_cfg = vars(parser.parse_args())
        web.run_app(
            app,
            host=server_cfg['host'],
            port=int(server_cfg['port']),
            path=server_cfg['path'])
    return app


def setup_jinja2(app):
    """Jinja2 setup."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_path, 'templates')
    jinja2_loader = jinja2.FileSystemLoader(template_path)
    aiohttp_jinja2.setup(app, loader=jinja2_loader)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app = loop.run_until_complete(create_app(True))
