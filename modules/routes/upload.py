
from routes.common import *
from routes import app
from auth import *
from forms import Form, Field
import forms.validators as validators

class UploadForm( Form ):
    
    title = Field( 
        name = 'title', 
        label = 'Post title:',
        validators = [ validators.NotEmpty() ]
    )
    
    description = Field( 
        name = 'description', 
        label = 'Post description:',
        validators = []
    )

    tags = Field( 
        name = 'tags', 
        label = 'Post tags:',
        validators = [ validators.NotEmpty() ]
    )

    file = Field(
        name = 'file',
        label = 'Image file:',
        type = 'file',
        validators = [ validators.NotEmpty() ]
    )
    

def string_to_tags( s: str ) -> list:
    res:list = []
    for tag_name in s.split():
        tag = dbsession.query( Tag ).filter( Tag.name == tag_name ).first()
        if tag:
            res.append( tag )
    return res

@app.route( '/upload', methods = [ 'GET', 'POST' ] )
async def upload_route():
    
    if not g.current_account:
        return redirect( url_for( 'login_route' ) )

    form = UploadForm

    tags = dbsession.query( Tag ).filter( Tag.meta == None ).all()

    if request.method == 'GET':
        return await render_page( 'upload.html', tags = tags )
    else:
