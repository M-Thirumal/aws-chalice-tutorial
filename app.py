from chalice import Chalice
from chalicelib.blueprints import extra_routes

import os

app = Chalice(app_name='aws-chalice-tutorial')

# Blueprint registration
app.register_blueprint(extra_routes)

@app.route('/')
def index():
    return {'hello': 'world'}


@app.lambda_function()
def foo(event, context):
    return {'value': os.environ.get('MY_ENV_VAR')}

# Pagination example


@app.route('/pagination')
def pagination():
    app.log.debug("you are in Pagination!")
    return {
        'page': app.current_request.query_params.get('page'),
        'limit': app.current_request.query_params.get('limit'),
    }

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
