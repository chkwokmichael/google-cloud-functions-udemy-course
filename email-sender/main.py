from flask import abort

def get_bearer_token(request):

    bearer = request.headers.get('Authorization', None)
    if not bearer:
        abort(401)
    elements = bearer.split()
    if elements[0].lower() != 'bearer':
        # Authorisation header must start with 'Bearer'
        abort(401)
    elif len(elements) == 1:
        # Token was not found
        abort(401)
    elif len(elements) > 2:
        # Authorisation header must be of the form 'Bearer Token'
        abort(401)
    
    token = elements[1]
    return token

def send_mail(request):

    # using SendGrid's Python Library
    # https://github.com/sendgrid/sendgrid-python
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    # Adding a check to only allow the cloud functino to be called with POST method
    if request.method != 'POST':
        abort(405)

    # Check if the request contain the authorised token
    bearer_token = get_bearer_token(request)
    secret_key = os.environ.get('ACCESS_TOKEN')
    if bearer_token != secret_key:
        # Abort unauthorisation error
        abort(401)

    request_json = request.get_json(silent=True)
    parameters = ('sender','receiver','subject','message')

    sender, receiver, subject, message = '','','',''

    # Check if the JSON argument is passed when calling the funciton
    if request_json and all(k in request_json for k in parameters):
        sender = request_json['sender']
        receiver = request_json['receiver']
        subject = request_json['subject']
        message = request_json['message']
    else:
        # If not, 
        # Abort HTTP code 400 if no arguments are passed
        abort(400)
    
    message = Mail(
        from_email=sender,
        to_emails=receiver,
        subject=subject,
        html_content=message)
    
    try:
        # source API KEY from .env
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        # send message with sg.send()
        sg.send(message)
        # Return HTTP code 200 with "OK"
        return 'OK',200
    except Exception as e:
        return e, 400