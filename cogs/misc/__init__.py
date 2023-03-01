from __future__ import annotations

from typing import TYPE_CHECKING

from .main import MainRoleCog

if TYPE_CHECKING:
    from main import Table


class Misc(MainRoleCog, name="misc"):
    """Misc commands"""


async def setup(bot: Table):
    await bot.add_cog(Misc(bot))
