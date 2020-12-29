# Django3视频教程的代码
![Python3.x](https://img.shields.io/badge/Python-3.x-519dd9.svg)
![Django3.x](https://img.shields.io/badge/Django-3.x-519dd9.svg)

**版权声明：该套教程版权是作者（杨仕航）所有，侵权必究。**

该git项目是Django3视频教程对应每节课的代码。为了查看方便，对应章节代码在对应文件夹中。<br>
Django3视频教程地址：https://space.bilibili.com/252028233/channel/detail?cid=125207

## 公告 2020-12-29 23:59
大家好，我是杨仕航。<br>
这大半年来我一直想好好把教程录制下去。这期间我挣扎过、无奈、焦虑。事实上，我无法腾出时间录制。<br>
疫情之后，我就开始走上创业的道理。从外包到合伙创业，基本精力都投入在事业上。<br>
创业非比就业，需要把全部精力都投入才行。<br>
无以为继。目前教程关键的后续代码，在“后续代码”的目录里面。<br>
<br>
不管你年龄几何，无论你是否学过编程，只要付出努力，在对的思想和思考方法指引下，总会成长和收获！大家好好加油！

## 如何使用
该git项目主要是提供一个可对照的代码给大家。每个文件夹对应每节课的代码。<br>
大家自己一定要先把代码敲一遍，消化理解，以加深印象。

#### 1、Python
Django是Python的一种web框架，需要Python才可使用。<br>
本教程使用Python3.8的版本录制，建议使用Python3.x最新版本。<br>
可打开[Python官网](https://www.python.org/downloads/)下载并安装。

#### 2、虚拟环境
本课程用virtualenv，你也可以使用其他虚拟环境管理Python库。

#### 3、一键安装库（包含Django）
每次课的代码文件夹都有一个requirments.txt文件。该文件是记录所使用库的信息。可利用该文件直接一键安装所有库。<br>
启动虚拟环境之后（若有使用虚拟环境的的话），进入requirments.txt所在的目录，执行命令：<br>
```pip install -r requirements.txt```

#### 4、启动本地服务
普通启动：进入项目根目录，执行命令：```python manage.py runserver```<br>
ASGI启动：使用Daphne启动，执行命令：```daphne mysite.asgi:application```<br>

## 教程目录
01.什么是Django<br>
02.Django是如何工作的<br>
03.开始项目构思<br>
04.本地简单登录<br>
05.初步搭建主界面<br>
06.建立WebSocket连接<br>
07.创建人与人聊天的机制<br>

## 交流
**QQ群：701914136**<br>
**公众号：再敲一行代码**<br>
**官网：https://zqyhdm.com**
