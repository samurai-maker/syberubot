# Copyright (C) 2021 CyberUserBot
# This file is a part of < https://github.com/FaridDadashzade/CyberUserBot/ >
# Please read the GNU General Public License v3.0 in
# <https://www.github.com/FaridDadashzade/CyberUserBot/blob/master/LICENSE/>.

import twitter_scraper
import os
import time
import requests
import asyncio
import shutil
from bs4 import BeautifulSoup
from shutil import rmtree
import re
from PIL import Image
from time import sleep
from html import unescape
from re import findall
from selenium import webdriver
from urllib.parse import quote_plus
from urllib.error import HTTPError
from google_trans_new import LANGUAGES, google_translator
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError, PageError
from urbandict import define
from requests import get
from search_engine_parser import GoogleSearch
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googletrans import LANGUAGES, Translator
from gtts import gTTS
from gtts.lang import tts_langs
from emoji import get_emoji_regexp
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from asyncio import sleep
from userbot import CMD_HELP, BOTLOG, bot, BOTLOG_CHATID, YOUTUBE_API_KEY, CHROME_DRIVER, GOOGLE_CHROME_BIN
from userbot.events import register
from userbot.modules.upload_download import progress, humanbytes, time_formatter
from ImageDown import ImageDown
import base64, binascii
import random
from userbot.cmdhelp import CmdHelp
from userbot.utils import chrome, progress
from userbot.utils.cyberimage import googleimagesdownload
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeAudio
from telethon import events
from userbot import LANGUAGE as DIL

CARBONLANG = "auto"
TTS_LANG = "tr"
TRT_LANG = DIL

from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import glob


@register(pattern="^.reddit ?(.*)", outgoing=True)
async def reddit(event):
    sub = event.pattern_match.group(1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Avast/77.2.2153.120',
    }       

    if len(sub) < 1:
        await event.edit("`Xahi?? edir??m bir Subreddit qeyd edin. N??mun??: ``.reddit cyber`")
        return

    kaynak = get(f"https://www.reddit.com/r/{sub}/hot.json?limit=1", headers=headers).json()

    if not "kind" in kaynak:
        if kaynak["error"] == 404:
            await event.edit("`Bel?? bir Subreddit tap??lmad??.`")
        elif kaynak["error"] == 429:
            await event.edit("`Reddit yava??laman?? s??yl??yir.`")
        else:
            await event.edit("`Bir x??ta ba?? verdi...`")
        return
    else:
        await event.edit("`M??lumatlar g??tirilir...`")

        veri = kaynak["data"]["children"][0]["data"]
        mesaj = f"**{veri['title']}**\n??????{veri['score']}\n\nBy: __u/{veri['author']}__\n\n[Link](https://reddit.com{veri['permalink']})"
        try:
            resim = veri["url"]
            with open(f"reddit.jpg", 'wb') as load:
                load.write(get(resim).content)

            await event.client.send_file(event.chat_id, "reddit.jpg", caption=mesaj)
            os.remove("reddit.jpg")
        except Exception as e:
            print(e)
            await event.edit(mesaj + "\n\n`" + veri["selftext"] + "`")

            
