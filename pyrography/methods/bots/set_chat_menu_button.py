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

from typing import Union

import pyrography
from pyrography import raw
from pyrography import types


class SetChatMenuButton:
    async def set_chat_menu_button(
        self: "pyrography.Client",
        chat_id: Union[int, str] = None,
        menu_button: "types.MenuButton" = None
    ) -> bool:
        """Change the bot's menu button in a private chat, or the default menu button.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the target chat.
                If not specified, default bot's menu button will be changed.

            menu_button (:obj:`~pyrography.types.MenuButton`, *optional*):
                The new bot's menu button.
                Defaults to :obj:`~pyrography.types.MenuButtonDefault`.
        """

        await self.invoke(
            raw.functions.bots.SetBotMenuButton(
                user_id=await self.resolve_peer(chat_id or "me"),
                button=(
                    (await menu_button.write(self)) if menu_button
                    else (await types.MenuButtonDefault().write(self))
                )
            )
        )

        return True
