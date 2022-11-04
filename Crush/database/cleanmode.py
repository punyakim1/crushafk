#
# Copyright (C) 2022-2023 by @Darkranger00, < https://github.com/Darkranger00 >.
#
# This file is part of < https://github.com/Darkranger00/crushafk > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Darkranger00/crushafk/tree/main/LICENSE >
#
# All rights reserved.
#

from Crush import db

cleandb = db.cleanmode
cleanmode = {}


async def is_cleanmode_on(chat_id: int) -> bool:
    mode = cleanmode.get(chat_id)
    if not mode:
        user = await cleandb.find_one({"chat_id": chat_id})
        if not user:
            cleanmode[chat_id] = True
            return True
        cleanmode[chat_id] = False
        return False
    return mode


async def cleanmode_on(chat_id: int):
    cleanmode[chat_id] = True
    user = await cleandb.find_one({"chat_id": chat_id})
    if user:
        return await cleandb.delete_one({"chat_id": chat_id})


async def cleanmode_off(chat_id: int):
    cleanmode[chat_id] = False
    user = await cleandb.find_one({"chat_id": chat_id})
    if not user:
        return await cleandb.insert_one({"chat_id": chat_id})

