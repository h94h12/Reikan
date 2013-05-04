def auth(request):
    t = Tumblpy(app_key = settings.TUMBLR_COMSUMER_KEY, app_secret = settings.TUMBLR_SECRET_KEY,
        callback_url = 'http://%s/tumblr/callback' % request.get_host())
    auth_props = t.get_authentication_tokens()
    auth_url = auth_props['auth_url']

    oauth_token = auth_props['oauth_token']
    oauth_token_secret = auth_props['oauth_token_secret']

    request.session["oauth_token"] = oauth_token
    request.session["oauth_token_secret"] = oauth_token_secret

    return redirect("http://www.tumblr.com/oauth/authorize?oauth_token=%s" % oauth_token)
