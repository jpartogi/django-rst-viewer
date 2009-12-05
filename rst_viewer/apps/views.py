from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect

from rst_viewer.apps.forms import ViewerForm

class ViewerFormPreview(FormPreview):
    preview_template = 'preview.html'
    form_template = 'form.html'
    
    def done(self, request, cleaned_data):
        form = ViewerForm(request.POST)

        return HttpResponseRedirect('')
