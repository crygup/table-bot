from __future__ import annotations

from typing import TYPE_CHECKING

import discord
from discord.ext import commands

from utils import BaseCog

from .views import NotificationView, PronounsView

if TYPE_CHECKING:
    from utils import Context


class MainRoleCog(BaseCog):
    @commands.group(name="setup", hidden=True)
    @commands.is_owner()
    async def setup(self, ctx: Context):
        await ctx.send(
            embed=discord.Embed(
                color=0xFFFFFF,
                title="Notification roles",
                description="Select the roles you would like to get notifications for.",
            ),
            view=NotificationView(),
        )

        await ctx.send(
            embed=discord.Embed(
                color=0xFFFFFF,
                title="Pronoun roles",
                description="Select your pronouns.",
            ),
            view=PronounsView(),
        )
