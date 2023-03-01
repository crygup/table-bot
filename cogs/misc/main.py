from __future__ import annotations

from typing import TYPE_CHECKING

import discord
from discord.ext import commands

from utils import BaseCog

if TYPE_CHECKING:
    from utils import GuildContext


class MainRoleCog(BaseCog):
    @commands.group(name="deadchat")
    @commands.cooldown(1, 60, commands.BucketType.guild)
    @commands.guild_only()
    @commands.has_role(885166869567393813)
    async def deadchat(self, ctx: GuildContext):
        role = ctx.guild.get_role(885166869567393813)

        if role is None:
            return

        mentions = discord.AllowedMentions.none()
        mentions.roles = True

        await ctx.send(role.mention, allowed_mentions=mentions)

    @commands.group(name="minecraft", aliases=("mc",))
    @commands.cooldown(1, 60, commands.BucketType.guild)
    @commands.has_role(1080565525261844600)
    @commands.guild_only()
    async def minecraft(self, ctx: GuildContext):
        role = ctx.guild.get_role(1080565525261844600)

        if role is None:
            return

        mentions = discord.AllowedMentions.none()
        mentions.roles = True

        await ctx.send(
            f"{role.mention}, {ctx.author.mention} wants to play minecraft!",
            allowed_mentions=mentions,
        )