@register(pattern="^.twit ?(.*)", outgoing=True)
async def twit(event):
    hesap = event.pattern_match.group(1)
    if len(hesap) < 1:
        await event.edit("`Xahi?? edir??m bir Twitter hesab?? qeyd edin. N??mun??: ``.twit twitter`")
        return
    try:
        twits = list(twitter_scraper.get_tweets(hesap, pages=1))
    except Exception as e:
        await event.edit(f"`Hmm dey??s??n bel?? bir hesab yoxdur. ????nk?? x??ta ba?? verdi. X??ta: {e}`")
        return

    if len(twits) > 2:
        if twits[0]["tweetId"] < twits[1]["tweetId"]:
            twit = twits[1]
            fotolar = twit['entries']['photos']
            sonuc = []
            if len(fotolar) >= 1:
                i = 0
                while i < len(fotolar):
                    with open(f"{hesap}-{i}.jpg", 'wb') as load:
                        load.write(get(fotolar[i]).content)
                    sonuc.append(f"{hesap}-{i}.jpg")
                    i += 1
                await event.client.send_file(event.chat_id, sonuc, caption=f"**{hesap}**\n{twit['time']}\n\n`{twit['text']}`\n\n????{twit['replies']} ????{twit['retweets']} ??????{twit['likes']}")
                await event.delete()
                return
            await event.edit(f"**{hesap}**\n{twit['time']}\n\n`{twit['text']}`\n\n????{twit['replies']} ????{twit['retweets']} ??????{twit['likes']}")
        else:
            twit = twits[1]
            fotolar = twit['entries']['photos']
            sonuc = []
            if len(fotolar) >= 1:
                i = 0
                while i < len(fotolar):
                    with open(f"{hesap}-{i}.jpg", 'wb') as load:
                        load.write(get(fotolar[i]).content)
                    sonuc.append(f"{hesap}-{i}.jpg")
                    i += 1
                print(sonuc)
                await event.client.send_file(event.chat_id, sonuc, caption=f"**{hesap}**\n{twit['time']}\n\n`{twit['text']}`\n\n????{twit['replies']} ????{twit['retweets']} ??????{twit['likes']}")
                await event.delete()
                return
            await event.edit(f"**{hesap}**\n{twit['time']}\n\n`{twit['text']}`\n\n????{twit['replies']} ????{twit['retweets']} ??????{twit['likes']}")
        return
    else:
        twit = twits[0]
        fotolar = twit['entries']['photos']
        sonuc = []
        if len(fotolar) >= 1:
            i = 0
            while i < len(fotolar):
                with open(f"{hesap}-{i}.jpg", 'wb') as load:
                    load.write(get(fotolar[i]).content)
                sonuc.append(f"{hesap}-{i}.jpg")
                i += 1
            await event.client.send_file(event.chat_id, sonuc, caption=f"**{hesap}**\n{twit['time']}\n\n`{twit['text']}`\n\n????{twit['replies']} ????{twit['retweets']} ??????{twit['likes']}")
            await event.delete()
            return
        await event.edit(f"**{hesap}**\n{twit['time']}\n\n`{twit['text']}`\n\n????{twit['replies']} ????{twit['retweets']} ??????{twit['likes']}")
        return
        
@register(outgoing=True, pattern="^.x??b??r(?: |$)(.*)")
async def haber(event):
    TURLER = ["guncel", "magazin", "spor", "ekonomi", "politika", "dunya"]
    cmd = event.pattern_match.group(1)
    if len(cmd) < 1:
            HABERURL = 'https://sondakika.haberler.com/'
    else:
        if cmd in TURLER:
            HABERURL = f'https://sondakika.haberler.com/{cmd}'
        else:
            await event.edit("`Yanl???? x??b??t kateqoriyas??! Tap??lan kateqoriyalar: .x??b??r guncel/magazin/spor/ekonomi/politika/dunya`")
            return
    await event.edit("`X??b??rl??r g??tirilir...`")

    haber = get(HABERURL).text
    kaynak = BeautifulSoup(haber, "lxml")
    haberdiv = kaynak.find_all("div", attrs={"class":"hblnContent"})
    i = 0
    HABERLER = ""
    while i < 3:
        HABERLER += "\n\n>**" + haberdiv[i].find("a").text + "**\n"
        HABERLER += haberdiv[i].find("p").text
        i += 1

    await event.edit(f"**Son d??qiq?? x??b??rl??r {cmd.title()}**" + HABERLER)

