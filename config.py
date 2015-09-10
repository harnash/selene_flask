from authomatic.providers import oauth2

CONFIG = {
    'oauth': {
        'class_': oauth2.OAuth2,

        'consumer_key': 'dddefdffgfdg',
        'consumer_servret': 'sf4445',
        'short_name': 'wikia',
    },
    
    'fb': {
           
        'class_': oauth2.Facebook,
        
        # Facebook is an AuthorizationProvider too.
        'consumer_key': '########################',
        'consumer_secret': '########################',
        
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    },
}