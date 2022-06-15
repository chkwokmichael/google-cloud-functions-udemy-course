def hello_world(request):
    '''
    This cloud function prints return "Hello World" page when there is an HTTP request.
    '''

    # CORS
    # If the funtion is called by web-broswers, we need to include a header
    # It is called a preflight request. It's returned before the main request (returning the html to print names)
    if request.method == 'OPTIONS':
        headers = {
            # Specify the specific domain, or allow everyone '*'
            'Access-Control-Allow-Origin': '*',
            # Specify the allowed methods to call the funciton
            'Access-Control-Allow-Methods': 'POST',
            # Specify the allowed headers
            'Access-Control-Allow-Headers': 'Content-Type',
            # Maximum time for the broswer to remember the header in seconds (1 hour = 3600s)
            'Access-Control-Max-Age': '3600'
        }

        return '',204,headers
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    # Create a variable `request_args`` to hold the arguments of the request `request.args`
    request_args = request.args
    # Create a variable `request_json` to catch the JSON object argument if there's any
    ## If there are no JSON object passed, set it to none (silen=True)
    request_json = request.get_json(silent=True)

    # Check if the argument is none or a dictionary
    # If the argument is not none and includes name, store the name of the request
    if request_args and 'name' in request_args and 'lastname' in request_args:
        name = request_args['name']
        lastname = request_args['lastname']
    # Check if the JSON argument is passed
    elif request_json and 'name' in request_json and 'lastname' in request_json:
        name = request_json['name']
        lastname = request_json['lastname']
    else:
        name = 'World'
        lastname = 'lastname'
    
    return f'Hello {name} {lastname}!', 200, headers