@register(outgoing=True, pattern="^.karbon ?(.*)")
async def karbon(e):
    cmd = e.pattern_match.group(1)
    if os.path.exists("@TheCyberUserBot-Karbon.jpg"):
        os.remove("@TheCyberUserBot-Karbon.jpg")

    if len(cmd) < 1:
        await e.edit("??stifad??si: .karbon mesaj")    
    yanit = await e.get_reply_message()
    if yanit:
        cmd = yanit.message
    await e.edit("`Xahi?? edir??m g??zl??yin...`")    

    r = get(f"https://carbonnowsh.herokuapp.com/?code={cmd}")

    with open("@TheCyberUserBot-Karbon.jpg", 'wb') as f:
        f.write(r.content)    

    await e.client.send_file(e.chat_id, file="@TheCyberUserBot-Karbon.jpg", force_document=True, caption="[C Y B E R](https://t.me/TheCyberUserBot) il?? yarad??ld??...")
    await e.delete()

@register(outgoing=True, pattern="^.crblang (.*)")
async def setlang(prog):
    global CARBONLANG
    CARBONLANG = prog.pattern_match.group(1)
    await prog.edit(f"Karbon modulu ??????n default dil {CARBONLANG} olaraq ayarland??.")


@register(outgoing=True, pattern="^.carbon")
async def carbon_api(e):
    """ carbon.now.sh i??in bir ??e??it wrapper """
    await e.edit("`Haz??rlan??r...`")
    CARBON = 'https://carbon.now.sh/?l={lang}&code={code}'
    global CARBONLANG
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Girilen metin, mod??le aktar??l??yor.
    code = quote_plus(pcode)  # ????z??lm???? url'ye d??n????t??r??l??yor.
    await e.edit("`Haz??rlan??r...\nFaiz: 25%`")
    if os.path.isfile("./carbon.png"):
        os.remove("./carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': './'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    await e.edit("`Haz??rlan??r...\nFaiz: 50%`")
    download_path = './'
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    command_result = driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
    # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await e.edit("`????leniyor...\nTamamlanma Oran??: 75%`")
    # ??ndirme i??in bekleniyor
    while not os.path.isfile("./carbon.png"):
        await sleep(0.5)
    await e.edit("`Haz??rlan??r...\nFaiz: 100%`")
    file = './carbon.png'
    await e.edit("`Foto haz??rlan??r...`")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="Bu ????kil [Carbon](https://carbon.now.sh/about/) istifad?? edil??r??k haz??rland??,\
        \nbir [Dawn Labs](https://dawnlabs.io/) proyektidir.",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove('./carbon.png')
    driver.quit()
    # Kar????ya y??klemenin ard??ndan carbon.png kald??r??l??yor
    await e.delete()  # Mesaj siliniyor

@register(outgoing=True, pattern="^.tercume")
async def ceviri(e):
    # http://www.tamga.org/2016/01/web-tabanl-gokturkce-cevirici-e.html #
    await e.edit("`T??rc??m?? edilir...`")
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Girilen metin, mod??le aktar??l??yor.
    url = "http://www.tamga.org/2016/01/web-tabanl-gokturkce-cevirici-e.html"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.find_element_by_name("Latin_Metin").send_keys(pcode)
    Turk = driver.find_element_by_name("G??kt??rk_Metin").get_attribute("value")
    await e.edit(f"**??eviri: T??rk??e -> K??kT??rk??e**\n\n**Verilen Metin:** `{pcode}`\n**????kt??:** `{Turk}`")


@register(outgoing=True, disable_errors=True, pattern=r"^\.img(?: |$)(.*)")
async def img_sampler(event):
    await event.edit("`Haz??rlan??r...`")
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        queryo = event.pattern_match.group(1)
    elif reply:
        queryo = reply.message
    else:
        await event.edit("`Axtara bilm??yim ??????n bir ??ey verm??lis??n!\nN??mun??: .img Cyber`"
        )
        return
    query = queryo + "hd wallpaper"
    lim = findall(r"lim=\d+", query)

    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = 5
    response = googleimagesdownload()

 
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }


    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(
        await event.client.get_input_entity(event.chat_id), lst
    )
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await event.delete()

    query = queryo + "ultra hd wallpaper"
    lim = findall(r"lim=\d+", query)
    
    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = 3
    response = googleimagesdownload()


    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }


    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(
        await event.client.get_input_entity(event.chat_id), lst
    )
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await event.delete()

