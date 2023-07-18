from django.shortcuts import render


# Page with various info.
def about(request):
    # Template for info page.
    template = 'pages/about.html'
    # Render template into page.
    return render(request, template)


# Page with rules of conduct.
def rules(request):
    # Template for RoC page.
    template = 'pages/rules.html'
    # Render template into page.
    return render(request, template)
