# Simple Fumo Alarm Clock

## 简介 Introduction

这是一个本人自己写自己用的语音提醒闹钟。做这个小型应用的目的是：自己总是投入一件事情不能自拔，导致吃饭睡觉都经常被耽误，需要一个闹钟来提醒自己。我感觉用fumo的声音（油库里音）来提醒自己应该非常有意思，就仿佛自己养的fumo跑过来拍我叫我吃饭睡觉。

This is a voice alarm clock. The objective is: I need an alarm clock to remind me. Because I always delay my sleeping and eating due to paying too much attention to working or learning. I feel it should be very interesting to remind me by using the Fumo's voice (Yukuri's voice). It feels like my own Fumo runs to me, pats me, and reminds me to eat or sleep.

我不想在这个上面花太多时间。所以它只有很简单的功能，界面也只有一个右下角托盘图标和菜单。

I do not want to use too much time on this. Thus, its function is very simple, and the interface only contains a tray icon and a menu.

## 如何使用 How To Use

打开fumo\_alarm.exe，在屏幕右下角的托盘区会有一个灵梦fumo图标出现，说明成功打开，一直挂着就可以。

Open fumo\_alarm.exe. A tray icon with Reimu Fumo's face will appear, which means you opened it successfully. You can just leave it there.

你可以在config那个csv文件里指定每天的固定闹铃时间，以及要播放的声音。文件里的年月日是无效的，随便填数字就行，声音是每天播放的。留着年月日是为了方便以后修改。这里图省事用的playsound播放音频，因此声音文件名称最好是英文。你也可以自己制作自己的fumo语音，放到sound文件夹里。在更新过config之后需要手动重新打开应用使修改生效。

You can set the time and sound for the alarm clock in the config.csv. Year, Month, and Day are invalid, actually. The sound will play for everyday. I just left Year, Month, and Day for future use. Because "playsound" is used here, it is better to use English names for your own sounds. You can make and use your sound, and then put them into "sound" folder. You need to restart the application manually after modifying the "config" file.

只是用油库里的声音替代闹铃就太无聊了，于是我加了一个小小的互动选项在托盘图标的右键菜单里。点击抚摸fumo会发出fumofumo的声音（三种声音随机播放）。声音在random文件夹里。

Simply using Yukuri's voice as an alarm sound is a little boring. So I added an option in the right-click menu to interact with Fumo. Click "抚摸fumo"(touch fumo), and it will play three kinds of sounds randomly. These sounds are in the "random" folder.

## Python版本及依赖 Python and Dependencies

|python|3.12.12|
|:---|:---|
|pillow|12.1.1|
|playsound|1.3.0|
|pystray|0.19.5|

为了方便正常运行，playsound.py中第55行被修改过。

Line 55 in playsound.py has been modified to ensure successful running.

## 参考 Reference

图标收集自(Icon collected from)：[Fumo List](https://fumo.website/fumo_list.html)

声音生成自(Sounds generated from)：[Yukumo!](https://www.yukumo.net/#/)

本应用由粉丝创作，与东方Project官方、上海爱丽丝幻乐团、Gift公司无直接关联。所有角色版权归属ZUN/Gift。

This application is a fan creation and is not directly affiliated with the official Touhou Project, Team Shanghai Alice, or Gift. All character rights belong to ZUN / Gift.