@register(outgoing=True, pattern="^.currency ?(.*)")
async def moni(event):
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split(" ")
    if len(input_sgra) == 3:
        try:
            number = float(input_sgra[0])
            currency_from = input_sgra[1].upper()
            currency_to = input_sgra[2].upper()
            request_url = "https://api.exchangeratesapi.io/latest?base={}".format(
                currency_from)
            current_response = get(request_url).json()
            if currency_to in current_response["rates"]:
                current_rate = float(current_response["rates"][currency_to])
                rebmun = round(number * current_rate, 2)
                await event.edit("{} {} = {} {}".format(
                    number, currency_from, rebmun, currency_to))
            else:
                await event.edit(
                    "`Bir x??ta ba?? verdi...`"
                )
        except Exception as e:
            await event.edit(str(e))
    else:
        await event.edit("`Yanl???? sintaksis.`")
        return

# The codes belong entirely to https://github.com/FaridDadashzade. Reuse is not allowed.
# ?? https://t.me/FVREED 
      
@register(cyber=True, pattern=r"^.google ?(.*)")
async def googlesearch(cyber):
    soz = cyber.pattern_match.group(1)
    sehife = 1  
    start = (sehife - 1) * 10 + 1
    if not soz:
        await cyber.edit("`Axtar???? ed?? bilm??yim ??????n m??n?? bir??ey verin!`")
        return
    CYBER_API_KEY = ('AIzaSyC3psXHEJpBHuNXdWUMBuU6QmTam0YXwRg')
    url = f"https://www.googleapis.com/customsearch/v1?key={CYBER_API_KEY}&cx=003124365989545633216:m49jkqxkn0e&q={soz}&start={start}"
    data = requests.get(url).json()
    axtaris = data.get("items")
    alinan_neticeler = ""
    for i, sozu_axtar in enumerate(axtaris, start=1):
        basliq = sozu_axtar.get("title")
        sayt_aciqlamasi = sozu_axtar.get("htmlSnippet")
        link = sozu_axtar.get("link")
        alinan_neticeler += f"<b>{basliq}</b>\n<i>{sayt_aciqlamasi}</i>\n\n{link}\n\n"
    try:
        await cyber.edit("<b>Axtard??????n??z:</b>\n<i>" + soz + "</i>\n\n<b>N??tic??:</b>\n" +
                       alinan_neticeler,
                       link_preview=False, parse_mode="html")
    except UnboundLocalError:
        pass
    if BOTLOG:
        await cyber.client.send_message(
            BOTLOG_CHATID,
            soz + "`s??z?? Google'da axtar??ld??!`",
        )
        
# The codes belong entirely to https://github.com/FaridDadashzade. Reuse is not allowed.
# ?? https://t.me/FVREED 

@register(outgoing=True, pattern=r"^.wiki (.*)")
async def wiki(wiki_q):
    """ .wiki komutu Vikipedi ??zerinden bilgi ??eker. """
    match = wiki_q.pattern_match.group(1)
    try:
        summary(match)
    except DisambiguationError as error:
        await wiki_q.edit(f"X??ta.\n\n{error}")
        return
    except PageError as pageerror:
        await wiki_q.edit(f"Axtard??????n??z s??hif?? tap??lmad??.\n\n{pageerror}")
        return
    result = summary(match)
    if len(result) >= 4096:
        file = open("wiki.txt", "w+")
        file.write(result)
        file.close()
        await wiki_q.client.send_file(
            wiki_q.chat_id,
            "wiki.txt",
            reply_to=wiki_q.id,
            caption="`N??tic?? ??ox uzundur, fayl olaraq g??nd??rir??m...`",
        )
        if os.path.exists("wiki.txt"):
            os.remove("wiki.txt")
        return
    await wiki_q.edit("**Axtar????:**\n`" + match + "`\n\n**N??tic??:**\n" + result)
    if BOTLOG:
        await wiki_q.client.send_message(
            BOTLOG_CHATID, f"{match}` teriminin Wikipedia sor??usu u??urla haz??rland??!`")


