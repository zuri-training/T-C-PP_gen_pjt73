from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from .models import Company, Template
from .forms import WebsiteForm
import re
import pdfkit

# Create your views here.
def privacy(request):
    return render(request, 'pp_gen/privacy.html')


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST or None)

        company_name = request.POST['company_name']
        company_website_name = request.POST['company_website_name']
        company_website_url = request.POST['company_website_url']
        cookies = request.POST['cookies']
        google_advertising = request.POST['google_advertising']
        third_party_advertising = request.POST['third_party_advertising']
        country = request.POST['country']
        state = request.POST['state']
        company_email_address = request.POST['company_email_address']

        new_company = Company(
            company_name = company_name,
            company_website_name = company_website_name,
            company_website_url = company_website_url,
            cookies = cookies,
            google_advertising = google_advertising,
            third_party_advertising = third_party_advertising,
            country = country,
            state = state,
            company_email_address = company_email_address
        )

        new_company.save()

        return redirect('/pp_gen/preview')
    form = WebsiteForm()

    context = {
        'website_form': form
    }

    return render(request, 'pp_gen/pp_questions_2.html', context)

def generate_policy(request):
    id = 0
    for company in Company.objects.all():
        id = company.id
    if request.method == 'POST':
        try:
            company = Company.objects.get(company_name=request.POST['company_name'])
        except company.MultipleObjectsReturned:
            raise Http404("You can only save one template per company. Delete other templates for this company before saving this one....")
            
        slug = request.POST['company_name'].lower()
        slug = re.sub('[^A-Za-z0-9]', '', slug)
        
        new_template = Template(
            company = company,
            slug = slug
        )

        new_template.save()
        return HttpResponse('<h2>Your Template has been saved.</h2>')

    context = {
        'company': Company.objects.filter(id=id),
        'saved_policies': Template.objects.all()
    }
    
    return render(request, 'pp_gen/policy.html', context)
        


def view_saved_policies(request, slug):
    # Save all the previously saved terms and condions to the context variable
    selected_policy = Template.objects.get(slug=slug).company
    context = {
        'selected_policy': selected_policy,
        'saved_policy': Template.objects.get(slug=slug)
    }
    # Return the generate terms function
    return render(request, 'pp_gen/dynamic_policy.html', context)

# Function to downoad A generated terms and conditions as PDF
def download_pdf(request, company_name):
    # Get a company by its name
    selected_company = Company.objects.get(company_name=company_name)

    # Read the template file and push each line to a list
    lines = []
    with open('pp_gen/src/privacy_policy_sample.txt') as f:
        lines = f.readlines()
    # Initialize a count variable and a list
    count = 0
    new_lines = []
    # Initialize the final string
    final_string = ''
    # Loop through the lines in the template file and replace the placeholders with variables
    for line in lines:
        if '{{ company.company_website_name }}' in line:
            line = re.sub('{{ company.company_website_name }}', selected_company.company_website_name, line, flags=re.IGNORECASE)
        
        if '{{ company.company_name }}' in line:
            line = re.sub('{{ company.company_name }}', selected_company.company_name, line, flags=re.IGNORECASE)

        if '{{ company.company_website_url }}' in line:
            line = re.sub('{{ company.company_website_url }}', selected_company.company_website_url, line, flags=re.IGNORECASE)

        if '{{ company.company_email_address }}' in line:
            line = re.sub('{{ company.company_email_address }}', selected_company.company_email_address, line, flags=re.IGNORECASE)
        # Append the edited lines to the initialized list and increment the count
        new_lines.append(line)
        count += 1
    # Append the initialized list to the final_string variable
    for line in new_lines:
        final_string += line
    # Set options for the PDF file
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
        }


    # Use False instead of output path to save pdf to a variable
    # Remove any special characters from the company name and save it to the filename
    filename = re.sub('[!,*)@#%(&$_?.^]', '', f'{selected_company.company_name}')
    # Generate a PDF from the final_string variable
    pdf = pdfkit.from_string(final_string, False, options=options,)
    # Save the generated PDF to the filename and download it
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='f'{filename}.pdf'

    return response

#creating views for download format
def format(request, company_name):
    context = {
        'company_name': company_name
    }
    return render(request, 'pp_gen/download_format.html', context)