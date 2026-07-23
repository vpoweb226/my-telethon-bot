import os
import sys
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = 37985486
API_HASH = "dbaee05a710790e326b70fcf0853ac33"
SESSION_STR = "1AZWarzUBu0batbj3dXd8t21oHY1TZDxlAU9wkP6y_ALIf_Gh7etoMA9wA3oxntuI3efLPU2cpQjSH_k5lMgnti95NXRXjKs_H5ZHyC67yYG3eg2QU6z9NbXiUCqAy7gDI9-eZUQjXbQY-AER-qBVT3xE2GwFxbisfy-0C7cAb6cuYM384neh4IT1VueROv2lhfuIxb-Nx8r9_dT_vVqVrM1-avlPssV3eZQFOK7I0SOpQk8gVFDkQmX9fi438uBNAYryAN888UfEx8xYwxW6Uhg6wYiK-MNj-l3IXugZj-AQO9K7gglFM7ezgAhkfsyvdniKBLIgrVZx3Q1Btbva7jcQY7d2WeQ="

bot = TelegramClient(StringSession(SESSION_STR), API_ID, API_HASH)

@bot.on(events.NewMessage(pattern=r"\.ping", incoming=False))
async def ping_handler(event):
    await event.edit("**By**")

bot.start()
bot.run_until_disconnected()