@register(outgoing=True, pattern="^.ud (.*)")
async def urban_dict(ud_e):
    """ .ud komutu Urban Dictionary'den bilgi ??eker. """
    await ud_e.edit("????leniyor...")
    query = ud_e.pattern_match.group(1)
    try:
        define(query)
    except HTTPError:
        await ud_e.edit(f"Ba??????lay??n, {query} ??????n he??bir n??tic?? tap??lmad??.")
        return
    mean = define(query)
    deflen = sum(len(i) for i in mean[0]["def"])
    exalen = sum(len(i) for i in mean[0]["example"])
    meanlen = deflen + exalen
    if int(meanlen) >= 0:
        if int(meanlen) >= 4096:
            await ud_e.edit("`N??tic?? ??ox uzundur fayl olaraq g??nd??rir??m...`")
            file = open("urbandictionary.txt", "w+")
            file.write("Sor??u: " + query + "\n\nM??nas??: " + mean[0]["def"] +
                       "\n\n" + "N??mun??: \n" + mean[0]["example"])
            file.close()
            await ud_e.client.send_file(
                ud_e.chat_id,
                "urbandictionary.txt",
                caption="`Sonu?? ??ok uzun, dosya yoluyla g??nderiliyor...`")
            if os.path.exists("urbandictionary.txt"):
                os.remove("urbandictionary.txt")
            await ud_e.delete()
            return
        await ud_e.edit("Sor??u: **" + query + "**\n\nM??nas??: **" +
                        mean[0]["def"] + "**\n\n" + "N??mun??: \n__" +
                        mean[0]["example"] + "__")
        if BOTLOG:
            await ud_e.client.send_message(
                BOTLOG_CHATID,
                query + "`s??zc??????n??n UrbanDictionary sorgusu ba??ar??yla ger??ekle??tirildi!`")
    else:
        await ud_e.edit(query + "**??????n he?? bir n??tic?? tap??lmad??.**")


@register(outgoing=True, pattern=r"^.tts(?: |$)([\s\S]*)")
async def text_to_speech(event):
    """ .tts komutu ile Google'??n metinden yaz??ya d??n????t??rme servisi kullan??labilir. """
    if event.fwd_from:
        return
    ttss = event.pattern_match.group(1)
    rep_msg = None
    if event.is_reply:
        rep_msg = await event.get_reply_message()
    if len(ttss) < 1:
        if event.is_reply:
            sarki = rep_msg.text
        else:
            await event.edit("`S??s?? ??evirm??yim ??????n ??mrin yan??nda bir mesaj yazmal??s??n??z.`")
            return

    await event.edit(f"__S??s?? ??evirilir...__")
    chat = "@MrTTSbot"
    async with bot.conversation(chat) as conv:
        try:     
            await conv.send_message(f"/tomp3 {ttss}")
        except YouBlockedUserError:
            await event.reply(f"`Hmm dey??s??n` {chat} `??ng??ll??mis??n. Xahi?? edir??m bloku a??.`")
            return
        ses = await conv.wait_event(events.NewMessage(incoming=True,from_users=1678833172))
        await event.client.send_read_acknowledge(conv.chat_id)
        indir = await ses.download_media()
        voice = await asyncio.create_subprocess_shell(f"ffmpeg -i '{indir}' -c:a libopus 'MrTTSbot.ogg'")
        await voice.communicate()
        if os.path.isfile("MrTTSbot.ogg"):
            await event.client.send_file(event.chat_id, file="MrTTSbot.ogg", voice_note=True, reply_to=rep_msg)
            await event.delete()
            os.remove("MrTTSbot.ogg")
        else:
            await event.edit("`Bir x??ta ba?? verdi!`")


        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID, "U??urla s??s?? ??evirildi!")


