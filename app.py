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
	newPostForm = web.form.Form(
			web.form.Textbox('title'),
			web.form.Textarea('content'),
			web.form.Checkbox('publish'),
			web.form.Button('post')
			)

	def GET(self):
		np = self.newPostForm()
		return render.admin( np )

	def POST(self):
		np = web.input()
		publish_checkbox = 0;
		if np.has_key('publish'):
			publish_checkbox = 1;
		else:
			publish_checkbox = 0;
		db.insert('posts', title=np.title, content=np.content, author="Kiddi", publish=publish_checkbox )
		raise web.seeother('/new')
		
if __name__ == "__main__": 
    app.run()
