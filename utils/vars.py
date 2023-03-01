from __future__ import annotations

from typing import TYPE_CHECKING

import discord
from discord.ext import commands

if TYPE_CHECKING:
    from main import Table

__all__ = ["NotificationRoles", "PronounsRoles", "Context"]

NotificationRoles = {
    "random": {
        "name": "Random",
        "role_id": 885166907190313012,
        "emoji": discord.PartialEmoji(name="\U0001f3b2"),
        "description": "Random pings from staff",
    },
    "giveaways": {
        "name": "Giveaways",
        "role_id": 885166937871646750,
        "emoji": discord.PartialEmoji(name="\U0001f389"),
        "description": "When giveaways are being hosted",
    },
    "server_updates": {
        "name": "Server Updates",
        "role_id": 988339911839076363,
        "emoji": discord.PartialEmoji(name="\U0001f4e2"),
        "description": "When updates for the server happen",
    },
    "polls": {
        "name": "Polls",
        "role_id": 885167012265984031,
        "emoji": discord.PartialEmoji(name="\U0001f4ca"),
        "description": "Whenever a poll is being hosted",
    },
    "chat_active": {
        "name": "Chat active",
        "role_id": 885166869567393813,
        "emoji": discord.PartialEmoji(name="\U0001f4ac"),
        "description": "Whenever chat is dead. Send !deadchat to ping.",
    },
    "minecraft": {
        "name": "Minecraft",
        "role_id": 1080565525261844600,
        "emoji": discord.PartialEmoji(name="minecraft", id=1080568049083621397),
        "description": "When you want to play on the server, +gain access to #minecraft",
    },
}

PronounsRoles = {
    "sh": {
        "name": "She/her",
        "role_id": 996466065825607810,
    },
    "hh": {
        "name": "He/Him",
        "role_id": 996466008850178048,
    },
    "tt": {
        "name": "They/Them",
        "role_id": 996466066626723931,
    },
    "any": {
        "name": "Any",
        "role_id": 996466068237332601,
    },
    "ask": {
        "name": "Ask",
        "role_id": 996466131630051388,
    },
}


class Context(commands.Context):
    bot: Table
