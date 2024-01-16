from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


@login_required
def vote_proccess(request):
    if request.method == 'POST':
        messages.success(
            request,
        )
        return redirect('competitors:dashboard')
    return render(request, '', {'section': 'vote'})
