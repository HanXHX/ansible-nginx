def php_default_upstream_socket(php_version):
    return '/run/php/php%s-fpm.sock' % php_version

def php_default_upstream_name(php_version):
    return 'default_php_%s' % php_version

def php_fpm_service(php_version):
    return 'php%s-fpm' % php_version

class FilterModule(object):
    ''' PHP module '''

    def filters(self):
        return {
            'php_default_upstream_socket': php_default_upstream_socket,
            'php_default_upstream_name': php_default_upstream_name,
            'php_fpm_service': php_fpm_service,
            'php_fpm_package': php_fpm_service
        }
