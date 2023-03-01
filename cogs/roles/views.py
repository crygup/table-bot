from __future__ import annotations

from typing import TYPE_CHECKING, List

import discord
from discord.ext import commands

from utils import NotificationRoles, PronounsRoles

if TYPE_CHECKING:
    from utils import Context


class RoleSetup(discord.ui.Select):
    def __init__(
        self,
        options: List[discord.SelectOption],
        all_role_ids: List[int],
    ):
        self.all_role_ids = all_role_ids

        super().__init__(
            options=options,
            min_values=0,
            max_values=len(options),
            custom_id="table_roles",
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True, ephemeral=True)
        selected_role_ids = [int(value) for value in self.values]
        author: discord.Member = interaction.user  # type: ignore

        missing: List[discord.Role] = []
        selected: List[discord.Role] = []

        for arole_id in self.all_role_ids:
            role = author.guild.get_role(arole_id)
            if role is None:
                continue

            if role.id in selected_role_ids:
                selected.append(role)
            else:
                missing.append(role)

        content = ""
        new_roles = author.roles

        for role in selected:
            if role not in author.roles:
                new_roles.append(role)
                content += f"> `+` {role.mention}\n"
            continue

        for role in missing:
            if role in author.roles:
                new_roles.remove(role)
                content += f"> `-` {role.mention}\n"
            continue

        await author.edit(roles=new_roles, reason="Role menu change")
        await interaction.followup.send(content, ephemeral=True)


class NotificationView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        options = []
        all_role_ids = []

        for nrole in NotificationRoles.values():
            all_role_ids.append(nrole["role_id"])
            options.append(
                discord.SelectOption(
                    label=nrole["name"],
                    emoji=nrole["emoji"],
                    description=nrole["description"],
                    value=nrole["role_id"],
                )
            )
        self.add_item(RoleSetup(options=options, all_role_ids=all_role_ids))


class PronounsView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        options = []
        all_role_ids = []

        for nrole in PronounsRoles.values():
            all_role_ids.append(nrole["role_id"])
            options.append(
                discord.SelectOption(
                    label=nrole["name"],
                    value=nrole["role_id"],
                )
            )
        self.add_item(RoleSetup(options=options, all_role_ids=all_role_ids))
