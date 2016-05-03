# BusTrackerTaipeiAppiumTesting

### Installation
#### 安裝chocolatey

``` bash
@powershell -NoProfile -ExecutionPolicy Bypass -Command “iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))” && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin

choco install jdk8
choco install android-sdk
choco install ant
```
以下兩個指令官方或許沒有完全維護
安裝Python建議從官方網站下載python3
``` bash
choco install python
choco install pip
```

記得先加上python環境變數
Python\Python35-32
Python\Python35-32\Scripts

``` bash
pip install Appium-Python-Client
```
#### 設定環境變數

JAVA_HOME = jdk位置
ANT_HOME=C:\ProgramData\chocolatey\lib\ant
ANDROID_HOME= android sdk 位置

PATH=

	* AndroidSDK\sdk\tools
	* AndroidSDK\sdk\platform-tools
	* Java\jdk1.8.0_45\bin
	* apache-ant-1.9.7\bin






pip install Appium-Python-Client

Appium設定成下列的樣子
![](http://i.imgur.com/9y0yAty.png)






