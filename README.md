# 网页生成器

## Quick Start

需要环境: Python 3.7+

需要依赖包: python-markdown-math pygments jinja2

依赖包安装方式:

pip install python-markdown-math pygments jinja2

## 如何使用

### 如何增加文章

将文章存入posts中，在posts.json中posts增加一个条信息。

- id:文章url
- title:文章标题
- description:科目列表中关于文章的描述
- color:科目列表中文章图标颜色
- ico: 科目列表中文章图标
- course:所属科目
- path: 文章存储文件名称

### 如何增加科目

在posts.json中courses增加一条信息

在source/img目录下增加图标

- name:名称
- url:生成网址
- doc:科目介绍
- ico:科目图标

### 如何生成网页

python main.py


PS:
ico可填写值:
ion-ios-analytics-outline
ion-ios-bookmarks-outline
ion-ios-paper-outline
ion-ios-speedometer-outline
ion-ios-world-outline
ion-ios-clock-outline