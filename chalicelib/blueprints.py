from chalice import Blueprint

extra_routes = Blueprint(__name__)

#https://chalice.readthedocs.io/en/latest/topics/blueprints.html


@extra_routes.route('/foo')
def foo():
    return {'foo': 'bar'}