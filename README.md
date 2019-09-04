# Discord-youtube-live-notify-bot


## 特色
支援一個 Youtube 頻道直播提醒 <br>
發布至 Discord 單一伺服器 `指定文字頻道`<br>


## 準備
1.安裝 Python 3.5 或以上版本 <br>
* 開啟命令提示字元(cmd.exe) 輸入 <br>
> python -m pip install -U discord.py <br>
> python -m pip install requests <br>

並在同一目錄下建立locallive.txt<br>
內容預設為<br>

> live_status=0 <br>
>* 若不小心終止機器人,狀態會保持在最後一次取得,特別注意


<br>
2.取得 Youtube Data Api Key  <br> 
<br>

* 使用記事本(notepad.exe)紀錄備用 <br> 

> [Youtube Api 教學](https://developers.google.com/youtube/v3/getting-started)<br> 

<br>
3.取得 Discord Bot token <br>
<br>

* 使用記事本(notepad.exe)紀錄備用 <br> 

> [Discord 開發者官網](https://discordapp.com/developers)<br> 
> [Discord Bot 建立及取得 Bot Token 教學](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) <br> 
> Thanks for reactiflux <br>

<br>
4.取得Youtube Channel ID <br> 
<br>

* 使用記事本(notepad.exe)紀錄備用<br>

> 頻道所有者應該知道<br> 
> 非頻道所有者就靠下面這個網站<br> 
> [Youtube Channel ID, info and statistics - Comment Picker ](https://commentpicker.com/youtube-channel-id.php)<br> 

5.取得 Discord 伺服器指定文字頻道 ID <br> 
<br>

* 使用記事本(notepad.exe)紀錄備用<br> 

> 在 Discord 客戶端中啟用開發者模式，以獲得伺服器 ` 指定文字頻道ID `  <br> 
> `使用者設定` -> `外觀` -> 在進階選項中勾選 `開發者模式 ` 來執行此操作<br> 
> 右鍵該文字頻道，然後單擊 ` 複製ID ` ，獲得頻道ID <br> 

6. <br>

## 通知內容格式

預設開播通知顯示內容 <br> 
        
        @everyone
        頻道名稱
        直播主題
        直播網址

預設結束直播通知 <br> 

        Stream is off ,thank you for your watching

## 修改項

更改 Youtube channel id & Youtube Data Api Key & Discord 伺服器指定文字頻道ID & Discord Bot token <br>

```python
17 'channelId' : 'YOUTBUE CHANNEL ID'
20 'key' : 'YOUTUBE DATA API KEY' 
38         channel = client.get_channel(COPY DISCORD CHANNEL ID)
130  client.run('DISCORD BOT TOKEN')
```



## 執行
點擊兩下 discord youtube live notify bot .py 執行 <br> 
