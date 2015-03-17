from django.shortcuts import render_to_response, HttpResponse
from generallibrary import rel
import os
from prices import settings

def base_objects(a_request, a_template_name, a_template_objects):
    return render_to_response(a_template_name,  a_template_objects)

def staticFile(a_request,  a_filename):
    v_fh = None
    try:
        v_fh = open(rel(os.path.join(settings.MEDIA_ROOT,  a_filename).replace('\\','/')),  'r')
        v_result = v_fh.read()
    except Exception as v_err:
        v_result = str(v_err)
    finally:
        if v_fh is not None:
            v_fh.close()
    return HttpResponse(v_result)