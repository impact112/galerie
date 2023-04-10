
from routes.common import *
from routes.forms import SearchForm
from routes import app
from database import *


@app.route('/search', methods=['GET', 'POST'])
async def search_route():
    form = SearchForm(await request.form)
    tags = dbsession.query(Tag).all()
    if request.method == 'GET':
        return await render_template('search.html', form=form, tags=tags)
    else:
        pass
