import asyncio
import datetime
import logging
import logging.handlers
import sys
from typing import Any, Dict

import discord
import toml
from discord.ext import commands

config = toml.load("config.toml")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

EXTS = {"jishaku", "cogs.roles"}
from cogs.roles.views import NotificationView, PronounsView


class Table(commands.Bot):
    def __init__(self, logger: logging.Logger):
        super().__init__(
            command_prefix=commands.when_mentioned_or("!"),
            intents=intents,
        )
        self.config: Dict[str, Any] = config
        self.logger: logging.Logger = logger
        self.uptime: datetime.datetime

    async def setup_hook(self):
        for ext in EXTS:
            await self.load_extension(ext)
            self.logger.info(f"Loaded {ext}")

        self.add_view(NotificationView())
        self.add_view(PronounsView())

    async def on_ready(self):
        if hasattr(self, "uptime") or self.user is None:
            return

        self.uptime = discord.utils.utcnow()
        self.logger.info(f"Logged into {self.user}")


async def main():
    logger = logging.getLogger("discord")
    logger.setLevel(logging.INFO)
    logging.getLogger("discord.http").setLevel(logging.INFO)

    handlers = [
        logging.handlers.RotatingFileHandler(
            filename="discord.log",
            encoding="utf-8",
            maxBytes=32 * 1024 * 1024,  # 32 MiB
            backupCount=5,  # Rotate through 5 files
        ),
        logging.StreamHandler(sys.stdout),
    ]

    formatter = logging.Formatter(
        "[{asctime}] [{levelname:<8}] {name}: {message}", "%Y-%m-%d %H:%M:%S", style="{"
    )

    for handler in handlers:
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    async with Table(logger=logger) as bot:
        await bot.start(config["token"])


asyncio.run(main())
