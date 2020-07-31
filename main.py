# -*- encoding: utf-8 -*-
# uncle-lu

import os
import json
import shutil
import markdown
from mdx_math import MathExtension
from jinja2 import Environment, PackageLoader, select_autoescape


def make_all_html(courses, set_course, posts):

    # 创建目录
    pwd = os.getcwd()
    __pwd = os.path.join(pwd, "html")
    postwd = os.path.join(__pwd, "posts")
    if not os.path.exists(__pwd):
        os.mkdir(__pwd)
    if not os.path.exists(postwd):
        os.mkdir(postwd)
    if not os.path.exists(os.path.join(__pwd, "source")):
        shutil.copytree("source", os.path.join(__pwd, "source"))
    else:
        shutil.rmtree(os.path.join(__pwd, "source"))
        shutil.copytree("source", os.path.join(__pwd, "source"))

    # 引用jinja类
    env = Environment(
        loader=PackageLoader(__name__, "template"),
        auto_reload=select_autoescape(['html'])
    )
    index_template = env.get_template("index.html")
    list_template = env.get_template("list.html")
    post_template = env.get_template("post.html")

    # 渲染主页
    html = index_template.render(courses = courses)
    f = open(os.path.join(__pwd,"index.html"), "w", encoding="utf-8")
    f.write(html)

    # 渲染列表
    for i in courses:
        html = list_template.render(title = i["name"], posts = set_course[ i["name"] ])
        f = open(os.path.join(__pwd, str(i["url"]) + ".html"), "w", encoding="utf-8")
        f.write(html)

    # 渲染文章
    for i in posts:
        html = post_template.render(title = i["title"], content = i["content"])
        f = open(os.path.join(postwd, str(i["url"]) + ".html"), "w", encoding="utf-8")
        f.write(html)



def read_posts(post_info, courses):
    # 垃圾方式创建course集合list
    tags_archives={}
    for i in courses:
        tags_archives[i["name"]] = []
    posts = []

    for p in post_info:
        post_file = open(os.path.join(os.getcwd(), "posts", p["path"]), "r", encoding="utf-8").read()
        md = markdown.Markdown(extensions=[MathExtension(enable_dollar_delimiter=True), 'fenced_code', 'footnotes', 'tables', 'toc'])

        temp = { "title" : p["title"], "url": p["id"] , "description" : p["description"], "color" : p["color"], "ico" : p["ico"] }
        tags_archives[p["course"]].append(temp);
        
        temp = { "title" : p["title"], "url": p["id"], "content": md.convert(post_file)}
        posts.append(temp)

    return tags_archives, posts
        

if __name__ == "__main__":
    print("Start work\n")
    file_post = open(os.path.join(os.getcwd(), "post.json"), "r", encoding="utf-8").read()

    setting = json.loads(file_post) # 通过json将信息读取到setting中
    courses = setting["courses"]; # 提取课程的属性
    post_info = setting["posts"]; # 提取文章的属性

    # set_course 课程对应的文章的集合
    # posts 每篇文章的属性, 包括内容
    set_course, posts = read_posts(post_info, courses) 

    make_all_html(courses, set_course, posts)