# twitter-auth

twitter auth するやつ

twitter app は適当な redirect_url を設定しておく必要があります

## use

1. Start the server used for authentication

   ```bash
   docker run --rm -p 8080:8080/tcp suzutan/twitter-auth <consumer_key> <consumer_secret>
   ```

1. Access URL of <http://localhost:8080/>
1. authenticate twitter account
1. view consumer_key,consumer_secret, access_token andaccess_token_secret
