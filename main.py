import os
import sys
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading


class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_web_server():
    server = HTTPServer(("0.0.0.0", int(os.getenv("PORT", 8080))), WebServer)
    server.serve_forever()

API_ID = 37985486
API_HASH = "dbaee05a710790e326b70fcf0853ac33"
SESSION_STR = "1AZwarZUu58i0taMNixQQElHB1w78iVQo7ct5jol_xiV-1SM94vEqpyd6fdPvff6ffCZEJplRFTn_m4twkjPDIZQFBljSTZhKuwQ0pKc6TTrMd57i4T7y4EUAZKPoxDa2aVYdumNmJeP-RxbJwMMcp5ZyWWLyEfr2f1fUg6zVQnDdVynfaJl_UPKVMIIFtneFx_8ei0o-kFA88bLalQlgN_unQlyxwO8E4jshJUOc1UwsmUaNYvlrPvLQIYPYzs1PKRkBFf_uj9uF98sbCAILSOGDu9MLNBVE4pOOOLAF1w03Gl0Ms4nxRLlDUvuQkIC16G1mNlvBVMg/ygNLKaS1FV5gky4ZX1="


threading.Thread(target=run_web_server, daemon=True).start()

bot = TelegramClient(StringSession(SESSION_STR), API_ID, API_HASH)

@bot.on(events.NewMessage(pattern=r'\.ping', incoming=False))
async def ping_handler(event):
    await event.edit("**By**")

bot.start()
bot.run_until_disconnected()
