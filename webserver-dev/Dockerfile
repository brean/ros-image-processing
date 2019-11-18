FROM ubuntu:18.04

# install and update pip
RUN apt-get update && apt-get install -q -y \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/

RUN python3 -m pip install aiohttp-devtools jinja2 aiohttp_jinja2
