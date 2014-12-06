from eve import Eve
from flask import jsonify, request, redirect
from twilio.util import TwilioCapability
from twilio import twiml
from flask.ext.cors import CORS

app = Eve()
cors = CORS(app)
app.config.from_envvar('TANDEM_SETTINGS', silent=True)

""" twilio functions """
@app.route('/client', methods=['GET', 'POST'])
def client():
    """Respond to incoming requests."""
 
    account_sid = app.config['TWILIO_ACCOUNT_SID']
    auth_token  = app.config['TWILIO_AUTH_TOKEN'] 
 
    capability = TwilioCapability(account_sid, auth_token)
 
    application_sid = app.config['TWILIO_APP_SID']

    capability = TwilioCapability(account_sid, auth_token)
    capability.allow_client_outgoing(application_sid)
    token = capability.generate()
 
    return jsonify(token=token)
 
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    """Greet the caller."""

    response = twiml.Response()
    response.say("Please leave your message after the beep - you can end the message by pressing any button.")
    response.record(maxLength="30", action="/recording")
    return str(response)

@app.route('/recording', methods=['GET', 'POST'])
def recording():
    """Play back the caller's recording."""
 
    recording_url = request.values.get("RecordingUrl", None)
 
    response = twiml.Response()
    response.say("Thanks for the message... take a listen to what you howled.")
    response.play(recording_url)
    response.say("Goodbye.")
    return str(response)

