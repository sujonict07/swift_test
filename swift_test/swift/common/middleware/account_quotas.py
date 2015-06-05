from swift.inspect_custom import  whoami, whosdaddy


pass  # (WIS) print __name__


class AccountQuotaMiddleware(object):
    """docstring for AccountQuotaMiddleware"""
    def __init__(self, app):
        pass  # (WIS) print "%s %s (%s -> %s)" % (__name__, self.__class__.__name__, whosdaddy(), whoami())
        self.app = app

    def __call__(self, env, start_response):
        pass  # (WIS) print "%s %s\n" % (self.__class__.__name__, env)
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return self.__class__.__name__ + "  ->  " + self.app(env, start_response)


def filter_factory(global_conf, **local_conf):
    """Returns a WSGI filter app for use with paste.deploy."""
    pass  # (WIS) print "%s (%s -> %s)" % (__name__, whosdaddy(), whoami())
    conf = global_conf.copy()
    conf.update(local_conf)
    # register_swift_info('account_quotas')

    def account_quota_filter(app):
        pass  # (WIS) print "%s (%s -> %s)" % (__name__, whosdaddy(), whoami())
        return AccountQuotaMiddleware(app)
    return account_quota_filter
