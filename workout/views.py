"""Module providing the main views."""
import git
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

class HomePage(TemplateView):
    """Class representing a person"""

    template_name = 'index.html'


@csrf_exempt
def update(request):
    """"pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        """
    # if request.method == "POST":
        repo = git.Repo("")
        origin = repo.remotes.origin

        origin.pull()

    #     return HttpResponse("Updated code on PythonAnywhere")
    # else:
    #     return HttpResponse("Couldn't update the code on PythonAnywhere")
