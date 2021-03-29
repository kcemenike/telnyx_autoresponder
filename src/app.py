import os
from dotenv import load_dotenv
from flask import Flask, request, abort, jsonify
import telnyx

MAPPING = {
    "pizza": "Chicago pizza is the best",
    "ice cream": "I prefer gelato"
}
DEFAULT = "Please send either the word 'pizza' or 'ice cream' for a different response"


def parse_message(body: dict):
    # Return none if no data in request body
    if body is None:
        return None
    # Check that event type is a message and not a status
    try:
        if (body['data']['payload']['type'] == 'SMS'):
            from_ = body['data']['payload']['from']['phone_number']
            to = body['data']['payload']['to'][0]['phone_number']
            text = body['data']['payload']['text'].lower()
            print(f'''
            Message from {from_} to {to}:
            {text}
            ''')
        else:
            return None
    except:
        return None

    for item in MAPPING:
        if item.lower() in text:
            reply = MAPPING.get(item)
            return {'from': from_, 'to': to, 'reply': reply}
    else:
        return {'from': from_, 'to': to, 'reply': DEFAULT}


def send_message(from_, to, message):
    try:
        telnyx.Message.create(
            from_=to,
            to=from_,
            text=message)
        print(f'''
            Response sent from {to} to {from_}:
            {message}
        ''')
    except:
        print('Message sending failed')


def create_app():
    app = Flask(__name__)

    @app.route('/webhooks', methods=['POST', 'GET'])
    def autoResponse():
        if request.method == 'POST':
            # Receive inbound message
            body = request.get_json()

            # Check if POST doesn't have content
            if body is None:
                print('No body')
                abort(400)

            # Parse message
            if (body['data']['event_type'] == 'message.received'):
                parsed_message = parse_message(body)
                try:
                    # Get sender, recipient and message information
                    # from parsed message
                    from_ = parsed_message.get('from')
                    to = parsed_message.get('to')
                    message = parsed_message.get('reply')
                    # Respond to message
                    send_message(from_, to, message)
                except:
                    print('Parsed message faulty')
                    abort(400)

                return jsonify({
                    'success': True,
                    'message': 'Autoresponder complete'
                }), 200
            return jsonify({
                'success': True
            })
        else:
            print('Method not post')
            abort(400)

    @app.route('/test', methods=['GET'])
    def test():
        print('Test successful')
        return jsonify({
            'success': True
        }), 200

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    return app


app = create_app()

if __name__ == "__main__":
    load_dotenv()
    telnyx.api_key = os.getenv('TELNYX_API_KEY')
    port = os.getenv('PORT')
    app.run(port=port, debug=True)
