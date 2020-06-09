# twitter-auth

server for twitter oauth.

Twitter app needs proper redirect_url set.

## use

1. Start the server used for authentication

   ```bash
   docker run --rm -p 8080:8080/tcp suzutan/twitter-auth <consumer_key> <consumer_secret>
   ```

1. Access URL of <http://localhost:8080/>
1. authenticate twitter account
1. view consumer_key,consumer_secret, access_token andaccess_token_secret
