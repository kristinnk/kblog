import web

urls = (
    '/', 'index',
    '/singlepost/(\d+)', 'singlepost',
    '/admin', 'admin',
    '/new', 'new',
    '/edit/(\d+)', 'edit',
    '/edit', 'edit',
    '/delete/(\d+)', 'confirmdelete',
    '/dodelete/(\d+)', 'performdelete',
    '/login', 'login',
    '/logout', 'logout'
)

web.config.debug = False
app = web.application( urls, globals() )
render = web.template.render('templates/', base='base')
db = web.database(dbn='mysql', db='kBlog', user='kiddi', pw='beholder')
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'username': 'none'})

def authenticate():
	if session.username == "kiddi":
		web.debug( session.username )
		pass
	else:
		web.debug("authenticate failed")
		raise web.seeother('/login')

class index(object):
    def GET(self):
    	items = db.select('posts')
        return render.index(items)

class singlepost(object):
	def GET(self, id_number):
		item = db.select('posts', where='id=$id_number', vars=locals())
		return render.singleitem(item[0])

class admin(object):
	def GET(self):
		authenticate()
		items = db.select('posts')
		return render.admin(items, session)


class confirmdelete(object):
	def GET(self, id_number):
		authenticate()
		return render.confirm(id_number)


class performdelete(object):
	def GET(self, id_number):
		db.delete('posts', where="id=$id_number", vars=locals())
		raise web.seeother('/admin')


class login(object):
	loginForm = web.form.Form(
		web.form.Textbox('username'),
		web.form.Password('password'),
		web.form.Button('Log in')
		)

	def GET(self):
		li = self.loginForm()
		return render.login( li )

	def POST(self):
		li = web.input()
		user = db.select('users', where='username=$li.username and password=$li.password', vars=locals())
		if user:
			# return user[0].username
			session.username = user[0].username
			web.debug("found, setting session")
			raise web.seeother('/admin')
		else:
			web.debug("not found")
			raise web.seeother('/login')
		

class logout(object):
	def GET(self):
		session.kill()
		raise web.seeother('/')


class new(object):
	postForm = web.form.Form(
		web.form.Textbox('title'),
		web.form.Textarea('content'),
		web.form.Checkbox('publish'),
		web.form.Button('post')
		)

	def GET(self):
		authenticate()
		np = self.postForm()
		return render.new( np )

	def POST(self):
		np = web.input()
		publish_checkbox = 0;
		if np.has_key('publish'):
			publish_checkbox = 1;
		else:
			publish_checkbox = 0;
		db.insert('posts', title=np.title, content=np.content, author="Kiddi", publish=publish_checkbox )
		raise web.seeother('/admin')


class edit(object):
	postForm = web.form.Form(
			web.form.Textbox('id', class_='disabledInput'),
			web.form.Textbox('title'),
			web.form.Textarea('content'),
			web.form.Checkbox('publish'),
			web.form.Button('post')
			)

	def GET(self, id_number):
		authenticate()
		item = db.select('posts', where='id=$id_number', vars=locals())
		ep = self.postForm()
		ep.fill( item[0] )
		return render.edit( ep )
		
	def POST(self):
		np = web.input()
		if np.has_key('publish'):
			publish_checkbox = 1;
		else:
			publish_checkbox = 0;
		db.update('posts', where="id=$np.id", vars=locals(), title=np.title, content=np.content, author="Kiddi", publish=publish_checkbox )
		raise web.seeother('/admin')


if __name__ == "__main__": 
    app.run()
