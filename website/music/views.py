from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Album
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    # used if you want to change the default 'object_list' name in html file
    # context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # since using same url for get and post reqs

    # display blank for w get
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # storing locally first before putting in DB
            user = form.save(commit=False)

            # first we want to get cleaned(normalized) data
                # which is data that is formatted properly
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # when changing password, need to use func for encryption
            user.set_password(password)
            # now save
            user.save()

            # authenticate and login user
            # returns User obj if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                # if account isn't banned or something
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
        # else not auth, sent blank for back again
        return render(request, self.template_name, {'form': form})
