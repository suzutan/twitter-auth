import argparse
import sys

import tweepy
from flask import Flask, request, redirect

parser = argparse.ArgumentParser(description='twitter auth client.')

parser.add_argument('ck', help='twitter consumer key', type=str, )
parser.add_argument('cs', help='twitter consumer secret', type=str, )
parser.add_argument('--port', help='listen port', default=8080, type=int)
args = parser.parse_args()

if args.ck is None or args.cs is None:
    parser.print_help()
    sys.exit(1)

app = Flask(__name__)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/')
def auth():

    try:
        auth = tweepy.OAuthHandler(
            args.ck, args.cs, f"http://localhost:{args.port}/callback")
        redirect_url = auth.get_authorization_url(signin_with_twitter=True)

        return redirect(redirect_url, code=307)
    except tweepy.TweepError:
        return "Error! Failed to get request token."


@app.route('/callback')
def callback():
    auth = tweepy.OAuthHandler(args.ck, args.cs)
    oauth_token = request.args.get('oauth_token')
    oauth_verifier = request.args.get('oauth_verifier')

    auth.request_token = {'oauth_token': oauth_token,
                          'oauth_token_secret': oauth_verifier}

    try:
        auth.get_access_token(oauth_verifier)
        return f"""
<pre>
ck: {args.ck}
cs: {args.cs}
at: {auth.access_token}
ats: {auth.access_token_secret}
</pre>
"""
    except tweepy.TweepError:
        return "Error! Failed to get access token."
    finally:
        shutdown_server()


app.run(host="0.0.0.0", port=args.port)
