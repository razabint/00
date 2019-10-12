# -*- coding: utf-8 -*-
#HIT TEAM PROTECT BOT
#VERSI        = PROTECT + PUBLIC BOT
#ASIST        = 1 INDUK + 15 ASIST
#CREATOR    = BINTANG
#=======================================#
import BINTANG
from BINTANG import *
from RYO.ttypes import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from datetime import datetime
import pytz, pafy, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, atexit, goslate, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata, youtube_dl
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from time import sleep

#=============================================================#
print ("=============================================================\n                  HIT AUTO PROTECT BOT LINE\n                     CREATOR : BINTANG\n\n=============================================================")
print ("==========[ HACKERS AUTO PROTECT BOT LOGIN START]============")
ME = LINE("ucea3374aa7bef5fec5a78a13cc8074b2:aWF0OiAxNTYzMjgwNDQxNDUxCg==..sg9aCh52RjY6rNY8nhUG2drXl3w=")
H1 = LINE('u5732d19fb78054f11c295d31c953ccfa:aWF0OiAxNTY0MjAzMDMzNTkzCg==..wfdPPRxaZTvWBBHmE2r1RD8mMR4=')
H2 = LINE('uf4dc21d8a316f364c7cf8ebc6dd26e60:aWF0OiAxNTY0MjAzMjk3MTc0Cg==..zywqSgDCgSG4QEeyXH6JNW5nmlw=')
H3 = LINE('ua63ad591b3aa33af8bcb44b7db5080d9:aWF0OiAxNTY0MjAzNTIwMzU0Cg==..MJNFHUYaFIikDgqri2HT4xV2NY8=')
H4 = LINE('u936702c762f5fd642fc33fee30a90575:aWF0OiAxNTY0MjAzNzg0MDMxCg==..t63ESu55MLIQu0eRC6BTRAbgOmo=')
H5 = LINE('u1b85f4a4628e011fea2ecbef0461f1f1:aWF0OiAxNTY0MjA0MDg2NjI4Cg==..xwgOUvM+llQNifDGJLh8lo4LYnk=')
print ("================[HIT AUTO PROTECT BOT START]================")
#=============================================================#
oepoll = OEPoll(ME)
myProfile = ME.getProfile()
mySettings = ME.getSettings()
mid = ME.profile.mid
meMID = ME.getProfile().mid
H1MID = H1.getProfile().mid
H2MID = H2.getProfile().mid
H3MID = H3.getProfile().mid
H4MID = H4.getProfile().mid
H5MID = H5.getProfile().mid
#=============================================================#
D_BOT = [meMID,H1MID,H2MID,H3MID,H4MID,H5MID]
D_BOTS = [ME,H1,H2,H3,H4,H5]
D_PROTECTOR = [H1,H2,H3,H4,H5]
#=============================================================#
D_BOSS = ["u38cbb60440251cd61c2e94efd715b181","u9a8dfc80fb5eace4f194c67bb8145755","ucea3374aa7bef5fec5a78a13cc8074b2"]
D_GHOST = ["uff6245b75a41a2ae7942a909ab6372af","uc21b6d949e7a2a7de1f8a445787d314d","u32baa8793360bb0a85c6b90d03eeb2d5"]
D_KICKER = ["ucea3374aa7bef5fec5a78a13cc8074b2","u5732d19fb78054f11c295d31c953ccfa","uf4dc21d8a316f364c7cf8ebc6dd26e60","ua63ad591b3aa33af8bcb44b7db5080d9","u936702c762f5fd642fc33fee30a90575","u1b85f4a4628e011fea2ecbef0461f1f1"]
#=============================================================#
D_ADM = ["u38cbb60440251cd61c2e94efd715b181","u9a8dfc80fb5eace4f194c67bb8145755"]
D_STAFF = ["u38cbb60440251cd61c2e94efd715b181","u9a8dfc80fb5eace4f194c67bb8145755"]
#=============================================================#
for PRO in D_BOTS:
	for BOSS in D_BOSS:
		try:
			PRO.findAndAddContactByMid(BOSS)
		except: pass
	for  ADMIN in D_ADM:
		try:
			PRO.findAndAddContactByMid(ADMIN)
		except: pass
	for ALLPRO in D_BOT:
		try:
			PRO.findAndAddContactByMid(ALLPRO)
		except: pass
	for CL in D_GHOST:
		try:
			PRO.findAndAddContactByMid(CL)
		except: pass
mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
msg_dict = {}
msg_dict1 = {}
D_NILLA = {
    "KUNCI": False,
    "PERINTAH": "",
    "REMOTE": True,
    "SELFBOT": True,
    "PUBLIC": True,
    "ADDMESS": True,
    "VICTIM": {},
    "PRO_LINK": True,
    "PRO_INVITE": True,
    "PRO_MEMBER": True,
    "PRO_JOIN": True,
    "JSLEAVE": True,
    "ADDVICTIM": False,
    "DELVICTIM": False,
    "STICKER": False,
    "GHOST": False,
    "INVITE": False,
    "CONTACT": False,
    "JOIN": True,
    "JOINLINK": True,
    "WELCOME": False,
    "UNSEND": True,
    "GCOVER": False,
    "IMAGE": False,
    "IMAGES": False,
    "KLIMIT": 500,
    "LIMIT1": 250,
    "LIMIT": 2,
    "AGENT": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}
D_PROMO = """━━━━━━━━━━━━━━━━━━━━━━
  °HACKERS INC. TEAM BOT SERVICE°
━━━━━━━━━━━━━━━━━━━━━━
⭐• SB Reguler             : 200K/3 bln
⭐• SB Plus V.1            : 100K/bln
⭐• SB Plus V.2            : 150K/bln
⭐• SB + 1 AJS V.1       : 150K/bln
⭐• SB + 1 AJS V.2       : 200K/bln
⭐• Couple Bot + 1 AJS : 250K/bln
⭐• Protect Bot  :
       1. 8 Asist + 2 Ajs   : 300K/bln
       2. 12 Asist + 3 Ajs : 400K/bln
       3. 17 Asist + 3 Ajs : 500K/bln
⭐• Jaga Chat Room      : 200K/bln
⭐• Jaga Room Event    : 300K 
       - Free SB Utk Owner (1 bulan)
━━━━━━━━━━━━━━━━━━━━━━
            FITUR H.I.T LINE BOT
━━━━━━━━━━━━━━━━━━━━━━
🎲 On Via VPS
🎲 Remote Comand***
🎲 Always On 24 Jam
🎲 Python3
🎲 Login Via sertifikat (Selfbot)
      - No Link / Token
      - Sekali login selamanya
🎲 Gratis Upgrade Menu Bot
🎲 Akun Asist Bisa Kami sediakan
      - Asist Token Primary Bot
      - Asist Sertifikat Bot
━━━━━━━━━━━━━━━━━━━━━━
               ANOTHER SERVICE
━━━━━━━━━━━━━━━━━━━━━━
🎤• VIP Smule 1th (Bergaransi)
🎤• Akun Fresh Smule Sdh ViIP 1th
🎤• Stiker Line Resmi (Anti Hangus)
🎤• Aplikasi Premium (Pro)
━━━━━━━━━━━━━━━━━━━━━━
📵 LINE : line.me/ti/p/~__me___
📵 WA   : +6281333833838
━━━━━━━━━━━━━━━━━━━━━━"""

D_MENU = """╭━━━━━━━━━━━━━━━━━╮
┃     HACKERS INC. TEAM BOT
┃        SISTEM : PYTHON3
┃ VERSI  : AUTO PROTECT BOT
┣•━━━━━━━━━━━━━━━━━
┃    ⭐• MAIN COMMAND •⭐
┣•━━━━━━━━━━━━━━━━━
┣•    ⭐•  MENU
┣•    ⭐•  OWNER CMD
┣•    ⭐•  ADMIN CMD
┣•    ⭐•  STAFF CMD
┣•    ⭐•  AJS CMD
┣•    ⭐•  REMOTE CMD
┣•    ⭐•  MEDIA CMD
┣•━━━━━━━━━━━━━━━━━
┃   •> CREATOR : BINTANG
┃   •> line.me/ti/p/~__me___
┃   •> WA : +6281333833838
╰━━━━━━━━━━━━━━━━━╯"""

D_MEDIA = """╭━━━━━━━━━━━━━━━━━━╮
┃     HACKERS INC. TEAM BOT
┃         SISTEM : PYTHON3
┃  VERSI  : AUTO PROTECT BOT
┣•━━━━━━━━━━━━━━━━━━
┃    🔰• MEDIA COMMAND •🔰
┣•━━━━━━━━━━━━━━━━━━
┣•  🔰•  MP4 (JUDUL-PENYANYI)
┣•  🔰•  MP3 (JUDUL-PENYANYI)
┣•  🔰•  TODAY
┣•  🔰•  SMULE (ID SMULE)
┣•  🔰•  CEKTTL (TGL-BLN-THN)
┣•  🔰•  BERITA
┣•━━━━━━━━━━━━━━━━━━
┃   •> CREATOR : BINTANG
┃   •> line.me/ti/p/~__me___
┃   •> WA : +6281333833838
╰━━━━━━━━━━━━━━━━━━╯"""

D_OWNERCMD = """╭━━━━━━━━━━━━━━━━━━╮
┃     HACKERS INC. TEAM BOT
┃         SISTEM : PYTHON3
┃       LOGIN : NO TOKEN/QR
┃  VERSI  : AUTO PROTECT BOT
┣•━━━━━━━━━━━━━━━━━━
┃      🏅• PRO SETTING •🏅
┣•━━━━━━━━━━━━━━━━━━
┣•    🏅•  OWNER CMD
┣•    🏅•  PRO BOSS
┣•    🏅•  PRO CON
┣•    🏅•  PRO JOIN/OUT
┣•    🏅•  KICKER OUT
┣•    🏅•  OUT
┣•    🏅•  PRO MID
┣•    🏅•  MY BOTS
┣•    🏅•  ABSEN
┣•    🏅•  JOINLINK ON/OFF
┣•    🏅•  UP
┣•    🏅•  ALL UP
┣•    🏅•  UPVP (Link Youtube)
┣•    🏅•  NM (Nama)
┣•    🏅•  NM1-7 (Nama)
┣•    🏅•  ALLNM (Nama)
┣•    🏅•  JOINLINK ON/OFF
┣•    🏅•  CLEAN.!!!
┣•━━━━━━━━━━━━━━━━━━
┃   •> CREATOR : BINTANG
┃   •> line.me/ti/p/~__me___
┃   •> WA : +6281333833838
╰━━━━━━━━━━━━━━━━━━╯"""

D_REMOTE = """╭━━━━━━━━━━━━━━━━━━━━╮
┃        HACKERS INC. TEAM BOT
┃            SISTEM : PYTHON3
┃     VERSI  : AUTO PROTECT BOT
┣•━━━━━━━━━━━━━━━━━━━━
┃    📵• REMOTE COMMAND •📵
┣•━━━━━━━━━━━━━━━━━━━━
┣•    📵•  PRO GR
┣•    📵•  MEMBERS (NO. GR)
┣•    📵•  SMIDS (NO. GR)
┣•    📵•  INFOGR (NO. GR)
┣•    📵•  RATAKAN (NO. GR)
┣•    📵•  PENDINGAN 
┣•    📵•  CANCEL (NO.PENDINGAN)
┣•    📵•  CANCEL ALL
┣•    📵•  JOINTO (NO. GR)
┣•    📵•  TUNDA (NO. GR)
┣•    📵•  BATAL (GR) (TUNDA)
┣•    📵•  ALLBATAL (NO. GR)
┣•    📵•  JOINTO (NO. GR)
┣•    📵•  LEAVE (NO. GR)
┣•    📵•  ALLMEM (NO. GR)
┣•    📵•  OPENQR (NO. GR)
┣•    📵•  CLOSEQR (NO. GR)
┣•    📵•  RINV (NO. GR) (MID)
┣•    📵•  RKICK (NO. GR) (NO.MEM)
┣•    📵•  RCALL (NO. GR) (MID)
┣•    📵•  RKCALL (NO. GR) (MID)
┣•    📵•  PRO GID
┣•    📵•  TAKEME (GID)
┣•━━━━━━━━━━━━━━━━━━━━
┃         ⛔• DELETE VICTIM •⛔
┣•━━━━━━━━━━━━━━━━━━━━
┣•    ⛔•  VICTIM
┣•    ⛔•  VICTIM ON
┣•    ⛔•  VICTIM OFF
┣•    ⛔•  DEL VICTIM ON
┣•    ⛔•  DEL VICTIM OFF
┣•    ⛔•  DEL VICTIM
┣•━━━━━━━━━━━━━━━━━━━━
┃     •> CREATOR : BINTANG
┃     •> line.me/ti/p/~__me___
┃     •> WA : +6281333833838
╰━━━━━━━━━━━━━━━━━━━━╯"""

