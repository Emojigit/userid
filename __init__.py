# -*- coding: utf-8 -*-

__author__ = "Emoji"
__version__ = "1.0.3"
__url__ = "https://github.com/Emojigit/userid"
__description__ = "Get ids of user, message, etc."
__dname__ = "userid"

from telethon import events
def setup(bot):
    @bot.on(events.NewMessage(pattern='/userid'))
    async def userid(event):
        resp = []
        resp.append("Your user ID: `{}` [🔗](tg://user?id={})".format(event.sender_id,event.sender_id))
        rep = await event.get_reply_message()
        if rep != None:
            resp.append("Replied message sender ID: `{}` [🔗](tg://user?id={})".format(rep.sender.id,rep.sender.id))
        resp = "\n".join(resp)
        await event.respond(resp)
        raise events.StopPropagation

    @bot.on(events.NewMessage(pattern='/uidlink'))
    async def uidlink(event):
        try:
            i = int(event.text.split(" ",1)[1])
            if i < 1: # -xxxxx is channel or group!
                raise ValueError
        except ValueError:
            await event.respond("Not a valid user id!")
        except IndexError:
            await event.respond("No id given!")
        else:
            await event.respond("[{id}](tg://user?id={id})".format(id=i))
        raise events.StopPropagation

    @bot.on(events.NewMessage(pattern='/chatid'))
    async def chatid(event):
        await event.respond("Chat ID: `{}` ({})".format(event.chat_id,"Direct Message" if event.chat_id > 0 else "Group Chat"))
        raise events.StopPropagation

