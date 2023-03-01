from __future__ import annotations

from typing import TYPE_CHECKING

from .main import MainRoleCog

if TYPE_CHECKING:
    from main import Table


class Roles(MainRoleCog, name="roles"):
    """Role setup for table"""


async def setup(bot: Table):
    await bot.add_cog(Roles(bot))
