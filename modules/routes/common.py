
from quart import Quart, g, render_template, session, redirect, url_for, request, flash, jsonify
import time
from pathlib import Path

def render_page( arg, **kwargs ):
    kwargs.update( { 'current_account': g.current_account } ) 
    return render_template( arg, **kwargs )
