"""
Pyrography - A wonderful Pyrogram fork inspired by Pyromod & AmanoTeam/Pyrogram.
Copyright (C) 2023-present Lelzin λ <https://github.com/d3cryptofc>

Forked from Pyrogram <https://github.com/pyrogram/pyrogram>,
originally copyright (C) 2017-present Dan <https://github.com/delivrance>

This file is part of Pyrography.

Pyrography is is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

Pyrography is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
for more details.

You should have received a copy of the GNU Lesser General Public License along
with Pyrography. If not, see <http://www.gnu.org/licenses/>.
"""

from pyrogram import raw
from .auto_name import AutoName


class MessageEntityType(AutoName):
    """Message entity type enumeration used in :obj:`~pyrogram.types.MessageEntity`."""

    MENTION = raw.types.MessageEntityMention
    "``@username``"

    HASHTAG = raw.types.MessageEntityHashtag
    "``#hashtag``"

    CASHTAG = raw.types.MessageEntityCashtag
    "``$USD``"

    BOT_COMMAND = raw.types.MessageEntityBotCommand
    "``/start@pyrogrambot``"

    URL = raw.types.MessageEntityUrl
    "``https://pyrogram.org`` (see ``url``)"

    EMAIL = raw.types.MessageEntityEmail
    "``do-not-reply@pyrogram.org``"

    PHONE_NUMBER = raw.types.MessageEntityPhone
    "``+1-123-456-7890``"

    BOLD = raw.types.MessageEntityBold
    "Bold text"

    ITALIC = raw.types.MessageEntityItalic
    "Italic text"

    UNDERLINE = raw.types.MessageEntityUnderline
    "Underlined text"

    STRIKETHROUGH = raw.types.MessageEntityStrike
    "Strikethrough text"

    SPOILER = raw.types.MessageEntitySpoiler
    "Spoiler text"

    CODE = raw.types.MessageEntityCode
    "Monowidth string"

    PRE = raw.types.MessageEntityPre
    "Monowidth block (see ``language``)"

    BLOCKQUOTE = raw.types.MessageEntityBlockquote
    "Blockquote text"

    TEXT_LINK = raw.types.MessageEntityTextUrl
    "For clickable text URLs"

    TEXT_MENTION = raw.types.MessageEntityMentionName
    "for users without usernames (see ``user``)"

    BANK_CARD = raw.types.MessageEntityBankCard
    "Bank card text"

    CUSTOM_EMOJI = raw.types.MessageEntityCustomEmoji
    "Custom emoji"

    UNKNOWN = raw.types.MessageEntityUnknown
    "Unknown message entity type"
