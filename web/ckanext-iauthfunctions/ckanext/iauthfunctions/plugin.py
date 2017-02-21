import os

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import jwt
import pylons


class IauthfunctionsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IAuthenticator)
    plugins.implements(plugins.IAuthFunctions)

    def login(self):
        """
        Implementation of IAuthenticator.login
        We don't need to do anything here as we provide a JWT token with all info
        """
        pass

    def identify(self):
        """
        Implementiation of IAuthenticator.identify
        Identify which user (if any) is logged in via DatapuntAmsterdam / auth
        """
        user = 'anonymous'
        if pylons.session.get('Authorization'):
            jwt_payload = jwt.decode(
                pylons.session.get('Authorization'),
                os.getenv('JWT_SHARED_SECRET_KEY', 'insecure'),
                algorithms=['HS256']
            )
            user = jwt_payload.get('authz')
        if user:
            plugins.toolkit.c.user = 'authenticated'

    def get_auth_functions(self):
        """
        IAuthFunctions
        :return:
        """
        pass
