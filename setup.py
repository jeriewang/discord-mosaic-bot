import setuptools
import sys, pathlib

sys.path.append(pathlib.Path(__file__).resolve().parent)
from mosaic_bot import __version__

setuptools.setup(
    name = 'discord-mosaic-bot',
    author = 'Mia Wang',
    url = 'https://bemosiac.art/',
    author_email = 'm@mia.wang',
    python_requires = '>=3.9',
    version = __version__,
    install_requires = [
        'discord.py',
        'aiohttp',
        'chardet',
        'cchardet',
        'aiodns',
        'requests',
        'numpy',
        'pillow',
        'SQLAlchemy',
        'gunicorn',
        'flask'
    ],
    packages = ['mosaic_bot', 'mosaic_bot.bot', 'mosaic_bot.server'],
    zip_safe = False
)
