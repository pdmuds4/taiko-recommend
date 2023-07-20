import os
from dataaccess import DataAccess

def write1( file1, str1 ): 
    with open( file1, 'w', encoding='utf-8' ) as f1: 
        f1.write( str1 ) 
    return 0 

da = DataAccess()
title_option = [t[0] for i in range(5,11) for t in da.get_table(i)]

optstr = '''
{% extends "layout.html" %}
{% block content %}'''

for o in title_option:
    optstr += f"<option value='{o}'></option>\n"

optstr += '''{% endblock %}'''
write1( os.path.dirname(__file__) + "/templates/test.html", optstr ) 