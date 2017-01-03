# -*- coding:utf-8 -*-

import web

# 到模板目录中查找模板
render = web.template.render('templates/')

urls = (
    '/', 'index'
)


class index:
    def GET(self):
        i = web.input(name=None)
        return render.index(i.name)


if __name__=="__main__":
    app = web.application(urls, globals())
    app.run()