def php_default_upstream_socket(php_version):
    return '/run/php/php%s-fpm.sock' % php_version

class FilterModule(object):
    ''' PHP module '''

    def filters(self):
        return {
            'php_default_upstream_socket': php_default_upstream_socket,
        }
