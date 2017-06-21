from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'DataStuff'}

@view_config(route_name='layout', renderer='templates/layout.jinja2')
def layout_view(request):
    return {'project': 'DataStuff'}

@view_config(route_name='sample', renderer='templates/pageSample.jinja2')
def sample_view(request):
    return {'project': 'DataStuff'}