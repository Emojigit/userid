# -*- coding: utf-8 -*-

__author__ = "Emoji"
__version__ = "1.0.1"
__url__ = "https://github.com/Emojigit/userid"
__description__ = "Get ids of user, message, etc."
__dname__ = "userid"

from telethon import events
def setup(bot):
    @bot.on(events.NewMessage(pattern='/userid'))
    async def start(event):
        resp = []
        resp.append("Your user ID: `{}` [🔗](tg://user?id={})".format(event.sender_id,event.sender_id))
        rep = await event.get_reply_message()
        if rep != None:
            resp.append("Replied message sender ID: `{}` [🔗](tg://user?id={})".format(rep.sender.id,rep.sender.id))
        resp = "\n".join(resp)
        await event.respond(resp)
        raise events.StopPropagation

