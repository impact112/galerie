
from routes.common import *
from database import *
from forms import Form, Field
import forms.validators as validators


class AddTagForm(Form):

    tag_name = Field(
        name='tag_name',
        label='Name',
        validators=[validators.NotEmpty()]
    )

    tag_description = Field(
        name='tag_description',
        label='Description',
        validators=[validators.NotEmpty()]
    )


async def admin_route():

    if g.current_account.power_level < 99:
        return 'Not an admin'

    accounts = dbsession.query(Account).all()
    tags = dbsession.query(Tag).all()
    return await render_page('admin.html', tags=tags, accounts=accounts)


async def add_tag():
    pass


async def remove_tag():
    pass
