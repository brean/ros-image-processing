import aiohttp
import aiohttp_jinja2


@aiohttp_jinja2.template('index.html')
async def page_overview(request=None):
    return {}


def setup(app: aiohttp.web.Application, dev: bool):
    app.add_routes([
        aiohttp.web.get('/', page_overview, name='overview'),
    ])
