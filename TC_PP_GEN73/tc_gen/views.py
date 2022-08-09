from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

#creating the view for the terms and conditions preview
def tc_preview(request):

    #DUMMY DATA
    context = {
        'name': 'Ayodele',
        'email': 'ayodelekadiri.ak@gmail.com',
        'site': 'thehandsomeguys.com'
    }

    return render(request, 'tc_gen/tc_preview.html', context)

#view for the document you want to download
def tc_download(request):

    #DUMMY DATA
    context = {
        'name': 'Ayodele',
        'email': 'ayodelekadiri.ak@gmail.com',
        'site': 'thehandsomeguys.com'
    }

    #path of the template you want to download
    template_path = 'tc_gen/tc_download_ready.html'

    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'filename="Terms_and_Conditions.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    #create pdf
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Errors occured while generating the pdf.')

    return response


def tc_gen(request):
    return render(request, 'tc_gen/tandc.html')


def tc_gen2(request):
    return render(request, 'tc_gen/tandc2.html')

def questions(request):
    return render(request, 'tc_gen/pp_questions.html')

def privacy(request):
    return render(request, 'tc_gen/privacy.html')

def privacy2(request):
    return render(request, 'tc_gen/privacy1.html')


def done(request):
    return render(request, 'tc_gen/done.html')

def format(request):
    return render(request, 'tc_gen/download_format.html')

def complete(request):
    return render(request, 'tc_gen/after_download.html')