D_AJSCMD = """╭━━━━━━━━━━━━━━━━━━━╮
┃       HACKERS INC. TEAM BOT
┃         LOGIN : NO TOKEN/QR
┃    VERSI  : AUTO PROTECT BOT
┣•━━━━━━━━━━━━━━━━━━━
┃          🆑• AJS SETTING •🆑
┣•━━━━━━━━━━━━━━━━━━━
┣•    🆑•  JS IN/OUT
┣•    🆑•  JS UP
┣•    🆑•  JSNM (NAMA)
┣•    🆑•  JSBIO (STATUS)
┣•    🆑•  JS GR
┣•    🆑•  JS STAY
┣•    🆑•  JSTAY (NO.GR)
┣•    🆑•  ALL STAY
┣•    🆑•  JSLEAVE (NO.GR)
┣•    🆑•  JSCLOSE (NO.GR)
┣•    🆑•  JSMEMBERS (NO.GR)
┣•    🆑•  SIKAT (NO.GR) (MID)
┣•    🆑•  CULIK (NO.GR) (JS MEM)
┣•    🆑•  JS CON
┣•    🆑•  JSMID
┣•    🆑•  JS GID
┣•    🆑•  JSTAKE (GID)
┣•━━━━━━━━━━━━━━━━━━━
┃     •> CREATOR : BINTANG
┃     •> line.me/ti/p/~__me___
┃     •> WA : +6281333833838
╰━━━━━━━━━━━━━━━━━━━╯"""

D_ADMINCMD = """╭━━━━━━━━━━━━━━━━━━━╮
┃        HACKERS INC. TEAM BOT
┃            SISTEM : PYTHON3
┃     VERSI  : AUTO PROTECT BOT
┣•━━━━━━━━━━━━━━━━━━━
┃     🗡️• PROTECT OMMAND •🗡️
┣•━━━━━━━━━━━━━━━━━━━
┣•    🗡️•  STATUS
┣•    🗡️•  MODE ON/OFF
┣•    🗡️•  PROGR ON/OFF
┣•    🗡️•  PROINVITE ON/OFF
┣•    🗡️•  PROMEM ON/OFF
┣•    🗡️•  AM ON/OFF
┣•    🗡️•  SIDER ON/OFF
┣•    🗡️•  NOTIF ON/OFF
┣•━━━━━━━━━━━━━━━━━━━
┃   🌀• COMMAND FOR ADMIN •🌀
┣•━━━━━━━━━━━━━━━━━━━
┣•    🌀•  INVITE BINTANG
┣•    🌀•  ADMINLIST
┣•    🌀•  JS STAY
┣•    🌀•  ALL SP
┣•    🌀•  RUNTIME
┣•    🌀•  CEK
┣•    🌀•  DELCHAT
┣•    🌀•  MENTION/TAGALL
┣•    🌀•  INVITE ON/OFF
┣•    🌀•  PENDINGAN
┣•    🌀•  CANCEL (NO.PENDINGAN)
┣•    🌀•  CANCEL ALL
┣•    🌀•  GNAME (NAMA GROUP)
┣•    🌀•  GCOVER
┣•    🌀•  KICK *TAG
┣•    🌀•  DEL VICTIM
┣•━━━━━━━━━━━━━━━━━━━
┃     •> CREATOR : BINTANG
┃     •> line.me/ti/p/~__me___
┃     •> WA : +6281333833838
╰━━━━━━━━━━━━━━━━━━━╯"""

D_STAFFCMD = """╭━━━━━━━━━━━━━━━━━━╮
┃       HIT PROFESIONAL TEAM
┃   VERSI  : AUTO PROTECT BOT
┣•━━━━━━━━━━━━━━━━━━
┃💠• STAFF OMMAND •💠
┣•━━━━━━━━━━━━━━━━━━
┣•    💠•  INVITE BINTANG
┣•    💠•  STATUS
┣•    💠•  CEK
┣•    💠•  ALL SP
┣•    💠•  MENTION
┣•    💠•  INVITE ON/OFF
┣•    💠•  PENDINGAN
┣•    💠•  CANCEL (NO.PENDINGAN)
┣•    💠•  KICK *TAG
┣•    💠•  DEL VICTIM
┣•━━━━━━━━━━━━━━━━━━
┃   •> CREATOR : BINTANG
┃   •> line.me/ti/p/~__me___
┃   •> WA : +6281333833838
╰━━━━━━━━━━━━━━━━━━╯"""
#=============================================================#

