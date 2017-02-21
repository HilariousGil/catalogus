import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.plugins.toolkit import get_action

import pylons
import jwt

class IauthfunctionsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IAuthenticator)
    plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IPermissionLabels)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'iauthfunctions')

    # IAuthenticator

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
                pylons.session.get('Authorization'), 'secret', algorithms=['HS256'])
            user = jwt_payload.get('uid')
        if user:
            plugins.toolkit.c.user = user


    # IAuthFunctions

    def get_auth_funcytions(self):
        pass

    # # IPermissionLabels
    # def get_dataset_labels(self, dataset_obj):
    #     """
    #     Use dataclassificatie field
    #
    #     :param dataset_obj:
    #     :return:
    #     """
    #     labels = u'public'
    #     if dataset_obj.dataclassificatie == 'closed':
    #         labels = u'closed'
    #     elif dataset_obj.dataclassificatie == 'closed_plus':
    #         labels = u'closed_plus'
    #
    #         return [labels, ]
    #
    #     return super(IauthfunctionsPlugin, self).get_dataset_labels(dataset_obj)
    #
    # def get_user_dataset_labels(self, user_obj):
    #     """
    #     Use dataclassificatie field
    #     :param user_obj:
    #     :return:
    #     """
    #     labels = super(IauthfunctionsPlugin, self).get_user_dataset_labels(user_obj)
    #     if user_obj:
    #         orgs = get_action(u'organization_list_for_user')(
    #             {u'user': user_obj.id}, {u'permission': u'admin'})
    #         labels.extend(u'admin-%s' % o['id'] for o in orgs)
    #     return labels
