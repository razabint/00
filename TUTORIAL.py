# -*- coding: utf-8 -*-
#HIT TEAM PRO BOT
#VERSI        = SELFPLUS (REMOTE FULL)
#CREATOR  = BINTANG
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
print ("=============================================================\n                  HIT AUTO PROTECT BOT LINE\n                       CREATOR : DEDE\n                    HIT TEAM PRO BOTBOT\n════════════════════════════════=====================")
print ("===========[ HACKERS AUTO PROTECT BOT LOGIN START]===========")
ME = LINE('rdtrzxe@mail-fix.com','Lovers1978!')
print ("=============================================================")
print ("\n[ HIT AUTO PROTECT BOT START ]")
#=============================================================#
oepoll = OEPoll(ME)
meProfile = ME.getProfile()
meSettings = ME.getSettings()
mid = ME.profile.mid
meMID = ME.getProfile().mid
D_BOT = [meMID]
D_BOTS = [ME]
#=============================================================#
D_CREATOR = ["u38cbb60440251cd61c2e94efd715b181","u303c4c390bf00f81fcf1affe14f3779a","u9a8dfc80fb5eace4f194c67bb8145755","u1c1cf9010da4a0aad1be6b3446a63696"]
D_BOSS = ["u476a7fff0047468c903705a348ab8111"]
#=============================================================#
for CREATOR in D_CREATOR:
	try:
		ME.findAndAddContactByMid(CREATOR)
	except: pass

D_SELFBOT = """╭━━━━━━━━━━━━━━━━━━━━━╮
┃  HACKERS PROFESIONAL TEAM BOT
┃                BOT TUTORIAL
┣•━━━━━━━━━━━━━━━━━━━━━
┃           📲• MAIN COMMAND•📲
┣•━━━━━━━━━━━━━━━━━━━━━
┣• 📲•  /tutorial
┣• 📲•  /self
┃
┣•━━━━━━━━━━━━━━━━━━━━━
┃    ▶️• GANTI PHOTO PROFILE •▶️
┣•━━━━━━━━━━━━━━━━━━━━━
┣• ▶️•  /up
┣• ▶️•  /up video
┣• ▶️•  /upvp
┣• ▶️•  /pp3
┃
┣•━━━━━━━━━━━━━━━━━━━━━
┃            ▶️• REMOTE CMD •▶️
┣•━━━━━━━━━━━━━━━━━━━━━
┣• ▶️•  /remote
┣• ▶️•  /tagall
┣• ▶️•  /kill
┣• ▶️•  /sideron
┣• ▶️•  /clone
┣•━━━━━━━━━━━━━━━━━━━━━
┃   •> CREATOR : BINTANG
┃   •> line.me/ti/p/~__me___
┃   •> WA : +6281333833838
╰━━━━━━━━━━━━━━━━━━━━━╯"""

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
🎲 Login Via sertifikat
      - No Link / Token
      - Sekali login selamanya
