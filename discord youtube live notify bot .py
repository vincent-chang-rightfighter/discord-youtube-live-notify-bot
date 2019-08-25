import discord
from discord.ext import commands
import time
import datetime
import asyncio
import requests
import json
import sys
import os

client = commands.Bot(command_prefix = '?')
pingEveryXMinutes = 6  #5~10 minute is best a few delay
live_status = 2 # Preset status
#Youtube data api payload
payload = {
    'part' : 'snippet',
    'channelId' : 'YOUTBUE CHANNEL ID',
    'type' : 'video',
    'eventType' : 'live',
    'key' : 'YOUTUBE DATA API KEY',
    'maxResults': 50
}

@client.event
async def on_ready():
    #------------------------------------------------------------------------------------
    while True:
        dateEvent = ((datetime.datetime.utcnow())+datetime.timedelta(hours=8))# utc+8 taiwan time zone
        dateEventStr = dateEvent.strftime("%Y-%m-%d %H:%M:%S")
        print('Logged on as:',client.user,'is online.')#use # Choose not to display
        print('----------------------------------')#use # Choose not to display
        #print bot name and command log
        print('First Time run Program :',dateEventStr)#use # Choose not to display
        print('Log')#use # Choose not to display
        print('----------------------------------')#use # Choose not to display
        dateNow = ((datetime.datetime.utcnow())+datetime.timedelta(hours=8))# utc+8 taiwan time zone
        dateNowStr = dateNow.strftime("%Y-%m-%d %H:%M:%S")
        channel = client.get_channel(COPY DISCORD CHANNEL ID)
        #---------------------------------------------------------------------------
        # countdown in cmd
        #---------------------------------------------------------------------------
        print(dateNowStr,'waittime')
        waittime = pingEveryXMinutes * 60
        while waittime > 0:
            m, s = divmod(waittime, 60)
            time_left = str(m).zfill(2) + ":" + str(s).zfill(2)
            print (time_left + "\r",end="")
            waittime -= 1
            time.sleep(1)
        print('\n')
        print('waittime finish ') # use # Choose not to display
        readlocal=open("locallive.txt", "r") #read local txt to import local_live value
        reader_local=readlocal.read(14)
        #print(readfile)
        local_live =int(reader_local.split("=", 1)[1]) #string to int
        print(local_live)
        #初始化
        print('Detecting~')#use # Choose not to display
        #------------------------------------------------------------------------------
        #Detect
        #------------------------------------------------------------------------------
        r = requests.get('https://www.googleapis.com/youtube/v3/search', params = payload).json()
        try:
            info = r["items"][0]["snippet"]["liveBroadcastContent"]
        except:
            ## no live
            live_status = 0
            print('NO STREAM NOW')#use # Choose not to display
            print('---------------------------------------------------')#use # Choose not to display
        else:
            ## live now
            if info == "live":
                live_status = 1
                print('STREAMING NOW')#use # Choose not to display
                print('---------------------------------------------------')#use # Choose not to display
        #----------------------------------------------------------------------------
        # local_live == live_status -> do nothing
        #----------------------------------------------------------------------------
        if local_live == live_status:
            if live_status == 1:
                print('local_live == live_status==1')# use # Choose not to display
                print('---------------------------------------------------')# use # Choose not to display
            elif live_status == 0:
                print('local_live == live_status==0')# use # Choose not to display
                print('---------------------------------------------------')# use # Choose not to display
        #------------------------------------------------------------------------------
        #local_live != live_status  ->
        #------------------------------------------------------------------------------
        elif local_live != live_status:
        #------------------------------------------------------------------------------
        #send stream on message,local_live=1
        #------------------------------------------------------------------------------
            if live_status == 1:
                #local_live = 1
                file2=open("locallive.txt", "w")
                str2="live_status=1"
                file2.write(str2)
                print("change locallive.txt :",str2)#use # Choose not to display
                file2.close()
                dateOn = ((datetime.datetime.utcnow())+datetime.timedelta(hours=8)) # utc+8 taiwan time zone
                dateOnStr = dateOn.strftime("%Y-%m-%d %H:%M:%S")
                url='https://www.youtube.com/watch?v='+ r["items"][0]["id"]["videoId"]
                send_text_start = '@everyone \n```' + r["items"][0]["snippet"]["channelTitle"] + '\n' + r["items"][0]["snippet"]["title"] +'```\n'
                plus_send_text_start = send_text_start + url
                await channel.send(plus_send_text_start)
                print(dateOnStr,'sending online message ')#use # Choose not to display
                print('----------------------------------')#use # Choose not to display
        #-------------------------------------------------------------------------------
        #send stream off message,local_live=0
        #------------------------------------------------------------------------------
            elif live_status == 0: #send stop  live message,local_live=0,clock_down
                #local_live = 0
                file3=open("locallive.txt", "w")
                str3="live_status=0"
                file3.write(str3)
                print("change locallive.txt :",str3)#use # Choose not to display
                file3.close()
                #clock_down
                dateEnd = ((datetime.datetime.utcnow())+datetime.timedelta(hours=8)) # utc+8 taiwan time zone
                dateEndStr = dateEnd.strftime("%Y-%m-%d %H:%M:%S")
                send_text_stop ='```stream is off ,thank you for your watching ~~```\n'
                await channel.send(send_text_stop)
                print(dateEndStr,'sending offline message ')#use # Choose not to display
                print('----------------------------------')#use # Choose not to display
        #-------------------------------------------------------------------------------
        openfile.close()

client.run('DISCORD BOT TOKEN')
#========================================================
#version
#20190820 remove clock item & delete personal token , keys, id
#20190821 change language
#========================================================
