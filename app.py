import web

urls = (
    '/', 'index',
    '/new', 'new'
)

app = web.application( urls, globals() )
render = web.template.render('templates/', base='base')
db = web.database(dbn='mysql', db='kBlog', user='kiddi', pw='beholder')

class index(object):
    def GET(self):
    	items = db.select('posts')
        return render.index(items)

class new(object):	
	def GET(self):
		newPostForm = web.form.Form(
			web.form.Textbox('title'),
			web.form.Textarea('content'),
			web.form.Checkbox('publish'),
			web.form.Button('Post')
			)
		np = newPostForm()
		return render.admin( np )

	def POST(self):
		return "duuuude"

if __name__ == "__main__": 
    app.run()