@register(outgoing=True, pattern="^.imdb (.*)")
async def imdb(e):
    try:
        movie_name = e.pattern_match.group(1)
        remove_space = movie_name.split(' ')
        final_name = '+'.join(remove_space)
        page = get("https://www.imdb.com/find?ref_=nv_sr_fn&q=" + final_name +
                   "&s=all")
        lnk = str(page.status_code)
        soup = BeautifulSoup(page.content, 'lxml')
        odds = soup.findAll("tr", "odd")
        mov_title = odds[0].findNext('td').findNext('td').text
        mov_link = "http://www.imdb.com/" + \
            odds[0].findNext('td').findNext('td').a['href']
        page1 = get(mov_link)
        soup = BeautifulSoup(page1.content, 'lxml')
        if soup.find('div', 'poster'):
            poster = soup.find('div', 'poster').img['src']
        else:
            poster = ''
        if soup.find('div', 'title_wrapper'):
            pg = soup.find('div', 'title_wrapper').findNext('div').text
            mov_details = re.sub(r'\s+', ' ', pg)
        else:
            mov_details = ''
        credits = soup.findAll('div', 'credit_summary_item')
        if len(credits) == 1:
            director = credits[0].a.text
            writer = 'Not available'
            stars = 'Not available'
        elif len(credits) > 2:
            director = credits[0].a.text
            writer = credits[1].a.text
            actors = []
            for x in credits[2].findAll('a'):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + ',' + actors[1] + ',' + actors[2]
        else:
            director = credits[0].a.text
            writer = 'Not available'
            actors = []
            for x in credits[1].findAll('a'):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + ',' + actors[1] + ',' + actors[2]
        if soup.find('div', "inline canwrap"):
            story_line = soup.find('div',
                                   "inline canwrap").findAll('p')[0].text
        else:
            story_line = 'Not available'
        info = soup.findAll('div', "txt-block")
        if info:
            mov_country = []
            mov_language = []
            for node in info:
                a = node.findAll('a')
                for i in a:
                    if "country_of_origin" in i['href']:
                        mov_country.append(i.text)
                    elif "primary_language" in i['href']:
                        mov_language.append(i.text)
        if soup.findAll('div', "ratingValue"):
            for r in soup.findAll('div', "ratingValue"):
                mov_rating = r.strong['title']
        else:
            mov_rating = 'Not available'
        await e.edit('<a href=' + poster + '>&#8203;</a>'
                     '<b>Ba??l??k : </b><code>' + mov_title + '</code>\n<code>' +
                     mov_details + '</code>\n<b>Reytinq : </b><code>' +
                     mov_rating + '</code>\n<b>??lk?? : </b><code>' +
                     mov_country[0] + '</code>\n<b>Dil : </b><code>' +
                     mov_language[0] + '</code>\n<b>Rejissor : </b><code>' +
                     director + '</code>\n<b>Yazar : </b><code>' + writer +
                     '</code>\n<b>Ulduzlar : </b><code>' + stars +
                     '</code>\n<b>IMDB Url : </b>' + mov_link +
                     '\n<b>Hekay?? : </b>' + story_line,
                     link_preview=True,
                     parse_mode='HTML')
    except IndexError:
        await e.edit("D??zg??n bir film ad?? qeyd edin.")


@register(outgoing=True, pattern=r"^.trt(?: |$)([\s\S]*)")
async def translateme(trans):
    """.trt"""
    translator = Translator()
    textx = await trans.get_reply_message()
    message = trans.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await trans.edit("`T??rc??m?? ed?? bilm??yim ??????n m??n?? bir m??tn ver!`")
        return

    try:
        reply_text = translator.translate(deEmojify(message), dest=TRT_LANG)
    except ValueError:
        await trans.edit("S??hv dil kodu.")
        return

    source_lan = LANGUAGES[f'{reply_text.src.lower()}']
    transl_lan = LANGUAGES[f'{reply_text.dest.lower()}']
    reply_text = f"Bu dild??n:**{source_lan.title()}**\nBu dil??:**{transl_lan.title()}**\n\n{reply_text.text}"

    await trans.edit(reply_text)
    if BOTLOG:
        await trans.client.send_message(
            BOTLOG_CHATID,
            f"{source_lan.title()} s??z?? {transl_lan.title()} t??rc??m?? edildi.",
        )

        
