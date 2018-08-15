from django import template 

register = template.Library() 

@register.simple_tag(takes_context=True)
def template_filename(context):
    '''Returns template filename with the extension'''
    return context.template_name