🎲 Gratis Upgrade Menu Bot
🎲 Akun Asist Bisa Kami sediakan
━━━━━━━━━━━━━━━━━━━━━━
📵 LINE : line.me/ti/p/~__me___
📵 WA   : +6281333833838
━━━━━━━━━━━━━━━━━━━━━━"""

#=============================================================#
mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
msg_dict = {}
temp_flood = {}
D_NILLA = {
    "KUNCI": False,
    "PERINTAH": "",
    "ADDMESS": True,
    "AUTO_REJECT": True
    
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
#=============================================================#

def restartBot():
    print ("[I N F O] BOT RESTARTED\n")
    time.sleep(1)
    python = sys.executable
    os.execl(python, python, *sys.argv)
def waktu(secs):
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
    time = hasil + ", "+ inihari.strftime('%d') + "- "+ bln + "- "+ inihari.strftime('%Y') + "| "+ inihari.strftime('%H:%M:%S')
    with open("serverBug.txt","a") as error:
        error.write("\n[%s] %s"% (str(time), text))
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
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
def callMembers(to, mid):
    try:
        arrData = ""
        textx = "             [° MENTION MEMBER °]\n══════════════════════\n 1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            if i not in D_CREATOR:
                mention = "@Bintang\n"
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
        mention = "@Bintang"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ME.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        ME.sendMessage(to, "[ INFO ] Error :\n" + str(error))
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
                ME.sendMessage(op.param1, str(D_PROMO))
                search_url="https://youtu.be/WGLdsA1x2gk"
                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                vid = pafy.new(search_url)
                stream = vid.streams
                best = vid.getbest()
                best.resolution, best.extension
                for s in stream:
                	see = best.url
                vin = s.url
                ME.sendVideoWithURL(op.param1, see)
        if op.type == 13:
            if meMID in op.param3:
                if D_NILLA["AUTO_REJECT"] == True:
                    if op.param2 in D_CREATOR:
                        ME.acceptGroupInvitation(op.param1)
                    if op.param2 not in D_CREATOR:
                        try:
                            ME.rejectGroupInvitation(op.param1)
                        except: 
                            try:
                                ME.acceptGroupInvitation(op.param1)
                                ME.leaveGroup(op.param1)
                            except: pass
#=======================[ SELFBOT ONLY COMMAND ]=======================#
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType in [2,1,0]:
                if msg.toType == 0:
                    if sender != ME.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        D = command(text)
                        if D == "assalamualaikum" or D == "assalamu'alaikum" or D == "asalamualaikum" or D == "assalamuallaikum" or D == "assalamuallaikum wr wb" or D == "assalamuallaikum wr.wb" or D == "assalamuallaikum wr.wb.":
                            ME.sendMessage(msg.to, "وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ ")
                        if D == "cek" or D == "bot":
                            if msg._from in D_CREATOR:
                               eltime = time.time() - mulai
                               ME.sendMessage(msg.to,"📲 HIT TUTIRIAL_BOT On\n      "+waktu(eltime))
                        if D == "bot out":
                            if msg._from in D_CREATOR:
                                ME.leaveGroup(msg.to)
                        if D == "all reset" or D == "bot reset":
                            if msg._from in D_CREATOR:
                               ME.sendMessage(msg.to,"📲 HIT TUTIRIAL_BOT Resetted")
                               restartBot()
                        if D == "/tutorial":
                            ME.sendMessage(msg.to, str(D_SELFBOT))
                            ME.sendMessage(msg.to, "📲 Ketik Sesuai yg tertulis di Menu.!!!\n\n📲 Jangan Lupa Awali dg GARIS MIRING /")
                        if D == "/self":
                            search_url="https://youtu.be/jZLdBeKpAIc"
                            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                            vid = pafy.new(search_url)
                            stream = vid.streams
                            best = vid.getbest()
                            best.resolution, best.extension
                            for s in stream:
                            	me = best.url
                            vin = s.url
                            ME.sendMessage(msg.to,"👉•Penjelasan Menu .SELF\n\n👉•Simak Videonya Sampai Selesai.!!!")
                            ME.sendVideoWithURL(msg.to, me)
                            search_url2="https://youtu.be/i14irfCL_jw"
                            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                            vid = pafy.new(search_url2)
                            stream = vid.streams
                            best = vid.getbest()
                            best.resolution, best.extension
                            for s in stream:
                            	me2 = best.url
                            vin = s.url
                            ME.sendVideoWithURL(msg.to, me2)
                        if D == "/up":
                            search_url="https://youtu.be/bGmLfybA3UA"
                            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                            vid = pafy.new(search_url)
                            stream = vid.streams
                            best = vid.getbest()
                            best.resolution, best.extension
                            for s in stream:
                            	me = best.url
                            vin = s.url
                            ME.sendMessage(msg.to,"👉•Cara ganti Foto PP\n\n👉•Simak Videonya Sampai Selesai.!!!")
                            ME.sendVideoWithURL(msg.to, me)
                        if D == "/up video":
                            search_url="https://youtu.be/LaTHs7Z1Qi4"
                            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                            vid = pafy.new(search_url)
                            stream = vid.streams
                            best = vid.getbest()
                            best.resolution, best.extension
                            for s in stream:
                            	me = best.url
                            vin = s.url
                            ME.sendMessage(msg.to,"👉•Cara ganti pp menggunakan video sendiri-1\n\n👉•Simak Videonya Sampai Selesai.!!!")
                            ME.sendVideoWithURL(msg.to, me)
                        if D == "/upvp":
                            search_url="https://youtu.be/7Z1si53DZWc"
                            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                            vid = pafy.new(search_url)
                            stream = vid.streams
                            best = vid.getbest()
                            best.resolution, best.extension
                            for s in stream:
                            	me = best.url
                            vin = s.url
                            ME.sendMessage(msg.to,"👉•Cara ganti pp menggunakan video dr youtube\n\n👉•Simak Videonya Sampai Selesai.!!!")
                            ME.sendVideoWithURL(msg.to, me)
                        if D == "/pp 3":
                            search_url="https://youtu.be/fwCQW2vJ1xY"
                            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                            vid = pafy.new(search_url)
                            stream = vid.streams
                            best = vid.getbest()
                            best.resolution, best.extension
                            for s in stream:
                            	me = best.url
                            vin = s.url
                            ME.sendMessage(msg.to,"👉•Cara ganti pp menggunakan video sendiri-2\n\n👉•Simak Videonya Sampai Selesai.!!!")
                            ME.sendVideoWithURL(msg.to, me)
                        if D == "/remote":
                            search_url="https://youtu.be/Lkr0lLuPeJ0"
                            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                            vid = pafy.new(search_url)
                            stream = vid.streams
                            best = vid.getbest()
                            best.resolution, best.extension
                            for s in stream:
                            	me = best.url
                            vin = s.url
                            ME.sendMessage(msg.to,"👉•Penjelasan Remote CMD - 1\n\n👉•Simak Videonya Sampai Selesai.!!!")
                            ME.sendVideoWithURL(msg.to, me)
                        if D == "/tagall":
                            search_url="https://youtu.be/90J05WYu1Fk"
                            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                            vid = pafy.new(search_url)
                            stream = vid.streams
                            best = vid.getbest()
                            best.resolution, best.extension
                            for s in stream:
                            	me = best.url
                            vin = s.url
                            ME.sendMessage(msg.to,"👉•Mention/Tagall menggunakan Remote \n\n👉•Simak Videonya Sampai Selesai.!!!")
                            ME.sendVideoWithURL(msg.to, me)
                        if D == "/kill":
                            search_url="https://youtu.be/fPyA-2hnF6g"
                            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                            vid = pafy.new(search_url)
                            stream = vid.streams
                            best = vid.getbest()
                            best.resolution, best.extension
                            for s in stream:
                            	me = best.url
                            vin = s.url
                            ME.sendMessage(msg.to,"👉•Cara Kill/Freeze PM\n\n👉•Simak Videonya Sampai Selesai.!!!")
                            ME.sendVideoWithURL(msg.to, me)
                        if D == "/sideron":
                            search_url="https://youtu.be/3ip4EWsutMU"
                            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                            vid = pafy.new(search_url)
                            stream = vid.streams
                            best = vid.getbest()
                            best.resolution, best.extension
                            for s in stream:
                            	me = best.url
                            vin = s.url
                            ME.sendMessage(msg.to,"👉•Cara Aktifin Sider Via Remote\n\n👉•Simak Videonya Sampai Selesai.!!!")
                            ME.sendVideoWithURL(msg.to, me)
                        if D == "/clone":
                            search_url="https://youtu.be/E1S0D7dTh4I"
                            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                            vid = pafy.new(search_url)
                            stream = vid.streams
                            best = vid.getbest()
                            best.resolution, best.extension
                            for s in stream:
                            	me = best.url
                            vin = s.url
                            ME.sendMessage(msg.to,"👉•Cara Cloning Profile Org Lain\n\n👉•Simak Videonya Sampai Selesai.!!!")
                            ME.sendVideoWithURL(msg.to, me)
                        
                        
                        

#=============================================================================#

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
    except Exception as e:
        ME.log("[SINGLE_TRACE] ERROR : " + str(e))