# Darkcobra Original 🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍
# kangers Keep Credits 😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒
# Made by Dc-Team
# Don't remove these lines u fool ,,, 
#
#
#hehehhe

from math import ceil
import asyncio
import json
import random
import os,re
import urllib
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
from userbot import CMD_LIST, CMD_HELP
import io
#ABAB O KANGAR  BACK OPEN CLSE BTN KANG KIYA TO YE LONE CHIPKA DENA AUR GLOBALS K BINA NAHI CHALAGA aur global 5 gaja diff name and manipulation se imported hai 
#Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:


    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"open")))
   
    async def opner(event):
            if event.query.user_id == bot.uid :
                current_page_number=0
                dc = paginate_help(current_page_number, CMD_LIST, "helpme")
                await event.edit("`>>>\n\nReopened The Main Menu of \n©DARKCOBRA` ", buttons=dc)
            else:
                reply_pop_up_alert = "Please get your own Userbot,for more info visit @DARK_COBRA_SUPPORT!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
               

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Userbot"):
            rev_text = query[::-1]
            dc = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article("© Dark Cobra Userbot Help",text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),buttons=dc,link_preview=False)
            await event.answer([result] if result else None)
        else:
              reply_pop_up_alert = "Please get your own Userbot😁😁,for more info visit @DARK_COBRA_SUPPORT! 😎😎"
              await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            dc = paginate_help(
                current_page_number + 1, CMD_LIST, "helpme")
          
            await event.edit(buttons=dc)
        else:
            Cobra = "Please get your own Userbot, and don't use mine for more info visit @DARK_COBRA_SUPPORT!"
            await event.answer(Cobra, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            dc = paginate_help(
                current_page_number - 1,
                CMD_LIST,  # pylint:disable=E0602
                "helpme"
            )
            
            await event.edit(buttons=dc)
        else:
              TheDark = "Please get your own Userbot😁😁,for more info visit @DARK_COBRA_SUPPORT! 😎😎"
              await event.answer(TheDark, cache_time=0, alert=True)
 #hehehehehhehhehhehe   
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            danish = custom.Button.inline("◤✞ 𝕺𝖕𝖊𝖓 𝕸𝖆𝖎𝖓 𝕸𝖊𝖓𝖚 𝕬𝖌𝖆𝖎𝖓 ✞◥", data="open")
            await event.edit("`Main Menu Has Been Closed`", buttons=danish)
        else:
            reply_pop_up_alert = "Please get your own Userbot😁😁,for more info visit @DARK_COBRA_SUPPORT! 😎😎"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    
  
    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if not event.query.user_id == bot.uid:
            atul= "Please get your own Userbot😁😁,for more info visit @DARK_COBRA_SUPPORT! 😎😎"
            await event.answer(atul, cache_time=0, alert=True)
            return
        plugin_name = event.data_match.group(1).decode("UTF-8")
        help_string = "Commands found in {}:\n".format(plugin_name)
        k = "💠🔮💎"
        u = 0
        for i in CMD_LIST[plugin_name]:
            u += 1
            help_string += str(k[u % 3]) + " " + i + "\n\n"
        if plugin_name in CMD_HELP:
            help_string += (
                f"**📤 PLUGIN NAME 📤 :** `{plugin_name}` \n\n{CMD_HELP[plugin_name]}"
            )
        else:
            help_string += " CMD_HELP not set yet for {} 😅😅".format(plugin_name)

        reply_pop_up_alert = help_string
        reply_pop_up_alert += (
            "\n\n Use .unload {} to remove this plugin\n ©DARK COBRA Userbot".format(plugin_name)
        )
        try:
            if event.query.user_id == bot.uid :
                dc = [custom.Button.inline("◤✞ 𝕲𝖔 𝕭𝖆𝖈𝖐 ✞◥",data="back({})".format(shivam)),custom.Button.inline("◤✞ 𝕮𝖑𝖔𝖘𝖊 ✞◥", data="close")]
                await event.edit(reply_pop_up_alert, buttons=dc)
            else:
                reply_pop_up_alert = "Please get your own Userbot, and don't use mine for more info visit @DARK_COBRA_SUPPORT!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        except: 
            halps = "Do .help {} to get the list of commands.".format(plugin_name)
            await event.edit(halps)
        if len(reply_pop_up_alert) >= 4096:
            programmingerror = "`Pasting Your Help Menu.`"
            await event.answer(programmingerror, cache_time=0, alert=True)
            out_file = reply_pop_up_alert
            url = "https://del.dog/documents"
            r = requests.post(url, data=out_file.encode("UTF-8")).json()
            url = f"https://del.dog/{r['key']}"
            await event.edit(
                f"Pasted {plugin_name} to {url}", link_preview=False, buttons=dc
            )
        else:
            await event.edit(message=reply_pop_up_alert, buttons=dc)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
            
            if event.query.user_id == bot.uid :
                try:
                    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                    buttons = paginate_help(current_page_number, CMD_HELP, "helpme")
                    await event.edit("`>>>\n\nHere Is The Main Menu Of\n©DARKCOBRA`", buttons=buttons)
                except:
                    buttons = paginate_help(0, CMD_HELP, "helpme")
                    await event.edit("`>>>\n\nHere Is The Main Menu Of\n©DARKCOBRA`", buttons=buttons)
            else:
                reply_pop_up_alert = "Please get your own Userbot,for more info visit @DARK_COBRA_SUPPORT!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = Config.NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD
    multi = Config.EMOJI_TO_DISPLAY_IN_HELP
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [custom.Button.inline(
        "{} {}".format(random.choice(list(multi)), x),
        data="us_plugin_{}".format(x))
        for x in helpable_plugins]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    global shivam
    modulo_page = page_number % max_num_pages
    shivam=modulo_page
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("◃:✮𝙿𝚁𝙴𝚅.❃", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("⋇⋆𝙲𝙻✦𝚂𝙴⋆⋇", data="close"),
             custom.Button.inline("❃.𝙽𝙴𝚇𝚃✮:▹", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs

# chal nikal 
# gtfo