@register(pattern=".lang (trt|tts) (.*)", outgoing=True)
async def lang(value):
    """ .lang komutu birka?? mod??l i??in varsay??lan dili de??i??tirir. """
    util = value.pattern_match.group(1).lower()
    if util == "trt":
        scraper = "Translator"
        global TRT_LANG
        arg = value.pattern_match.group(2).lower()
        if arg in LANGUAGES:
            TRT_LANG = arg
            LANG = LANGUAGES[arg]
        else:
            await value.edit(
                f"`S??hv dil kodu!`\n`Dil kodlar??`:\n\n`{LANGUAGES}`"
            )
            return
    elif util == "tts":
        scraper = "Yaz??dan Sese"
        global TTS_LANG
        arg = value.pattern_match.group(2).lower()
        if arg in tts_langs():
            TTS_LANG = arg
            LANG = tts_langs()[arg]
        else:
            await value.edit(
                f"`S??hv dil kodu!`\n`Dil kodlar??`:\n\n`{LANGUAGES}`"
            )
            return
    await value.edit(f"`{scraper} modulu ??????n default dil {LANG.title()} dilin?? ??evirildi.`")
    if BOTLOG:
        await value.client.send_message(
            BOTLOG_CHATID,
            f"`{scraper} modulu ??????n default dil {LANG.title()} dilin?? ??evirildi.`")

        
@register(outgoing=True, pattern="^.yt (.*)")
async def _(event):
    try:
      from youtube_search import YoutubeSearch
    except:
      os.system("pip install youtube_search")
    from youtube_search import YoutubeSearch
    if event.fwd_from:
        return
    fin = event.pattern_match.group(1)
    stark_result = await event.edit("`Axtar??l??r...`")
    results = YoutubeSearch(f"{fin}", max_results=5).to_dict()
    noob = "<b>YOUTUBE AXTARI??I</b> \n\n"
    for moon in results:
      ytsorgusu = moon["id"]
      kek = f"https://www.youtube.com/watch?v={ytsorgusu}"
      stark_name = moon["title"]
      stark_chnnl = moon["channel"]
      total_stark = moon["duration"]
      stark_views = moon["views"]
      noob += (
        f"<b><u>Ad</u></b> ??? <code>{stark_name}</code> \n"
        f"<b><u>Link</u></b> ???  {kek} \n"
        f"<b><u>Kanal</u></b> ??? <code>{stark_chnnl}</code> \n"
        f"<b><u>Video Uzunlu??u</u></b> ??? <code>{total_stark}</code> \n"
        f"<b><u>G??r??nt??l??nm??</u></b> ??? <code>{stark_views}</code> \n\n"
        )
      await stark_result.edit(noob, parse_mode="HTML")

