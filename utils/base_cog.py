from __future__ import annotations

from typing import TYPE_CHECKING, List

import discord
from discord.ext import commands

if TYPE_CHECKING:
    from main import Table

__all__ = ["BaseCog"]


class BaseCog(commands.Cog):
    bot: Table
    emoji: discord.PartialEmoji

    def __init__(self, bot: Table):
        self.bot = bot

    @property
    def aliases(self) -> List[str]:
        return []
