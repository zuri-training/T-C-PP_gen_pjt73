from .models import Template

def show_previous_templates(request):
    return {
        'previous_templates': Template.objects.all()
    }