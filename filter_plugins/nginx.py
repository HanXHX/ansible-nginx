def nginx_site_filename(site):
    if site.has_key('filename'):
        return site['filename']
    else:
        return nginx_site_name(site)

def nginx_site_name(site):
    if isinstance(site['name'], list):
        return site['name'][0]
    else:
        return site['name']

def nginx_ssl_dir(pair, ssl_dir):
    return ssl_dir + '/' + nginx_site_filename(pair)

def nginx_key_path(pair, ssl_dir):
    if pair.has_key('dest_key'):
        return pair['dest_key']
    else:
        return nginx_ssl_dir(pair, ssl_dir) + '/' + nginx_site_filename(pair) + '.key'

def nginx_cert_path(pair, ssl_dir):
    if pair.has_key('dest_cert'):
        return pair['dest_cert']
    else:
        return nginx_ssl_dir(pair, ssl_dir) + '/' + nginx_site_filename(pair) + '.crt'

class FilterModule(object):
    ''' Nginx module '''

    def filters(self):
        return {
            'nginx_site_filename': nginx_site_filename,
            'nginx_site_name': nginx_site_name,
            'nginx_ssl_dir': nginx_ssl_dir,
            'nginx_key_path': nginx_key_path,
            'nginx_cert_path': nginx_cert_path
        }
