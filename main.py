from __future__ import annotations

import asyncio
import datetime
import logging
import logging.handlers
import sys
from typing import TYPE_CHECKING, Any, Dict

import discord
import toml
from discord.ext import commands
from discord.ext.commands.errors import CommandError

if TYPE_CHECKING:
    from utils import Context

config = toml.load("config.toml")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

EXTS = {"jishaku", "cogs.roles", "cogs.misc"}
from cogs.roles.views import NotificationView, PronounsView


class Table(commands.Bot):
    def __init__(self, logger: logging.Logger):
        super().__init__(
            command_prefix=commands.when_mentioned_or("!"),
            intents=intents,
            allowed_mentions=discord.AllowedMentions.none(),
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

    async def on_command_error(self, ctx: Context, error: CommandError):
        if hasattr(ctx.command, "on_error"):
            return

        if isinstance(error, commands.CommandOnCooldown):
            return

        elif isinstance(error, commands.MissingRole):
            assert ctx.guild
            role = ctx.guild.get_role(int(error.missing_role))
            if role is None:
                return
            await ctx.send(f'Role "{role.name}" is required to run this command.')
            return

        return await super().on_command_error(ctx, error)


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
