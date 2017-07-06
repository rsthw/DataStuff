from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/pageSample.jinja2')
def my_view(request):
    return {'project': 'DataStuff'}

@view_config(route_name='layout', renderer='templates/layout.jinja2')
def layout_view(request):
    return {'project': 'DataStuff'}

@view_config(route_name='sample', renderer='templates/pageSample.jinja2')
def sample_view(request):
    return {'project': 'DataStuff'}

@view_config(route_name='practice', renderer='templates/practice.jinja2')
def practice(request):
    far="";
    if ('tem' in request.params.keys()):
        far = int(request.params['tem']) - 50;
    else:
        print("algo esta mal")

    return {'project': 'DataStuff',
            'nombre': 'goey',
            'tem': far}