def restartBot():
    print ("[ ] BOT RESTARTED")
    backupData()
    time.sleep(0.02)
    python = sys.executable
    os.execl(python, python, *sys.argv)
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def logError(text):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("serverBug.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    if Days > 0 and weaks == 0:
        return '%02d' %(secs)
    if Days > 0 and weaks > 0:
        return '%02d' %(secs)
def backupData():
	try:
		backup = read
		f = codecs.open('read.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		return True
	except Exception as error:
		pass
		return False
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
def callMembers(to, mid):
    try:
        arrData = ""
        textx = "══════════════════════\n 1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            if i not in D_BOT + D_BOSS + D_CREATOR:
                mention = "@x\n"
                slen = str(len(textx))
                elen = str(len(textx) + len(mention) - 1)
                arrData = {'S':slen, 'E':elen, 'M':i}
                arr.append(arrData)
                textx += mention
                if no < len(mid):
                    no += 1
                    textx += " %i. " % (num)
                    num=(num+1)
                else:
                    try:
                        no = "\n[ {} ]".format(str(ME.getGroup(to).name))
                    except: pass
        ME.sendMessage(to, textx + "\n══════════════════════", {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except: pass
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ME.sendMessage(msg.to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        pass
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = ME.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'Hello_World.mp4'})
        data = {'params': obs_params}
        r_vp = ME.server.postContent('{}/talk/vp/upload.nhn'.format(str(ME.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        ME.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))
def removeD(cmd, text):
    key = D_NILLA["PERINTAH"]
    if D_NILLA["KUNCI"] == False: key = ''  
    rmv = len(key + cmd) + 1
    return text[rmv:]
#=============================================================#

with open('blacklist.json', 'r') as fp:
    VICTIM = json.load(fp)
def addvictim():
    with open('blacklist.json', 'w') as fp:
        json.dump(VICTIM, fp, sort_keys=True, indent=4)
#=============================================================#
def command(text):
    pesan = text.lower()
    if D_NILLA["KUNCI"] == True:
        if pesan.startswith(D_NILLA["PERINTAH"]):
            D = pesan.replace(D_NILLA["PERINTAH"],"")
        else:
            D = "Undefined command"
    else:
        D = text.lower()
    return D
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if D_NILLA["ADDMESS"] == True:
                ME.sendImageWithURL(op.param1, "https://1.bp.blogspot.com/-XP5euhzop4w/XVTw6Sxy-pI/AAAAAAAAAeA/sAyLgJC3F8U3Pz3Aj7RPrbwfS8apKGUYwCLcBGAs/s1600/20190814_223326.png")
                ME.sendMessage(op.param1, str(D_PROMO))
                search_url="https://youtu.be/2rRjPIG__zY"
                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                vid = pafy.new(search_url)
                stream = vid.streams
                best = vid.getbest()
                best.resolution, best.extension
                for s in stream:
                	me = best.url
                vin = s.url
                ME.sendVideoWithURL(op.param1, me)
                ME.sendMessage(op.param1,"⭐•Video lengkap :\n\n       https://youtu.be/2rRjPIG__zY")
#===============================[ PROTECTION ROOM ]=============================#
        if op.type == 15:
            if op.param2 in D_GHOST:
                if D_NILLA["JSLEAVE"] == True:
                    ME.findAndAddContactsByMid(op.param2)
                    H1.findAndAddContactsByMid(op.param2)
                    H2.findAndAddContactsByMid(op.param2)
                    H3.findAndAddContactsByMid(op.param2)
                    H4.findAndAddContactsByMid(op.param2)
                    H5.findAndAddContactsByMid(op.param2)
                    try:
                        ME.inviteIntoGroup(op.param1,[op.param2])
                    except:
                        try:
                            H1.inviteIntoGroup(op.param1,[op.param2])
                        except:
                            try:
                                H2.inviteIntoGroup(op.param1,[op.param2])
                            except:
                                try:
                                    H3.inviteIntoGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        H4.inviteIntoGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            H5.inviteIntoGroup(op.param1,[op.param2])
                                        except: pass
        
        if op.type == 17:
            if D_NILLA["PRO_JOIN"] == True:
                if op.param2 in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                    pass
                else:
                    try:
                        if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                            H1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                H2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                    H3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                        H4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                            H5.kickoutFromGroup(op.param1,[op.param2])
                                    except: pass

        if op.type == 11:
            if D_NILLA["PRO_LINK"] == True:
                if op.param2 in D_BOT + D_BOSS + D_ADM + D_GHOST:
                    return
                if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST:
                    random.choice(D_PROTECTOR).kickoutFromGroup(op.param1,[op.param2])
                    G = ME.getGroup(op.param1)
                    if G.preventedJoinByTicket == True:
                        return
                    else:
                        G.preventedJoinByTicket = True
                    random.choice(D_PROTECTOR).updateGroup(G)
                    VICTIM["KICKS"][op.param2] = True
                    addvictim()
        
        if op.type == 19 or op.type == 32:
            if D_NILLA["PRO_MEMBER"] == True:
                if op.param2 in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                	return
                else:
                    try:
                        if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                            H1.findAndAddContactsByMid(op.param3)
                            H1.kickoutFromGroup(op.param1,[op.param2])
                            H1.inviteIntoGroup(op.param1,[op.param3])
                            VICTIM["KICKS"][op.param2] = True
                            addvictim()
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                H2.findAndAddContactsByMid(op.param3)
                                H2.kickoutFromGroup(op.param1,[op.param2])
                                H2.inviteIntoGroup(op.param1,[op.param3])
                                VICTIM["KICKS"][op.param2] = True
                                addvictim()
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                    H3.findAndAddContactsByMid(op.param3)
                                    H3.kickoutFromGroup(op.param1,[op.param2])
                                    H3.inviteIntoGroup(op.param1,[op.param3])
                                    VICTIM["KICKS"][op.param2] = True
                                    addvictim()
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                        H4.findAndAddContactsByMid(op.param3)
                                        H4.kickoutFromGroup(op.param1,[op.param2])
                                        H4.inviteIntoGroup(op.param1,[op.param3])
                                        VICTIM["KICKS"][op.param2] = True
                                        addvictim()
                                except:
                                    try:
                                        if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                            H5.findAndAddContactsByMid(op.param3)
                                            H5.kickoutFromGroup(op.param1,[op.param2])
                                            H5.inviteIntoGroup(op.param1,[op.param3])
                                            VICTIM["KICKS"][op.param2] = True
                                            addvictim()
                                    except: pass
        
        if op.type == 19 or op.type == 32:
            if op.param3 in D_GHOST:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    pass
                else:
                    try:
                        if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                            H1.findAndAddContactsByMid(op.param3)
                            H1.kickoutFromGroup(op.param1,[op.param2])
                            H1.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                H2.findAndAddContactsByMid(op.param3)
                                H2.kickoutFromGroup(op.param1,[op.param2])
                                H2.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                    H3.findAndAddContactsByMid(op.param3)
                                    H3.kickoutFromGroup(op.param1,[op.param2])
                                    H3.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                        H4.findAndAddContactsByMid(op.param3)
                                        H4.kickoutFromGroup(op.param1,[op.param2])
                                        H4.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                            H5.findAndAddContactsByMid(op.param3)
                                            H5.kickoutFromGroup(op.param1,[op.param2])
                                            H5.inviteIntoGroup(op.param1,[op.param3])
                                    except: pass
        
        if op.type == 13:
            if meMID in op.param3:
                if op.param2 in D_BOSS:
                    ME.acceptGroupInvitation(op.param1)
                    G = ME.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    ME.updateGroup(G)
                    LINK = ME.reissueGroupTicket(op.param1)
                    for DXX in D_PROTECTOR:
                        DXX.acceptGroupInvitationByTicket(op.param1,LINK)
                    G = ME.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(D_PROTECTOR).updateGroup(G)
                    ME.sendMessage(op.param1,"═════════════════════\n       THIS ROOM PROTECTED BY\n                         ⭐\n           HACKERS INC. TEAM\n═════════════════════")
                    try:
                        H1.findAndAddContactsByMid("uff6245b75a41a2ae7942a909ab6372af")
                        H1.inviteIntoGroup(op.param1,["uff6245b75a41a2ae7942a909ab6372af"])
                    except:
                        try:
                            H2.findAndAddContactsByMid("uff6245b75a41a2ae7942a909ab6372af")
                            H2.inviteIntoGroup(op.param1,["uff6245b75a41a2ae7942a909ab6372af"])
                        except:
                            try:
                                H3.findAndAddContactsByMid("uff6245b75a41a2ae7942a909ab6372af")
                                H3.inviteIntoGroup(op.param1,["uff6245b75a41a2ae7942a909ab6372af"])
                            except:
                                try:
                                    H4.findAndAddContactsByMid("uff6245b75a41a2ae7942a909ab6372af")
                                    H4.inviteIntoGroup(op.param1,["uff6245b75a41a2ae7942a909ab6372af"])
                                except:
                                    try:
                                        H5.findAndAddContactsByMid("uff6245b75a41a2ae7942a909ab6372af")
                                        H5.inviteIntoGroup(op.param1,["uff6245b75a41a2ae7942a909ab6372af"])
                                    except:
                                        try:
                                            ME.findAndAddContactsByMid("uff6245b75a41a2ae7942a909ab6372af")
                                            ME.inviteIntoGroup(op.param1,["uff6245b75a41a2ae7942a909ab6372af"])
                                        except: pass
                if op.param2 in D_BOT + D_GHOST:
                    ME.acceptGroupInvitation(op.param1)
                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                    try:
                        ME.rejectGroupInvitation(op.param1)
                    except:
                        ME.acceptGroupInvitation(op.param1)
                        ME.kickoutFromGroup(op.param1,[op.param2])
                        ME.leaveGroup(op.param1)
            if H1MID in op.param3:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    H1.acceptGroupInvitation(op.param1)
                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                    try:
                        H1.rejectGroupInvitation(op.param1)
                    except:
                        H1.acceptGroupInvitation(op.param1)
                        H1.kickoutFromGroup(op.param1,[op.param2])
                        H1.leaveGroup(op.param1)
            if H2MID in op.param3:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    H2.acceptGroupInvitation(op.param1)
                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                    try:
                        H2.rejectGroupInvitation(op.param1)
                    except:
                        H2.acceptGroupInvitation(op.param1)
                        H2.kickoutFromGroup(op.param1,[op.param2])
                        H2.leaveGroup(op.param1)
            if H3MID in op.param3:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    H3.acceptGroupInvitation(op.param1)
                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                    try:
                        H3.rejectGroupInvitation(op.param1)
                    except:
                        H3.acceptGroupInvitation(op.param1)
                        H3.kickoutFromGroup(op.param1,[op.param2])
                        H3.leaveGroup(op.param1)
            if H4MID in op.param3:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    H4.acceptGroupInvitation(op.param1)
                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                    try:
                        H4.rejectGroupInvitation(op.param1)
                    except:
                        H4.acceptGroupInvitation(op.param1)
                        H4.kickoutFromGroup(op.param1,[op.param2])
                        H4.leaveGroup(op.param1)
            if H5MID in op.param3:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    H5.acceptGroupInvitation(op.param1)
                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                    try:
                        H5.rejectGroupInvitation(op.param1)
                    except:
                        H5.acceptGroupInvitation(op.param1)
                        H5.kickoutFromGroup(op.param1,[op.param2])
                        H5.leaveGroup(op.param1)
        
        if op.type == 13:
            if op.param3 in VICTIM["KICKS"]:
                if op.param2 in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                    random.choice(D_PROTECTOR).cancelGroupInvitation(op.param1,[op.param3])
                    ME.sendMessage(msg.to,"⭐•Sorry Boss,,,Iser in Victim List...")
                    
        if op.type == 13:
            if D_NILLA["PRO_INVITE"] == True:
                if op.param2 in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                    pass
                else:
                    try:
                        if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                            try:
                                H1.cancelGroupInvitation(op.param1,[op.param3])
                                H1.kickoutFromGroup(op.param1,[op.param2])
                                VICTIM["KICKS"][op.param2] = True
                                addvictim()
                            except:
                                G = ME.getGroup(op.param1)
                                H1.kickoutFromGroup(op.param1,[op.param2])
                                KORBAN = [contact.mid for contact in G.invitee]
                                for XX in KORBAN:
                                    if XX not in D_BOT + D_BOSS + D_ADM + D_GHOST:
                                        random.choice(D_PROTECTOR).cancelGroupInvitation(op.param1,[XX])
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                try:
                                    H2.cancelGroupInvitation(op.param1,[op.param3])
                                    H2.kickoutFromGroup(op.param1,[op.param2])
                                    VICTIM["KICKS"][op.param2] = True
                                    addvictim()
                                except:
                                    G = ME.getGroup(op.param1)
                                    H2.kickoutFromGroup(op.param1,[op.param2])
                                    KORBAN = [contact.mid for contact in G.invitee]
                                    for XX in KORBAN:
                                       if XX not in D_BOT + D_BOSS + D_ADM + D_GHOST:
                                            random.choice(D_PROTECTOR).cancelGroupInvitation(op.param1,[XX])
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                    try:
                                        H3.cancelGroupInvitation(op.param1,[op.param3])
                                        H3.kickoutFromGroup(op.param1,[op.param2])
                                        VICTIM["KICKS"][op.param2] = True
                                        addvictim()
                                    except:
                                        G = ME.getGroup(op.param1)
                                        H3.kickoutFromGroup(op.param1,[op.param2])
                                        KORBAN = [contact.mid for contact in G.invitee]
                                        for XX in KORBAN:
                                            if XX not in D_BOT + D_BOSS + D_ADM + D_GHOST:
                                                random.choice(D_PROTECTOR).cancelGroupInvitation(op.param1,[XX])
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                        try:
                                            H4.cancelGroupInvitation(op.param1,[op.param3])
                                            H4.kickoutFromGroup(op.param1,[op.param2])
                                            VICTIM["KICKS"][op.param2] = True
                                            addvictim()
                                        except:
                                            G = ME.getGroup(op.param1)
                                            H4.kickoutFromGroup(op.param1,[op.param2])
                                            KORBAN = [contact.mid for contact in G.invitee]
                                            for XX in KORBAN:
                                                if XX not in D_BOT + D_BOSS + D_ADM + D_GHOST:
                                                    random.choice(D_PROTECTOR).cancelGroupInvitation(op.param1,[XX])
                                except:
                                    try:
                                        if op.param2 not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                            try:
                                                H5.cancelGroupInvitation(op.param1,[op.param3])
                                                H5.kickoutFromGroup(op.param1,[op.param2])
                                                VICTIM["KICKS"][op.param2] = True
                                                addvictim()
                                            except:
                                                G = ME.getGroup(op.param1)
                                                H5.kickoutFromGroup(op.param1,[op.param2])
                                                KORBAN = [contact.mid for contact in G.invitee]
                                                for XX in KORBAN:
                                                    if XX not in D_BOT + D_BOSS + D_ADM + D_GHOST:
                                                        random.choice(D_PROTECTOR).cancelGroupInvitation(op.param1,[XX])
                                    except: pass
                    
#==============================================================================#
        if op.type == 15:
            if D_NILLA["WELCOME"] == True:
                if op.param2 in D_BOT + D_BOSS:
                    return
                ginfo = ME.getGroup(op.param1)
                contact = ME.getContact(op.param2)   
                path = contact.pictureStatus
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                ME.mention(op.param1,[op.param2])
                random.choice(D_PROTECTOR).sendMessage(op.param1,"           🔰 INFO : MEMBER KELUAR 🔰\n================================\n ⭐• Group     : " + str(ginfo.name) + "\n ⭐• Nama      : " + ME.getContact(op.param2).displayName + "\n ⭐• Tanggal  : " + datetime.strftime(timeNow,'%Y-%m-%d') + "\n ⭐• Jam        : " + datetime.strftime(timeNow,'%H:%M:%S') + "\n================================")
                random.choice(D_PROTECTOR).sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" +path)
        if op.type == 17:
            if D_NILLA["WELCOME"] == True:
                if op.param2 in D_BOT+ D_BOSS:
                    return
                ginfo = ME.getGroup(op.param1)
                contact = ME.getContact(op.param2)
                path = contact.pictureStatus
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                ME.mention(op.param1,[op.param2])
                random.choice(D_PROTECTOR).sendMessage(op.param1,"═════════════════════════\nAssalamualaikum Wr.Wb....\nAhlan wasahlan akhina wa ukhtinal kirom.\nSelamat bergabung di room ini\nSmg kita bisa belajar bareng dsini.\nBAROKALLAH\n\nSalam santun dan salam silaturrahmi.\n═════════════════════════")
                random.choice(D_PROTECTOR).sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" +path)

#==============================================================================#
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            KUNCI = D_NILLA["PERINTAH"].title()
            if D_NILLA["KUNCI"] == False:
                 KUNCI = ''
            if msg.toType == 2:
                 if msg._from in D_ADM:
                     if D_NILLA["GCOVER"] == True:
                         path = ME.downloadObjectMsg(msg_id)
                         D_NILLA["GCOVER"] = False
                         ME.updateGroupPicture(msg.to, path)
                         ME.sendMessage(msg.to,"⭐•Sukses Mengganti Cover Group")
            if msg.contentType == 13:            	
                if D_NILLA["CONTACT"] == True:
                    msg.contentType = 0
                    ME.sendMessage(msg.to, str(msg.contentMetadata["mid"]))
            if msg.contentType == 13:
                if msg._from in D_ADM + D_STAFF:
                    if D_NILLA["INVITE"] == True:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = ME.getGroup(msg.to)              
                         pending = groups.invitee
                         targets = []
                         for mem in groups.members:
                             if _name in mem.displayName:
                                 ME.sendMessage(msg.to,"⭐•Kakak " + _name + "\n⭐•Sudah di invite ke dlm room ini\n⭐•Jika tdk ada di dalam room,,,\n⭐•Coba cek di pendingan boss...")
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                         	pass                         
                         else:
                             for target in targets:
                                 try:                             	
                                     ME.findAndAddContactsByMid(target)
                                     H1.findAndAddContactsByMid(target)
                                     H2.findAndAddContactsByMid(target)
                                     H3.findAndAddContactsByMid(target)
                                     H4.findAndAddContactsByMid(target)
                                     H5.findAndAddContactsByMid(target)
                                     try:
                                         random.choice(D_PROTECTOR).inviteIntoGroup(msg.to,[target])
                                     except: pass
                                     ME.sendMessage(msg.to,"⭐•Sukses Invite kk : " + _name)
                                     break                              
                                 except:
                                     try:
                                         ME.sendMessage(msg.to,"⭐•Failed.!!!")
                                         break
                                     except: pass
#==============================================================================#
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            KUNCI = D_NILLA["PERINTAH"].title()
            if D_NILLA["KUNCI"] == False:
                 KUNCI = ''
            if msg.contentType == 13:
                if msg._from in D_BOSS + D_ADM:
                    if D_NILLA["ADDVICTIM"] == True:
                        if msg.contentMetadata["mid"] in VICTIM["KICKS"]:
                            ME.sendMessage(msg.to,"⭐•Already in Victim list.!!!")
                            D_NILLA["ADDVICTIM"] = True
                        else:
                            VICTIM["KICKS"][msg.contentMetadata["mid"]] = True
                            D_NILLA["ADDVICTIM"] = True
                            addvictim()
                            ME.sendMessage(msg.to,"⭐•Added to Victim list...")
                    if D_NILLA["DELVICTIM"] == True:
                        if msg.contentMetadata["mid"] in VICTIM["KICKS"]:
                            del VICTIM["KICKS"][msg.contentMetadata["mid"]]
                            addvictim()
                            D_NILLA["DELVICTIM"] = True
                        else:
                            D_NILLA["DELVICTIM"] = True
                            ME.sendMessage(msg.to,"⭐•Deleted from Victim list...")
            if msg.contentType == 1:
                if msg._from in D_BOSS:
                    if D_NILLA["IMAGE"] == True:
                        path = ME.downloadObjectMsg(msg_id)
                        path1 = H1.downloadObjectMsg(msg_id)
                        path2 = H2.downloadObjectMsg(msg_id)
                        path3 = H3.downloadObjectMsg(msg_id)
                        path4 = H4.downloadObjectMsg(msg_id)
                        path5 = H5.downloadObjectMsg(msg_id)
                        ME.updateProfilePicture(path)
                        H1.updateProfilePicture(path1)
                        H2.updateProfilePicture(path2)
                        H3.updateProfilePicture(path3)
                        H4.updateProfilePicture(path4)
                        H5.updateProfilePicture(path5)
                        ME.sendMessage(msg.to,"⭐•Changing PP Done")
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != ME.profile.mid:
                        to = sender
                    else:
                        to = receiver
                if msg.toType == 1:
                    to = receiver
                if msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        D = command(text)
#===========================[COMMAND FOR ADMIN]===========================#
                        if D == "menu" or D == "help":
                            if msg._from in D_STAFF:
                                ME.sendMessage(msg.to, str(D_MENU))
                                ME.sendMessage(msg.to,"⭐•COMMAND UNTUK OWNER + ADMIN")
                        if D == "owner cmd":
                            if msg._from in D_ADM:
                                ME.sendMessage(msg.to, str(D_OWNERCMD))
                                ME.sendMessage(msg.to,"⭐•COMMAND KHUSUS OWNER")
                        if D == "admin cmd":
                            if msg._from in D_ADM:
                                ME.sendMessage(msg.to, str(D_ADMINCMD))
                                ME.sendMessage(msg.to,"⭐•COMMAND UNTUK OWNER + ADMIN")
                        if D == "remote cmd":
                            if msg._from in D_ADM:
                                ME.sendMessage(msg.to, str(D_REMOTE))
                                ME.sendMessage(msg.to,"⭐•COMMAND UNTUK OWNER")
                        if D == "staff cmd":
                            if msg._from in D_ADM:
                                ME.sendMessage(msg.to, str(D_STAFFCMD))
                                ME.sendMessage(msg.to,"⭐•COMMAND UNTUK STAFF")
                        if D == "media cmd":
                            if msg._from in D_ADM:
                                ME.sendMessage(msg.to, str(D_MEDIA))
                                ME.sendMessage(msg.to,"⭐•COMMAND UNTUK SEMUA MEMBER")
                        if D == "ajs cmd":
                            if msg._from in D_ADM:
                                ME.sendMessage(msg.to, str(D_AJSCMD))
                                ME.sendMessage(msg.to,"⭐•COMMAND UNTUK OWNER")
                        if D == "reset":
                            if msg._from in D_ADM:
                                ME.sendMessage(msg.to,"⭐•Sistem Restart...")
                                restartBot()
                        if D == "check" or D == "cek":
                            if msg._from in D_ADM + D_BOSS + D_STAFF:
                                eltime = time.time() - mulai
                                ME.sendMessage(msg.to,"⭐•Sistem Active\n⭐•Type     : Pro Bot 8 Asist\n⭐•Cost     : 300k/Bln\n⭐•Owner   : HIDAY_HIT\n⭐•Relogin : Tgl 01\n⭐•Activ Time :\n      "+waktu(eltime))
                        if D == "adminlist":
                            if msg._from in D_ADM:
                                if D_ADM== []:
                                    ME.sendMessage(msg.to,"⭐•Admin Empty...")
                                else:
                                    mc = "        🔰 HIT HIDAY BOT ADMIN 🔰\n══════════════════════\n"
                                    for mi_d in D_ADM:
                                        mc += " ⭐•" +ME.getContact(mi_d).displayName + "\n"
                                    ME.sendMessage(msg.to,mc + "══════════════════════")
                        if D == "progr on":
                            if msg._from in D_ADM:
                            	D_NILLA["PRO_LINK"] = True
                            	ME.sendMessage(msg.to,"⭐•Group Protection On")
                        if D == "progr off":
                            if msg._from in D_ADM:
                            	D_NILLA["PRO_LINK"] = False
                            	ME.sendMessage(msg.to,"⭐•Group Protection Off")
                        if D == "promem on":
                            if msg._from in D_ADM:
                            	D_NILLA["PRO_MEMBER"] = True
                            	ME.sendMessage(msg.to,"⭐•Member Protection On")
                        if D == "promem off":
                            if msg._from in D_ADM:
                            	D_NILLA["PRO_MEMBER"] = False
                            	ME.sendMessage(msg.to,"⭐•Member Protection Off")
                        if D == "proinvite on":
                            if msg._from in D_ADM:
                            	D_NILLA["PRO_INVITE"] = True
                            	ME.sendMessage(msg.to,"⭐•Invite Protection On")
                        if D == "proinvite off":
                            if msg._from in D_ADM:
                            	D_NILLA["PRO_INVITE"] = False
                            	ME.sendMessage(msg.to,"⭐•Invite Protection Off")
                        if D == "invite on":
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                                D_NILLA["INVITE"] = True
                                D_NILLA["PRO_JOIN"] = False
                                ME.sendMessage(msg.to,"⭐•Auto Invite On...\n\n⭐•Silahkan kirim kontaknya..")
                        if D == "invite off":
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                                D_NILLA["INVITE"] = False
                                ME.sendMessage(msg.to,"⭐•Auto Invite Off")
                        if D == "am on":
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                                D_NILLA["PRO_JOIN"] = True
                                ME.sendMessage(msg.to,"⭐•ANTI PENYUSUP ON")
                        if D == "am off":
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                                D_NILLA["PRO_JOIN"] = False
                                ME.sendMessage(msg.to,"⭐•ANTI PENYUSUP OFF")
                        if D == "notif on":
                            if msg._from in D_ADM:
                                D_NILLA["WELCOME"] = True
                                ME.sendMessage(msg.to,"⭐•NOTIF MEMBER JOIN/ LEAVE ON")
                        if D == "notif off":
                            if msg._from in D_ADM:
                                D_NILLA["WELCOME"] = False
                                ME.sendMessage(msg.to,"⭐•NOTIF MEMBER JOIN/ LEAVE OFF")
                        if D == "victim on":
                            if msg._from in D_BOSS:
                                D_NILLA["ADDVICTIM"] = True
                                ME.sendMessage(msg.to,"⭐•Adding Victim On.!!!\n\n⭐•Send Contact...")
                        if D == "victim off":
                            if msg._from in D_BOSS:
                                D_NILLA["ADDVICTIM"] = False
                                ME.sendMessage(msg.to,"⭐•Adding Victim Off.!!!")
                        if D == "del victim on":
                            if msg._from in D_BOSS:
                                D_NILLA["DELVICTIM"] = True
                                ME.sendMessage(msg.to,"⭐•Deleting Victim On.!!!\n\n⭐•Send Contact...")
                        if D == "del victim off" or D == "finish":
                            if msg._from in D_BOSS + D_ADM:
                                D_NILLA["DELVICTIM"] = False
                                ME.sendMessage(msg.to,"⭐•Deleting Victim Off.!!!")
                        if D == "victim":
                            if msg._from in D_BOSS + D_ADM:
                                if VICTIM["KICKS"] == {}:
                                	ME.sendMessage(msg.to,"⭐•Victim Empty.!!!")
                            for K in VICTIM["KICKS"]:
                            	ME.sendMessage(msg.to, None, contentMetadata={'mid': K}, contentType=13)
                        if D == "del all victim" or D == "del victim":
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                                D_NILLA["DELVICTIM"] = True
                            if VICTIM["KICKS"] == {}:
                            	ME.sendMessage(msg.to,"⭐•Target Already Empty.!!!")
                            for K in VICTIM["KICKS"]:
                            	ME.sendMessage(msg.to, None, contentMetadata={'mid': K}, contentType=13)
                            ME.sendMessage(msg.to, "Finish")
                        if D == "mode on":
                            if msg._from in D_ADM:
                                D_NILLA["PRO_LINK"] = True
                                D_NILLA["PRO_MEMBER"] = True
                                D_NILLA["PRO_KICK"] = True
                                D_NILLA["PRO_INVITE"] = True
                                D_NILLA["PRO_JOIN"] = True
                                ME.sendMessage(msg.to,"⭐•All Protection On")
                                G = ME.getGroup(msg.to)
                                if G.preventedJoinByTicket == True:
                                    return
                                else:
                                    G.preventedJoinByTicket = True
                                ME.updateGroup(G)
                        if D == "mode off":
                            if msg._from in D_ADM:
                                D_NILLA["PRO_LINK"] = False
                                D_NILLA["PRO_MEMBER"] = False
                                D_NILLA["PRO_KICK"] = False
                                D_NILLA["PRO_INVITE"] = False
                                D_NILLA["PRO_JOIN"] = False
                                ME.sendMessage(msg.to,"⭐•All Protection Off")
                        if D == "status":
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                                md_ = "      🔰 STATUS PROTECTION 🔰\n═════════════════════\n" 
                                if D_NILLA["PRO_LINK"] == True: md_ +="  ☑️ GROUP PROTECTION      (ON)\n"
                                else: md_ +="  ⛔ GROUP PROTECTION     (OFF)\n"
                                if D_NILLA["PRO_INVITE"] == True: md_ +="  ☑️ INVITE PROTECTION     (ON)\n"
                                else: md_ +="  ⛔ INVITE PROTECTION    (OFF)\n"
                                if D_NILLA["PRO_MEMBER"] == True: md_ +="  ☑️ MEMBER PROTECTION   (ON)\n"
                                else: md_ +="  ⛔ MEMBER PROTECTION  (OFF)\n"
                                if D_NILLA["PRO_JOIN"] == True: md_ +="  ☑️ ANTI MALING                (ON)\n"
                                else: md_ +="  ⛔ ANTI MALING               (OFF)\n"
                                if D_NILLA["WELCOME"] == True: md_ +="  ☑️ NOTIF JOIN/LEAVE       (ON)\n"
                                else: md_ +="  ⛔ NOTIF JOIN/LEAVE      (OFF)\n"
                                ME.sendMessage  (msg.to, str(md_) +"═════════════════════")  
                                
                        if D == "invite bintang":
                            if msg._from in D_ADM:
                                ME.findAndAddContactsByMid("u38cbb60440251cd61c2e94efd715b181")
                                ME.inviteIntoGroup(msg.to,["u38cbb60440251cd61c2e94efd715b181"])
                                ME.sendMessage(msg.to,"⭐•Sukses invite Creator ke room ini")
                        if D.startswith("kick "):
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        if ls not in D_BOT + D_BOSS + D_GHOST:
                                            random.choice(D_PROTECTOR).kickoutFromGroup(msg.to,[ls])
                                            print (msg.to,[ls])
                        if D.startswith("nuke "): 
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                                separate = msg.text.split(" ")
                                group = str(separate[1])
                                mids = str(separate[2])
                                groups = ME.getGroupIdsJoined()
                                GS = groups[int(group)-1]
                                G = ME.getGroup(GS)
                                GM = [contact.mid for contact in G.members]
                                try:
                                    GM2 = GM[int(mids)-1]
                                    GM3 = ME.getContact(GM2).displayName
                                    if GM2 not in D_BOSS:
                                        random.choice(D_PROTECTOR).kickoutFromGroup(GS,[GM2])
                                    ME.sendMessage(msg.to, "⭐•REMOTE KICK SUKSES_\n⭐•VIA SELFBOT_\n\n⭐•Target : "+ GM3 + "_" + "\n⭐•Group  : " + str(G.name) + "_")
                                except: pass
                        if D.startswith("gname "):
                            if msg._from in D_ADM:
                                X = ME.getGroup(to)
                                sep = msg.text.split(" ")
                                X.name = msg.text.replace(sep[0] + " ","")
                                ME.updateGroup(X)
                                ME.sendMessage(msg.to,"⭐•Changing Group Name Sukses...")
                        if D == "gcover":
                            if msg._from in D_ADM:
                                D_NILLA["GCOVER"] = True
                                ME.sendMessage(msg.to,"⭐•Send Foto...")
                        if D == "pendingan":
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                                G = ME.getGroup(msg.to)
                                PMB = [contact.mid for contact in G.invitee]
                                no = 0
                                ret_ = ""
                                for mem in PMB:
                                    GM = ME.getContact(mem).displayName
                                    no += 1
                                    ret_ += "\n "+ str(no) + ". " + GM
                                ME.sendMessage(msg.to,"🔰 GROUP : " + str(G.name) + "🔰\n═══════════════════════\nPENDING MEMBERS : %i  ORANG" % len(G.invitee) + str(ret_ ) + "\n═══════════════════════")
                        if D.startswith("cancel "): 
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                                separate = msg.text.split(" ")
                                mids = msg.text.replace(separate[0] + " ","")
                                G = ME.getGroup(msg.to)
                                GM = [contact.mid for contact in G.invitee]
                                try:
                                    GM2 = GM[int(mids)-1]
                                    GM3 = ME.getContact(GM2).displayName
                                    if GM2 not in D_BOT + D_BOSS + D_GHOST:
                                        random.choice(D_PROTECTOR).cancelGroupInvitation(msg.to,[GM2])
                                    ME.sendMessage(msg.to, "⭐•CANCEL PENDING MEMBER SUKSES_\n\n⭐•Target : "+ GM3 )
                                except: pass
                        if D == 'cancel all' or D == 'cancelall':
                            if msg._from in D_ADM:
                                GR = ME.getGroup(msg.to)
                                TRGT = [contact.mid for contact in GR.invitee]
                                for BL in TRGT:
                                	if BL not in D_BOT + D_BOSS + D_GHOST:
                                	    random.choice(D_PROTECTOR).cancelGroupInvitation(msg.to,[BL])
                                ME.sendMessage(msg.to,"⭐•Sukses Menghapus : " + str(len(TRGT)) + " Pending Invite" )
                        if D == "delchat":
                            if msg._from in D_ADM:
                                ME.removeAllMessages(op.param2)
                                H1.removeAllMessages(op.param2)
                                H2.removeAllMessages(op.param2)
                                H3.removeAllMessages(op.param2)
                                H4.removeAllMessages(op.param2)
                                H5.removeAllMessages(op.param2)
                                ME.sendMessage(msg.to,"⭐•Done")
                        if D == "runtime":
                            if msg._from in D_ADM:
                                eltime = time.time() - mulai
                                bot = "🔰 HIT PROTECT BOT ACTIVE TIME 🔰\n══════════════════════\n⭐•Status : Active\n⭐•Sistem : Running\n⭐•Active Time :\n     " +waktu(eltime)+"\n══════════════════════"
                                ME.sendMessage(msg.to,bot)
                        if D == "all sp":
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                                start = time.time()
                                ME.sendMessage(msg.to,"⭐•SPEED CHECK_")
                                elapsed_time = time.time() - start
                                ME.sendMessage(msg.to,"⭐•PRO*L_Speed :\n\n   "+format(str(elapsed_time/10)))
                                elapsed_time = time.time() - start
                                H1.sendMessage(msg.to,"⭐•PRO*1_Speed :\n\n   "+format(str(elapsed_time/100)))
                                elapsed_time = time.time() - start
                                H2.sendMessage(msg.to,"⭐•PRO*2_Speed :\n\n   "+format(str(elapsed_time/100)))
                                elapsed_time = time.time() - start
                                H3.sendMessage(msg.to,"⭐•PRO*3_Speed :\n\n   "+format(str(elapsed_time/100)))
                                elapsed_time = time.time() - start
                                H4.sendMessage(msg.to,"⭐•PRO*4_Speed :\n\n   "+format(str(elapsed_time/100)))
                                elapsed_time = time.time() - start
                                H5.sendMessage(msg.to,"⭐•PRO*5_Speed :\n\n   "+format(str(elapsed_time/100)))
                        
#===========================[REMOTE COMMAND FOR ADMIN]===========================#
                        if D == "naik":
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                                group = ME.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(D_NILLA["LIMIT"] )
                                ME.sendMessage(msg.to,"⭐•Done")
                                if jmlh <= 1000:
                                    for x in range(jmlh):
                                        if members not in D_BOT + D_BOSS + D_GHOST:
                                            ME.inviteIntoGroupCall(msg.to, contactIds=members)
                        if D == "smid on":
                            if msg._from in D_ADM:
                                D_NILLA["CONTACT"] = True
                                ME.sendMessage(msg.to,"⭐•Steal Mid Contact On.!!!\n\n⭐•Kirim contact yg akan di curi midnya")
                        if D == "smid off":
                            if msg._from in D_ADM:
                                D_NILLA["CONTACT"] = False
                                ME.sendMessage(msg.to,"⭐•Steal Mid Contact Off.!!!")
                        
#===========================[COMMAND FOR OWNER]===========================#
                        
                        if D.startswith("iklan "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                groups = ME.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    ME.sendImageWithURL(op.param1, "https://1.bp.blogspot.com/-XP5euhzop4w/XVTw6Sxy-pI/AAAAAAAAAeA/sAyLgJC3F8U3Pz3Aj7RPrbwfS8apKGUYwCLcBGAs/s1600/20190814_223326.png")
                                    ME.sendMessage(op.param1, str(D_PROMO))
                                    ME.sendMessage(msg.to,"⭐•Done")
                                except: pass
                        if D == "promo":
                          if msg._from in D_BOSS:
                              groups = ME.getGroupIdsJoined()
                              for group in groups:
                                  ME.sendImageWithURL(op.param1, "https://1.bp.blogspot.com/-XP5euhzop4w/XVTw6Sxy-pI/AAAAAAAAAeA/sAyLgJC3F8U3Pz3Aj7RPrbwfS8apKGUYwCLcBGAs/s1600/20190814_223326.png")
                                  ME.sendMessage(op.param1, str(D_PROMO))
                              ME.sendMessage(msg.to,"⭐•Done")
                        if D == "joinlink on":
                            if msg._from in D_BOSS:
                                D_NILLA["JOINLINK"] = True
                                ME.sendMessage(msg.to,"⭐•Join Link On")
                        if D == "joinlink off":
                            if msg._from in D_BOSS:
                                D_NILLA["JOINLINK"] = False
                                ME.sendMessage(msg.to,"⭐•Join Link Off")
                        if D == "pro boss":
                            if msg._from in D_BOSS:
                                if D_BOSS == []:
                                    ME.sendMessage(msg.to,"⭐•Pro Boss Empty...")
                                else:
                                    mc = "    🔰 HIT PROTECT BOT BOSS 🔰\n============================\n"
                                    for mi_d in D_BOSS:
                                        mc += " ⭐•" +ME.getContact(mi_d).displayName + "\n"
                                    ME.sendMessage(msg.to,mc + "============================")
                        if D == "pro mid":
                            if msg._from in D_BOSS:
                                ME.sendMessage(msg.to,meMID+","+H1MID+","+H2MID+","+H3MID+","+H4MID+","+H5MID)
                        if D == "pro out":
                            if msg._from in D_BOSS:
                                D_NILLA["JSLEAVE"] = False
                                for DXX in D_PROTECTOR:
                                	DXX.leaveGroup(msg.to)
                                ME.sendMessage(msg.to,"⭐•Bye...See U Next Time\n⭐•Maap Jika kami ada salah...\n\n⭐•Assalamualaikum Wr.Wb...")
                                ME.leaveGroup(msg.to)
                        if D == "pro join" or D == "!!":
                            if msg._from in D_BOSS:
                                G = ME.getGroup(msg.to)
                                ginfo = ME.getGroup(msg.to)
                                if G.preventedJoinByTicket == False:
                                    return
                                else:
                                    G.preventedJoinByTicket = False
                                ME.updateGroup(G)
                                invsend = 0
                                LINK = ME.reissueGroupTicket(msg.to)
                                for DXX in D_PROTECTOR:
                                      DXX.acceptGroupInvitationByTicket(msg.to,LINK)
                                if G.preventedJoinByTicket == True:
                                    return
                                else:
                                    G.preventedJoinByTicket = True
                                ME.updateGroup(G)
                        if D == "js stay":
                            if msg._from in D_BOSS:
                                ME.findAndAddContactsByMid("uff6245b75a41a2ae7942a909ab6372af")
                                ME.inviteIntoGroup(msg.to,["uff6245b75a41a2ae7942a909ab6372af"])
                                ME.sendMessage(msg.to," ⭐•Anti JS Standby_")
                        if D == "out":
                            if msg._from in D_BOSS:
                            	ME.leaveGroup(msg.to)
                        if D == "kicker out":
                            if msg._from in D_BOSS:
                                for DXX in D_PROTECTOR:
                                	DXX.leaveGroup(msg.to)
                        if D == "my bots":
                            if msg._from in D_BOSS:
                                ME.sendContact(msg.to, meMID)
                                H1.sendContact(msg.to, H1MID)
                                H2.sendContact(msg.to, H2MID)
                                H3.sendContact(msg.to, H3MID)
                                H4.sendContact(msg.to, H4MID)
                                H5.sendContact(msg.to, H5MID)
                        if D == "absen":
                            if msg._from in D_BOSS:
                                ME.sendMessage(msg.to,"⭐•PRO*L_ON_")
                                H1.sendMessage(msg.to,"⭐•PRO*1_ON_")
                                H2.sendMessage(msg.to,"⭐•PRO*2_ON_")
                                H3.sendMessage(msg.to,"⭐•PRO*3_ON_")
                                H4.sendMessage(msg.to,"⭐•PRO*4_ON_")
                                H5.sendMessage(msg.to,"⭐•PRO*5_ON_")
                        if D == "pro con":
                            if msg._from in D_BOSS:
                                try:ME.inviteIntoGroup(msg.to, [meMID]);has = "OK"
                                except:has = "NOT"
                                try:ME.kickoutFromGroup(msg.to, [meMID]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "☑️"
                                else:sil = "⛔"
                                if has1 == "OK":sil1 = "☑️"
                                else:sil1 = "⛔"
                                ME.sendMessage(msg.to,"⭐•_K : {}__\n\n⭐•_I : {}__".format(sil1,sil))
                                try:H1.inviteIntoGroup(msg.to, [H1MID]);has = "OK"
                                except:has = "NOT"
                                try:H1.kickoutFromGroup(msg.to, [H1MID]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "☑️"
                                else:sil = "⛔"
                                if has1 == "OK":sil1 = "☑️"
                                else:sil1 = "⛔"
                                H1.sendMessage(msg.to,"⭐•_K : {}__\n\n⭐•_I : {}__".format(sil1,sil))
                                try:H2.inviteIntoGroup(msg.to, [H2MID]);has = "OK"
                                except:has = "NOT"
                                try:H2.kickoutFromGroup(msg.to, [H2MID]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "☑️"
                                else:sil = "⛔"
                                if has1 == "OK":sil1 = "☑️"
                                else:sil1 = "⛔"
                                H2.sendMessage(msg.to,"⭐•_K : {}__\n\n⭐•_I : {}__".format(sil1,sil))
                                try:H3.inviteIntoGroup(msg.to, [H3MID]);has = "OK"
                                except:has = "NOT"
                                try:H3.kickoutFromGroup(msg.to, [H3MID]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "☑️"
                                else:sil = "⛔"
                                if has1 == "OK":sil1 = "☑️"
                                else:sil1 = "⛔"
                                H3.sendMessage(msg.to,"⭐•_K : {}__\n\n⭐•_I : {}__".format(sil1,sil))
                                try:H4.inviteIntoGroup(msg.to, [H4MID]);has = "OK"
                                except:has = "NOT"
                                try:H4.kickoutFromGroup(msg.to, [H4MID]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "☑️"
                                else:sil = "⛔"
                                if has1 == "OK":sil1 = "☑️"
                                else:sil1 = "⛔"
                                H4.sendMessage(msg.to,"⭐•_K : {}__\n\n⭐•_I : {}__".format(sil1,sil))
                                try:H5.inviteIntoGroup(msg.to, [H5MID]);has = "OK"
                                except:has = "NOT"
                                try:H5.kickoutFromGroup(msg.to, [H5MID]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "☑️"
                                else:sil = "⛔"
                                if has1 == "OK":sil1 = "☑️"
                                else:sil1 = "⛔"
                                H5.sendMessage(msg.to,"⭐•_K : {}__\n\n⭐•_I : {}__".format(sil1,sil))
                        if D == "up":
                            if msg._from in D_BOSS:
                                D_NILLA["IMAGE"] = True
                                ME.sendMessage(msg.to,"⭐•KIRIM FOTONYA...") 
                        if D == "all up":
                            if msg._from in D_BOSS:
                                D_NILLA["IMAGES"] = True
                                ME.sendMessage(msg.to,"⭐•KIRIM FOTONYA...")
                        if D.startswith("upvp"):
                            if msg._from in D_BOSS:
                                link = removeD("upvp", text)
                                contact = ME.getContact(mid)
                                ME.sendMessage(to, "⭐•Changing Video Profile on Pict\n\n⭐•Downloading File")
                                ME.sendMessage(to, "⭐•Progress....Wait for a minute")
                                print("Sedang Mendownload Data ~")
                                pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                                subprocess.getoutput('youtube-dl --format mp4 --output HITBotVP.mp4 {}'.format(link))
                                pict = ME.downloadFileURL(pic)
                                vids = "HITBotVP.mp4"
                                changeVideoAndPictureProfile(pict, vids)
                                ME.sendMessage(to, "⭐•Done...Sukses.....")
                                os.remove("HITBotVP.mp4")
                        if D.startswith("nm "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ","")
                                if len(string) <= 10000000000:
                                    profile = ME.getProfile()
                                    profile.displayName = string
                                    ME.updateProfile(profile)
                                    ME.sendMessage(msg.to,"⭐•Done")
                        if D.startswith("nm1 "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ","")
                                if len(string) <= 10000000000:
                                    profile = H1.getProfile()
                                    profile.displayName = string
                                    H1.updateProfile(profile)
                                    H1.sendMessage(msg.to,"⭐•Done")
                        if D.startswith("nm2 "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ","")
                                if len(string) <= 10000000000:
                                    profile = H2.getProfile()
                                    profile.displayName = string
                                    H2.updateProfile(profile)
                                    H2.sendMessage(msg.to,"⭐•Done")
                        if D.startswith("nm3 "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ","")
                                if len(string) <= 10000000000:
                                    profile = H3.getProfile()
                                    profile.displayName = string
                                    H3.updateProfile(profile)
                                    H3.sendMessage(msg.to,"⭐•Done")
                        if D.startswith("nm4 "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ","")
                                if len(string) <= 10000000000:
                                    profile = H4.getProfile()
                                    profile.displayName = string
                                    H4.updateProfile(profile)
                                    H4.sendMessage(msg.to,"⭐•Done")
                        if D.startswith("nm5 "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ","")
                                if len(string) <= 10000000000:
                                    profile = H5.getProfile()
                                    profile.displayName = string
                                    H5.updateProfile(profile)
                                    H5.sendMessage(msg.to,"⭐•Done")
                        if D.startswith("allnm "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ","")
                                if len(string) <= 1000:
                                    profile = H1.getProfile()
                                    profile.displayName = string
                                    H1.updateProfile(profile)
                                    H1.sendMessage(msg.to,"⭐•Done")
                                    profile = H2.getProfile()
                                    profile.displayName = string
                                    H2.updateProfile(profile)
                                    H2.sendMessage(msg.to,"⭐•Done")
                                    profile = H3.getProfile()
                                    profile.displayName = string
                                    H3.updateProfile(profile)
                                    H3.sendMessage(msg.to,"⭐•Done")
                                    profile = H4.getProfile()
                                    profile.displayName = string
                                    H4.updateProfile(profile)
                                    H4.sendMessage(msg.to,"⭐•Done")
                                    profile = H5.getProfile()
                                    profile.displayName = string
                                    H5.updateProfile(profile)
                                    H5.sendMessage(msg.to,"⭐•Done")
                                    
#===========================[REMOTE COMMAND FOR OWNER]===========================#
                        if D == "pro gr":
                            if msg._from in D_BOSS:
                                ma = ""
                                a = 0
                                gid = ME.getGroupIdsJoined()
                                for i in gid:
                                    G = ME.getGroup(i)
                                    a = a + 1
                                    end = "\n"
                                    ma += " _" + str(a) + ". " +G.name+ "\n"
                                ME.sendMessage(msg.to,"             🔰 PRO GROUPS : "+str(len(gid))+" 🔰\n================================\n" + ma + "\n================================")
                        if D.startswith("members "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                groups = ME.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number)-1]
                                    G = ME.getGroup(group)
                                    no = 0
                                    ret_ = ""
                                    for mem in G.members:
                                        no += 1
                                        ret_ += "\n "+ str(no) + ". " + mem.displayName
                                    ME.sendMessage(msg.to,"🔰 GROUP : " + str(G.name) + "🔰\n═════════════════════════\n MEMBERS :" + ret_ + "\n═════════════════════════\n           🔰 TOTAL : %i  ORANG 🔰" % len(G.members) + "\n═════════════════════════")
                                except: pass
                        if D.startswith("smids "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                groups = ME.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number)-1]
                                    G = ME.getGroup(group)                                
                                    ret_ = "\n"
                                    for mem in G.members:
                                        ret_ += "⭐•"+ mem.displayName
                                        ret_ += "\n   "+ mem.mid + "\n"
                                    ME.sendMessage(msg.to, "[ GROUP : "+ str(G.name) + "]\n"+ str(ret_) + "\n[ TOTAL : %i  ORANG ]"% len(G.members))
                                except: pass
                        if D.startswith("jointo "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                groups = ME.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    G = ME.getGroup(group)
                                    if G.preventedJoinByTicket == False:
                                        pass
                                    else:
                                        G.preventedJoinByTicket = False
                                    ME.updateGroup(G)
                                    invsend = 0
                                    LINK = ME.reissueGroupTicket(group)
                                    for DXX in D_PROTECTOR:
                                        DXX.acceptGroupInvitationByTicket(group,LINK)
                                    if G.preventedJoinByTicket == True:
                                        return
                                    else:
                                        G.preventedJoinByTicket = True
                                    ME.updateGroup(G)
                                    ME.sendMessage(msg.to,"⭐•Done")
                                except: pass
                        if D.startswith("leave "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                groups = ME.getGroupIdsJoined()
                                try:
                                    group = groups[int(number)-1]
                                    G = ME.getGroup(group)
                                    H1.leaveGroup(group)
                                    H2.leaveGroup(group)
                                    H3.leaveGroup(group)
                                    H4.leaveGroup(group)
                                    H5.leaveGroup(group)
                                    ME.leaveGroup(group)
                                    ME.sendMessage(msg.to,"⭐•SUKSES KELUAR DR GROUP :\n   " + str(G.name))
                                except: pass
                        if D == "pro gid":
                            if msg._from in D_BOSS:
                                GR = ME.getGroupIdsJoined()
                                X = ""
                                for GID in GR:
                                	X += "⭐•%s :\n%s\n\n" % (ME.getGroup(GID).name,GID)
                                ME.sendMessage(msg.to, X)
                        if D.startswith("takeme "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                G = msg.text.replace(separate[0] + " ","")
                                gs = ME.getGroup(G)
                                if G == "":
                                	ME.sendMessage(msg.to,"⭐•Invalid Group Id")
                                else:
                                    ME.findAndAddContactsByMid(sender)
                                    H1.findAndAddContactsByMid(sender)
                                    H2.findAndAddContactsByMid(sender)
                                    H3.findAndAddContactsByMid(sender)
                                    H4.findAndAddContactsByMid(sender)
                                    H5.findAndAddContactsByMid(sender)
                                    try:
                                        random.choice(D_PROTECTOR).inviteIntoGroup(G,[sender])
                                    except: pass
                                    ME.sendMessage(msg.to,"⭐•Sukses Inv Owner To Group: \n   " + str(gs.name))
                        if D.startswith("rgname "): 
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                group = str(separate[1])
                                Ngroup = str(separate[2])
                                name = text.replace("rgname " + str(group) + " ","")
                                groups = ME.getGroupIdsJoined()
                                try:
                                    GS = groups[int(group)-1]
                                    gs = ME.getGroup(GS)
                                    ME.updateGroup(gs,str(Ngroup))
                                    ME.sendMessage(msg.to,"⭐•Done")
                                except: pass
                        if D.startswith("allmem "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                groups = ME.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number)-1]
                                    G = ME.getGroup(group)
                                    ret_ = "\n"
                                    for mem in G.members:
                                        ret_ += "⭐•" + mem.displayName
                                        ret_ += "\n   "+ mem.mid + "\n"
                                    ME.sendMessage(msg.to, "🔰 GROUP : " + str(G.name) + " 🔰\n" + str(ret_) + "================================\n              ?? TOTAL  : %i  ORANG ??" % len(G.members) +"\n================================")
                                except: pass
                        if D.startswith("infogr "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                groups = ME.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number)-1]
                                    G = ME.getGroup(group)
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket == True:
                                        gQr = "Tertutup"
                                        gTicket = "Tidak ada"
                                    else:
                                        gQr = "Terbuka"
                                        gTicket = "https://line.me/R/ti/g/{}".format(str(ME.reissueGroupTicket(G.id)))
                                    timeCreated = []
                                    timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                    ME.sendMessage(msg.to, "             🔰 INFO DETAIL GROUP 🔰\n=================================\n⭐•Nama Group : {}".format(G.name)+ "\n⭐•ID Group : \n    {}".format(G.id)+ "\n⭐•Pembuat : {}".format(G.creator.displayName)+ "\n⭐•Waktu Dibuat : \n  {}".format(str(timeCreated))+ "\n⭐•Jumlah Member : {}".format(str(len(G.members)))+ "\n⭐•Jumlah Pending : {}".format(gPending)+ "\n⭐•Group Qr : {}".format(gQr)+ "\n⭐•Group Ticket : {}".format(gTicket)+"\n=================================")
                                    ME.sendMessage(msg.to,"⭐•Kontak Pembuat Group :")
                                    ME.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                    ME.sendMessage(msg.to,"⭐•Goup Cover :")
                                    ME.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                                except: pass
                        
                        if D.startswith("openqr "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                groups = ME.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number)-1]
                                    G = ME.getGroup(group)
                                    if G.preventedJoinByTicket == False:
                                    	pass
                                    else:
                                    	G.preventedJoinByTicket = False
                                    ME.updateGroup(G)
                                    ME.sendMessage(msg.to,"⭐•Sukses Membuka QR...\n\n⭐•Group : "+str(G.name))
                                except: pass
                        if D.startswith("closeqr "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                groups = ME.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number)-1]
                                    G = ME.getGroup(group)
                                    if G.preventedJoinByTicket == True:
                                    	pass
                                    else:
                                    	G.preventedJoinByTicket = True
                                    ME.updateGroup(G)
                                    ME.sendMessage(msg.to,"⭐•Sukses Menutup QR...\n\n⭐•Group : "+str(G.name))
                                except: pass
                        if D.startswith("tunda "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                group = msg.text.replace(separate[0] + " ","")
                                groups = ME.getGroupIdsJoined()
                                try:
                                    GS = groups[int(group)-1]
                                    G = ME.getGroup(GS)
                                    PMB = [contact.mid for contact in G.invitee]
                                    no = 0
                                    ret_ = ""
                                    if PMB == "":
                                        ME.sendMessage(msg.to,"⭐•GROUP : " + str(G.name) + "\n⭐•Pendingan Empty")
                                    for mem in PMB:
                                        GM = ME.getContact(mem).displayName
                                        no += 1
                                        ret_ += "\n "+ str(no) + ". " + GM
                                    ME.sendMessage(msg.to,"🔰 GROUP : " + str(G.name) + "🔰\n═══════════════════════\n PENDING MEMBERS :" + str(ret_ )+ "\n═══════════════════════\n            🔰 TOTAL : %i  ORANG 🔰" % len(G.invitee) + "\n═══════════════════════")
                                except:pass
                        if D.startswith("batal "): 
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                group = str(separate[1])
                                mids = str(separate[2])
                                groups = ME.getGroupIdsJoined()
                                GS = groups[int(group)-1]
                                G = ME.getGroup(GS)
                                GM = [contact.mid for contact in G.invitee]
                                try:
                                    GM2 = GM[int(mids)-1]
                                    GM3 = ME.getContact(GM2).displayName
                                    if GM2 not in D_BOT + D_BOSS + D_GHOST:
                                        random.choice(D_PROTECTOR).cancelGroupInvitation(GS,[GM2])
                                    ME.sendMessage(msg.to, "⭐•REMOTE CANCEL SUKSES_\n\n⭐•Target : "+ GM3 + "_" + "\n⭐•Group  : " + str(G.name) + "_")
                                except: pass
                        if D.startswith("allbatal "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                groups = ME.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    GS = groups[int(number)-1]
                                    G = ME.getGroup(GS)
                                    TRGT = [contact.mid for contact in G.invitee]
                                    for BL in TRGT:
                                    	if BL not in D_BOT + D_BOSS + D_GHOST:
                                    	    random.choice(D_PROTECTOR).cancelGroupInvitation(GS,[BL])
                                    ME.sendMessage(msg.to,"⭐•Sukses Menghapus : " + str(len(TRGT)) + " Pending Invite\n\n⭐•Group : " + str(G.name))
                                except: pass
                        if D == "clean.!!!":
                            if msg._from in D_BOSS:
                                gs = ME.getGroup(msg.to)
                                time.sleep(0.000002)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                if targets == []:
                                    pass
                                else:
                                     for target in targets:
                                         if target not in D_BOT + D_BOSS + D_ADM + D_GHOST + D_STAFF:
                                             POLPP = [H1,H2,H3,H4,H5]
                                             GUSUR = random.choice(POLPP)
                                             GUSUR.kickoutFromGroup(msg.to,[target])
                        if D.startswith("ratakan "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                groups = ME.getGroupIdsJoined()
                                try:
                                    GS = groups[int(number)-1]
                                    gs = ME.getGroup(GS)
                                    time.sleep(0.000002)
                                    targets = []
                                    for g in gs.members:
                                        targets.append(g.mid)
                                    if targets == []:
                                        pass
                                    else:
                                         for target in targets:
                                             if target not in D_BOT + D_BOSS + D_ADM + D_GHOST:
                                                 POLPP = [H1,H2,H3,H4,H5]
                                                 GUSUR = random.choice(POLPP)
                                                 GUSUR.kickoutFromGroup(msg.to,[target])
                                except: pass
                        if D.startswith("rkcall "): 
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                group = str(separate[1])
                                mids = str(separate[2])
                                name = text.replace("rkcall " + str(group) + " ","")
                                groups = ME.getGroupIdsJoined()
                                target = ME.getContact(mids).displayName                            
                                try:
                                    GS = groups[int(group)-1]
                                    gs = ME.getGroup(GS)
                                    ME.sendMessage(msg.to, "🔰 REMOTE SPAMCALL MEMBER 🔰 \n==========================\n⭐•Target Name :\n "+target+"\n⭐•Target Group :\n "+str(gs.name)+"\n===========================")
                                    jmlh = int(D_NILLA["KLIMIT"] )
                                    korban = []
                                    for s in gs.members:
                                	    korban.append(s.mid)                          	
                                    if jmlh <= 10000:
                                        for x in range(jmlh):
                                            if name in korban:
                                                if name not in D_BOT + D_BOSS + D_GHOST:
                                                    ME.inviteIntoGroupCall(GS, [name])
                                        random.choice(D_PROTECTOR).kickoutFromGroup(GS,[name])
                                        ME.sendMessage(msg.to,"⭐•Done")
                                except: pass
                        if D.startswith("rcall "): 
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                group = str(separate[1])
                                mids = str(separate[2])
                                name = text.replace("rcall " + str(group) + " ","")
                                groups = ME.getGroupIdsJoined()
                                target = ME.getContact(mids).displayName                            
                                try:
                                    GS = groups[int(group)-1]
                                    gs = ME.getGroup(GS)
                                    ME.sendMessage(msg.to, "🔰 REMOTE SPAMCALL MEMBER 🔰 \n==========================\n⭐•Target Name :\n "+target+"\n⭐•Target Group :\n "+str(gs.name)+"\n===========================")
                                    jmlh = int(D_NILLA["LIMIT1"] )
                                    korban = []
                                    for s in gs.members:
                                	    korban.append(s.mid)                          	
                                    if jmlh <= 10000:
                                        for x in range(jmlh):
                                            if name in korban:
                                                if name not in D_BOT + D_BOSS + D_GHOST:
                                                    ME.inviteIntoGroupCall(GS, [name])
                                        ME.sendMessage(msg.to,"⭐•Done")
                                        ME.sendMessage(GS, "📲 Spamcall lbh dr 5 kali terdeteksi\n\n📲 Auto back Spam On")
                                except: pass
                        if D.startswith("rinv "): 
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                group = str(separate[1])
                                mids = str(separate[2])
                                name = text.replace("rinv " + str(group) + " ","")
                                groups = ME.getGroupIdsJoined()
                                target = ME.getContact(mids).displayName
                                D_NILLA ["PRO_JOIN"] = False
                                try:
                                    GS = groups[int(group)-1]
                                    gs = ME.getGroup(GS)
                                    ME.findAndAddContactsByMid(name)
                                    H1.findAndAddContactsByMid(name)
                                    H2.findAndAddContactsByMid(name)
                                    H3.findAndAddContactsByMid(name)
                                    H4.findAndAddContactsByMid(name)
                                    H5.findAndAddContactsByMid(name)
                                    if name not in gs.members:
                                        random.choice(D_PROTECTOR).inviteIntoGroup(GS,[name])
                                        ME.sendMessage(msg.to, "⭐•REMOTE INVITE SUKSES_\n\n⭐•Target : "+ target + "_" + "\n⭐•Group  : " + str(gs.name) + "_")
                                except: pass
                        if D.startswith("rkick "): 
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                group = str(separate[1])
                                mids = str(separate[2])
                                groups = ME.getGroupIdsJoined()
                                GS = groups[int(group)-1]
                                G = ME.getGroup(GS)
                                GM = [contact.mid for contact in G.members]
                                try:
                                    GM2 = GM[int(mids)-1]
                                    GM3 = ME.getContact(GM2).displayName
                                    if GM2 not in D_BOT + D_BOSS + D_GHOST:
                                        random.choice(D_PROTECTOR).kickoutFromGroup(GS,[GM2])
                                    ME.sendMessage(msg.to, "⭐•REMOTE KICK SUKSES_\n\n⭐•Target : "+ GM3 + "_" + "\n⭐•Group  : " + str(G.name) + "_")
                                except: pass
                        if D == "assalamualaikum" or D == "assalamu'alaikum" or D == "asalamualaikum" or D == "assalamuallaikum" or D == "assalamuallaikum wr wb" or D == "assalamuallaikum wr.wb" or D == "assalamuallaikum wr.wb.":
                            ME.sendMessage(msg.to, "وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ ")

#=========================================================================================================#
                        if D == "mention" or D == "tagall":
                            if msg._from in D_BOSS + D_ADM + D_STAFF:
                               GR = ME.getGroup(msg.to)
                               nama = [contact.mid for contact in GR.members]
                               nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, nm10, nm11, nm12, nm13, nm14, nm15, nm16, nm17, nm18, jml = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], len(nama)
                               if jml <= 20:
                                   callMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)                                   
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)                                   
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)                                   
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)                                   
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   callMembers(msg.to, nm8)
                               if jml > 160 and jml < 180:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   callMembers(msg.to, nm8)
                                   for q in range (160, len(nama)-1):
                                       nm9+= [nama[q]]
                                   callMembers(msg.to, nm9)
                               if jml > 180 and jml < 200:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   callMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9+= [nama[q]]
                                   callMembers(msg.to, nm9)
                                   for r in range (180, len(nama)-1):
                                       nm10+= [nama[r]]
                                   callMembers(msg.to, nm10)
                               if jml > 200 and jml < 220:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   callMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9+= [nama[q]]
                                   callMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10+= [nama[r]]
                                   callMembers(msg.to, nm10)
                                   for s in range (200, len(nama)-1):
                                       nm11+= [nama[s]]
                                   callMembers(msg.to, nm11)
                               if jml > 220 and jml < 240:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   callMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9+= [nama[q]]
                                   callMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10+= [nama[r]]
                                   callMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11+= [nama[s]]
                                   callMembers(msg.to, nm11)
                                   for t in range (220, len(nama)-1):
                                       nm12+= [nama[t]]
                                   callMembers(msg.to, nm12)
                               if jml > 240 and jml < 260:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   callMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9+= [nama[q]]
                                   callMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10+= [nama[r]]
                                   callMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11+= [nama[s]]
                                   callMembers(msg.to, nm11)
                                   for t in range (220, 240):
                                       nm12+= [nama[t]]
                                   callMembers(msg.to, nm12)
                                   for u in range (240, len(nama)-1):
                                       nm13+= [nama[u]]
                                   callMembers(msg.to, nm13)
                               if jml > 260 and jml < 280:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   callMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9+= [nama[q]]
                                   callMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10+= [nama[r]]
                                   callMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11+= [nama[s]]
                                   callMembers(msg.to, nm11)
                                   for t in range (220, 240):
                                       nm12+= [nama[t]]
                                   callMembers(msg.to, nm12)
                                   for u in range (240, 260):
                                       nm13+= [nama[u]]
                                   callMembers(msg.to, nm13)
                                   for v in range (260, len(nama)-1):
                                       nm14+= [nama[v]]
                                   callMembers(msg.to, nm14)
                               if jml > 260 and jml < 280:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   callMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9+= [nama[q]]
                                   callMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10+= [nama[r]]
                                   callMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11+= [nama[s]]
                                   callMembers(msg.to, nm11)
                                   for t in range (220, 240):
                                       nm12+= [nama[t]]
                                   callMembers(msg.to, nm12)
                                   for u in range (240, 260):
                                       nm13+= [nama[u]]
                                   callMembers(msg.to, nm13)
                                   for v in range (260, len(nama)-1):
                                       nm14+= [nama[v]]
                                   callMembers(msg.to, nm14)
                               if jml > 280 and jml < 300:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   callMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9+= [nama[q]]
                                   callMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10+= [nama[r]]
                                   callMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11+= [nama[s]]
                                   callMembers(msg.to, nm11)
                                   for t in range (220, 240):
                                       nm12+= [nama[t]]
                                   callMembers(msg.to, nm12)
                                   for u in range (240, 260):
                                       nm13+= [nama[u]]
                                   callMembers(msg.to, nm13)
                                   for v in range (260, 280):
                                       nm14+= [nama[v]]
                                   callMembers(msg.to, nm14)
                                   for w in range (280, len(nama)-1):
                                       nm15+= [nama[w]]
                                   callMembers(msg.to, nm15)
                               if jml > 300 and jml < 320:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   callMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9+= [nama[q]]
                                   callMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10+= [nama[r]]
                                   callMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11+= [nama[s]]
                                   callMembers(msg.to, nm11)
                                   for t in range (220, 240):
                                       nm12+= [nama[t]]
                                   callMembers(msg.to, nm12)
                                   for u in range (240, 260):
                                       nm13+= [nama[u]]
                                   callMembers(msg.to, nm13)
                                   for v in range (260, 280):
                                       nm14+= [nama[v]]
                                   callMembers(msg.to, nm14)
                                   for w in range (280, 300):
                                       nm15+= [nama[w]]
                                   callMembers(msg.to, nm15)
                                   for x in range (300, len(nama)-1):
                                       nm16+= [nama[x]]
                                   callMembers(msg.to, nm16)
                               if jml > 320 and jml < 340:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   callMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9+= [nama[q]]
                                   callMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10+= [nama[r]]
                                   callMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11+= [nama[s]]
                                   callMembers(msg.to, nm11)
                                   for t in range (220, 240):
                                       nm12+= [nama[t]]
                                   callMembers(msg.to, nm12)
                                   for u in range (240, 260):
                                       nm13+= [nama[u]]
                                   callMembers(msg.to, nm13)
                                   for v in range (260, 280):
                                       nm14+= [nama[v]]
                                   callMembers(msg.to, nm14)
                                   for w in range (280, 300):
                                       nm15+= [nama[w]]
                                   callMembers(msg.to, nm15)
                                   for x in range (300, 320):
                                       nm16+= [nama[x]]
                                   callMembers(msg.to, nm16)
                                   for y in range (320, len(nama)-1):
                                       nm17+= [nama[y]]
                                   callMembers(msg.to, nm17)
                               if jml > 340 and jml < 360:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   callMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   callMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   callMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   callMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   callMembers(msg.to, nm5)                                   
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   callMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   callMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   callMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9+= [nama[q]]
                                   callMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10+= [nama[r]]
                                   callMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11+= [nama[s]]
                                   callMembers(msg.to, nm11)
                                   for t in range (220, 240):
                                       nm12+= [nama[t]]
                                   callMembers(msg.to, nm12)
                                   for u in range (240, 260):
                                       nm13+= [nama[u]]
                                   callMembers(msg.to, nm13)
                                   for v in range (260, 280):
                                       nm14+= [nama[v]]
                                   callMembers(msg.to, nm14)
                                   for w in range (280, 300):
                                       nm15+= [nama[w]]
                                   callMembers(msg.to, nm15)
                                   for x in range (300, 320):
                                       nm16+= [nama[x]]
                                   callMembers(msg.to, nm16)
                                   for y in range (320, 340):
                                       nm17+= [nama[y]]
                                   callMembers(msg.to, nm17)
                                   for z in range (340, len(nama)-1):
                                       nm18+= [nama[z]]
                                   callMembers(msg.to, nm18)

#=========================================================================================================#
                    if "/ti/g/" in text.lower():
                     if msg._from in D_BOSS:
                        if D_NILLA["JOINLINK"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                LINKQR = ME.findGroupByTicket(ticket_id)
                                ME.acceptGroupInvitationByTicket(LINKQR.id,ticket_id)
                                G = ME.getGroup(LINKQR)
                                if G.preventedJoinByTicket == False:
                                	return
                                else:
                                	G.preventedJoinByTicket = False
                                ME.updateGroup(G)
                                LINK = ME.reissueGroupTicket(LINKQR)
                                for DXX in D_PROTECTOR:
                                    DXX.acceptGroupInvitationByTicket(LINKQR,LINK)
                                if G.preventedJoinByTicket == True:
                                    return
                                else:
                                    G.preventedJoinByTicket = True
                                ME.updateGroup(G)
                                ME.sendMessage(LINKQR,"═════════════════════\n     THIS ROOM PROTECTED BY\n                       ⭐\n         HACKERS INC. TEAM\n═════════════════════")
                                ME.sendMessage(msg.to,"⭐•SUKSES JOIN TO GROUP :\n   " + str(G.name))
                                        

#=========================================================================================================#

        if op.type == 19 or op.type == 32:
            if op.param3 in meMID:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    pass
                else:
                    try:
                        if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                            H1.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H4MID,H5MID])
                            H1.kickoutFromGroup(op.param1,[op.param2])
                            ME.acceptGroupInvitation(op.param1)
                            VICTIM["KICKS"][op.param2] = True
                            addvictim()
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                H2.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H4MID,H5MID])
                                H2.kickoutFromGroup(op.param1,[op.param2])
                                ME.acceptGroupInvitation(op.param1)
                                VICTIM["KICKS"][op.param2] = True
                                addvictim()
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                    H3.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H4MID,H5MID])
                                    H3.kickoutFromGroup(op.param1,[op.param2])
                                    ME.acceptGroupInvitation(op.param1)
                                    VICTIM["KICKS"][op.param2] = True
                                    addvictim()
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                        H4.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H4MID,H5MID])
                                        H4.kickoutFromGroup(op.param1,[op.param2])
                                        ME.acceptGroupInvitation(op.param1)
                                        VICTIM["KICKS"][op.param2] = True
                                        addvictim()
                                except:
                                    try:
                                        if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                            H5.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H4MID,H5MID])
                                            H5.kickoutFromGroup(op.param1,[op.param2])
                                            ME.acceptGroupInvitation(op.param1)
                                            VICTIM["KICKS"][op.param2] = True
                                            addvictim()
                                    except: pass
        
        if op.type == 19 or op.type == 32:
            if op.param3 in H1MID:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    pass
                else:
                    try:
                        if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                            H2.inviteIntoGroup(op.param1,[meMID,H1MID,H3MID,H4MID,H5MID])
                            H2.kickoutFromGroup(op.param1,[op.param2])
                            H1.acceptGroupInvitation(op.param1)
                            VICTIM["KICKS"][op.param2] = True
                            addvictim()
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                H3.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H4MID,H5MID])
                                H3.kickoutFromGroup(op.param1,[op.param2])
                                H1.acceptGroupInvitation(op.param1)
                                VICTIM["KICKS"][op.param2] = True
                                addvictim()
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                    H4.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H5MID])
                                    H4.kickoutFromGroup(op.param1,[op.param2])
                                    H1.acceptGroupInvitation(op.param1)
                                    VICTIM["KICKS"][op.param2] = True
                                    addvictim()
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                        H5.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H4MID])
                                        H5.kickoutFromGroup(op.param1,[op.param2])
                                        H1.acceptGroupInvitation(op.param1)
                                        VICTIM["KICKS"][op.param2] = True
                                        addvictim()
                                except: pass
        
        if op.type == 19 or op.type == 32:
            if op.param3 in H2MID:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    pass
                else:
                    try:
                        if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                            H3.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H4MID,H5MID])
                            H3.kickoutFromGroup(op.param1,[op.param2])
                            H2.acceptGroupInvitation(op.param1)
                            VICTIM["KICKS"][op.param2] = True
                            addvictim()
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                H4.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H5MID])
                                H4.kickoutFromGroup(op.param1,[op.param2])
                                H2.acceptGroupInvitation(op.param1)
                                VICTIM["KICKS"][op.param2] = True
                                addvictim()
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                    H5.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H4MID])
                                    H5.kickoutFromGroup(op.param1,[op.param2])
                                    H2.acceptGroupInvitation(op.param1)
                                    VICTIM["KICKS"][op.param2] = True
                                    addvictim()
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                        H1.inviteIntoGroup(op.param1,[meMID,H2MID,H3MID,H4MID,H5MID])
                                        H1.kickoutFromGroup(op.param1,[op.param2])
                                        H2.acceptGroupInvitation(op.param1)
                                        VICTIM["KICKS"][op.param2] = True
                                        addvictim()
                                except: pass
       
        if op.type == 19 or op.type == 32:
            if op.param3 in H3MID:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    pass
                else:
                    try:
                        if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                            H4.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H5MID])
                            H4.kickoutFromGroup(op.param1,[op.param2])
                            H3.acceptGroupInvitation(op.param1)
                            VICTIM["KICKS"][op.param2] = True
                            addvictim()
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                H5.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H4MID])
                                H5.kickoutFromGroup(op.param1,[op.param2])
                                H3.acceptGroupInvitation(op.param1)
                                VICTIM["KICKS"][op.param2] = True
                                addvictim()
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                    H1.inviteIntoGroup(op.param1,[meMID,H2MID,H3MID,H4MID,H5MID])
                                    H1.kickoutFromGroup(op.param1,[op.param2])
                                    H3.acceptGroupInvitation(op.param1)
                                    VICTIM["KICKS"][op.param2] = True
                                    addvictim()
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                        H2.inviteIntoGroup(op.param1,[meMID,H1MID,H3MID,H4MID,H5MID])
                                        H2.kickoutFromGroup(op.param1,[op.param2])
                                        H3.acceptGroupInvitation(op.param1)
                                        VICTIM["KICKS"][op.param2] = True
                                        addvictim()
                                except: pass
       
        if op.type == 19 or op.type == 32:
            if op.param3 in H4MID:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    pass
                else:
                    try:
                        if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                            H5.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H4MID])
                            H5.kickoutFromGroup(op.param1,[op.param2])
                            H4.acceptGroupInvitation(op.param1)
                            VICTIM["KICKS"][op.param2] = True
                            addvictim()
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                H1.inviteIntoGroup(op.param1,[meMID,H2MID,H3MID,H4MID,H5MID])
                                H1.kickoutFromGroup(op.param1,[op.param2])
                                H4.acceptGroupInvitation(op.param1)
                                VICTIM["KICKS"][op.param2] = True
                                addvictim()
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                    H2.inviteIntoGroup(op.param1,[meMID,H1MID,H3MID,H4MID,H5MID])
                                    H2.kickoutFromGroup(op.param1,[op.param2])
                                    H4.acceptGroupInvitation(op.param1)
                                    VICTIM["KICKS"][op.param2] = True
                                    addvictim()
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                        H3.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H4MID,H5MID])
                                        H3.kickoutFromGroup(op.param1,[op.param2])
                                        H4.acceptGroupInvitation(op.param1)
                                        VICTIM["KICKS"][op.param2] = True
                                        addvictim()
                                except: pass
       
        if op.type == 19 or op.type == 32:
            if op.param3 in H5MID:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    pass
                else:
                    try:
                        if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                            H1.inviteIntoGroup(op.param1,[meMID,H2MID,H3MID,H4MID,H5MID])
                            H1.kickoutFromGroup(op.param1,[op.param2])
                            H5.acceptGroupInvitation(op.param1)
                            VICTIM["KICKS"][op.param2] = True
                            addvictim()
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                H2.inviteIntoGroup(op.param1,[meMID,H2MID,H3MID,H4MID,H5MID])
                                H2.kickoutFromGroup(op.param1,[op.param2])
                                H5.acceptGroupInvitation(op.param1)
                                VICTIM["KICKS"][op.param2] = True
                                addvictim()
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                    H3.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H4MID,H5MID])
                                    H3.kickoutFromGroup(op.param1,[op.param2])
                                    H5.acceptGroupInvitation(op.param1)
                                    VICTIM["KICKS"][op.param2] = True
                                    addvictim()
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                        H4.inviteIntoGroup(op.param1,[meMID,H1MID,H2MID,H3MID,H5MID])
                                        H4.kickoutFromGroup(op.param1,[op.param2])
                                        H5.acceptGroupInvitation(op.param1)
                                        VICTIM["KICKS"][op.param2] = True
                                        addvictim()
                                except: pass
        
        if op.type == 13:
            if op.param3 in VICTIM["KICKS"]:
                if op.param2 in D_BOT + D_BOSS + D_GHOST:
                    pass
                else:
                    try:
                        if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                            H1.cancelGroupInvitation(op.param1,[op.param3])
                            H1.kickoutFromGroup(op.param1,[op.param2])
                            VICTIM["KICKS"][op.param2] = True
                            addvictim()
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                H2.cancelGroupInvitation(op.param1,[op.param3])
                                H2.kickoutFromGroup(op.param1,[op.param2])
                                VICTIM["KICKS"][op.param2] = True
                                addvictim()
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                    H3.cancelGroupInvitation(op.param1,[op.param3])
                                    H3.kickoutFromGroup(op.param1,[op.param2])
                                    VICTIM["KICKS"][op.param2] = True
                                    addvictim()
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                        H4.cancelGroupInvitation(op.param1,[op.param3])
                                        H4.kickoutFromGroup(op.param1,[op.param2])
                                        VICTIM["KICKS"][op.param2] = True
                                        addvictim()
                                except:
                                    try:
                                        if op.param2 not in D_BOT + D_BOSS + D_GHOST:
                                            H5.cancelGroupInvitation(op.param1,[op.param3])
                                            H5.kickoutFromGroup(op.param1,[op.param2])
                                            VICTIM["KICKS"][op.param2] = True
                                            addvictim()
                                    except: pass

#=========================================================================================================#
    except Exception as error:
        logError(error)
        if op.type == 59:
            print (op)
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
    except:
    	pass
#=========================================================================================================#