@register(outgoing=True, pattern=r".rip(a|v) (.*)")
async def download_video(v_url):
    """ .rip komutu ile YouTube ve birka?? farkl?? siteden medya ??ekebilirsin. """
    url = v_url.pattern_match.group(2)
    type = v_url.pattern_match.group(1).lower()

    await v_url.edit("`Y??kl??nm??y?? haz??rlan??r...`")

    if type == "a":
        opts = {
            'format':
            'bestaudio',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'writethumbnail':
            True,
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl':
            '%(id)s.mp3',
            'quiet':
            True,
            'logtostderr':
            False
        }
        video = False
        song = True

    elif type == "v":
        opts = {
            'format':
            'best',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'outtmpl':
            '%(id)s.mp4',
            'logtostderr':
            False,
            'quiet':
            True
        }
        song = False
        video = True

    try:
        await v_url.edit("`Laz??mi m??lumatlar y??kl??nir...`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await v_url.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await v_url.edit("`Y??kl??n??c??k video ??ox q??sad??r.`")
        return
    except GeoRestrictedError:
        await v_url.edit(
            "`Malesef co??rafi k??s??tlamalar y??z??nden i??lem yapamazs??n`")
        return
    except MaxDownloadsReached:
        await v_url.edit("`Maksimum y??klenme limiti a????ld??.`")
        return
    except PostProcessingError:
        await v_url.edit("`??stek s??ras??nda bir hata ba?? verdi.`")
        return
    except UnavailableVideoError:
        await v_url.edit("`Error UnavialableVideoError |//\\| Bu mesaj?? g??r??rsen b??y??k ihtimal ile userbotunda _youtube_ modulu x??ta verdi bu mesaj?? @TheCyberSupport qrupuna g??nd??r`")
        return
    except XAttrMetadataError as XAME:
        await v_url.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await v_url.edit("`Bir x??ta ba?? verdi.`")
        return
    except Exception as e:
        await v_url.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await v_url.edit(f"`Musiqi y??kl??nm??y?? haz??rlan??r:`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(rip_data['duration']),
                                       title=str(rip_data['title']),
                                       performer=str(rip_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Haz??rlan??r...",
                         f"{rip_data['title']}.mp3")))
        os.remove(f"{rip_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await v_url.edit(f"`Musiqi y??kl??nm??y?? haz??rlan??r:`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp4",
            supports_streaming=True,
            caption=rip_data['title'],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Haz??rlan??r...",
                         f"{rip_data['title']}.mp4")))
        os.remove(f"{rip_data['id']}.mp4")
        await v_url.delete()


def deEmojify(inputString):
    return get_emoji_regexp().sub(u'', inputString)

CmdHelp('scrapers').add_command(
    'img', '<d??y??r> <s??z>', 'Google-da ????kil axtarar', 'img CyberUserBot'
).add_command(
    'currency', '<miqdar> <vahid> <??evril??c??k vahid>', 'Valyuta.'
).add_command(
    'carbon', '<metn>', 'carbon.now.sh sayt??ndan istifad?? ed??r??k mesaj??n??za carbon effekti ver??r.'
).add_command(
    'crblang', '<dil>', 'Carbon ??????n dil ayarlayar.'
).add_command(
    'karbon', '<m??tin>', 'Carbon.'
).add_command(
    'google', '<s??z>', 'Googleda axtar???? etm??niz?? yard??m ed??c??k modul.'
).add_command(
    'wiki', '<term>', 'Wikipedia-da axtar???? ed??r.'
).add_command(
    'ud', '<terim>', 'Urban Dictionary axtar?????? etm??k ??????n.'
).add_command(
    'tts', '<m??tn>', 'M??tni s??s?? ??evir??r.'
).add_command(
    'lang', '<dil>', 'tts v?? trt ??????n dil ayarlay??n.'
).add_command(
    'trt', '<m??tn>', 'T??rc??m?? edin!'
).add_command(
    'yt', '<m??tn>', 'YouTube-da axtar???? ed??r'
).add_command(
    'x??b??r', '<guncel/magazin/spor/ekonomi/politika/dunya>', 'Son d??qiq?? x??b??rl??r.'
).add_command(
    'imdb', '<film>', 'Film haqq??nda m??lumat ver??r verir.'
).add_command(
    'ripa', '<link>', 'YouTube-dan (v?? ya ba??qa saytlardan) s??s y??kl??y??r.'
).add_command(
    'ripv', '<link>', 'YouTube-dan (v?? ya ba??qa saytlardan) video y??kl??y??r.'
).add_info(
    '[Rip ??mrinin d??st??kl??ndiyi saytlar.](https://ytdl-org.github.io/youtube-dl/supportedsites.html)'
).add()
