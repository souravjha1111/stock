from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import shortner_class
from django.views import View
from .forms import SubmitForm
from .utils import create_shortcode, code_generator
# Create your views here.

class urlshortner_home(View):
    def get(self,request,*args,**kwargs):
        form = SubmitForm()
        context = {
            "form": form
        }
        return render(request,'urlshortner/urlshortner.html',context)
    
    def post(self,request,*args,**kwargs):
        form = SubmitForm(request.POST)
        context = {
            "form": form
        }
        template = 'urlshortner/urlshortner.html'
        if self.request.POST['shortcode'] and shortner_class.objects.filter(shortcode = self.request.POST['shortcode']).exists() != True:
            if form.is_valid():
                new_url = form.cleaned_data.get("url")
                obj,created = shortner_class.objects.get_or_create(url = new_url,
                             shortcode = form.cleaned_data.get("shortcode"))
                #to_save_link = create_shortcode(obj)
                context = {
                "object":obj,
                "created": created
                }        
                if created:
                    template = 'urlshortner/success.html'
                else:
                    template = 'urlshortner/failure.html'
        elif self.request.POST['shortcode'] and shortner_class.objects.filter(shortcode = self.request.POST['shortcode']).exists() == True:
            template = "urlshortner/already_exist.html"

        elif form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj,created = shortner_class.objects.get_or_create(url = new_url)
            #to_save_link = create_shortcode(obj)
            context = {
            "object":obj,
            "created": created
            }        
            if created:
                template = 'urlshortner/success.html'
            else:
                template = 'urlshortner/failure.html'
        return render(request,template,context)

class urlshortner_request_view(View):
    def get(self,request,shortcode,*args,**kwargs):
        obj = get_object_or_404(shortner_class,shortcode = shortcode)
        return redirect(obj.url)
