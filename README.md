# Discord-youtube-live-notify-bot


## 特色
支援一個 Youtube 頻道直播提醒 <br>
發布至 Discord 單一伺服器 `指定文字頻道`<br>


## 準備
1.安裝 Python 3.5 <br>
<br>
2.取得 Youtube Data Api v3 <br> 
<br>
* 使用記事本(notepad.exe)紀錄備用 <br> 
> [Youtube Api 教學](https://developers.google.com/youtube/v3/getting-started)<br> 
<br>
3.取得 Discord Bot token <br>
<br>
* 使用記事本(notepad.exe)紀錄備用<br> 
> [Discord 開發者官網](https://discordapp.com/developers)<br> 
> [Discord Bot 建立及取得 Bot Token 教學](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) <br> 
> Thanks for reactiflux <br>
<br>
4.取得Youtube Channel ID <br> 
<br>
* 使用記事本(notepad.exe)紀錄備用 <br>   
> 頻道所有者應該知道<br> 
> 非頻道所有者就靠<br> 
> [Youtube Channel ID, info and statistics - Comment Picker 這個網站](https://commentpicker.com/youtube-channel-id.php)<br> 

5.取得 Discord 伺服器指定文字頻道 ID <br> 
<br>
* 使用記事本(notepad.exe)紀錄備用<br> 
> 在 Discord 客戶端中啟用開發者模式，以獲得伺服器 ` 指定文字頻道ID `  <br> 
> `使用者設定` -> `外觀` -> 在進階選項中勾選 `開發者模式 ` 來執行此操作<br> 
> 右鍵該文字頻道，然後單擊 ` 複製ID ` ，獲得頻道ID <br> 

6. <br>
## 通知內容格式

預設顯示內容
        
        @everyone
        頻道名稱
        直播主題
        直播網址

