from django import template

register = template.Library()


@register.inclusion_tag("results.html")
def search(request): 
    print("[DEBUG]: enter search template tag")
    token = request.POST.get('token')
    return { "token": token } 
