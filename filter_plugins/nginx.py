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

def nginx_all_site_names(site):
    all_sites = []
    if isinstance(site['name'], list):
        all_sites = all_sites + site['name']
    else:
        all_sites.append(site['name'])

    if site.has_key('redirect_from'):
        if isinstance(site['redirect_from'], list):
             all_sites = all_sites + site['redirect_from']
        else:
            all_sites.append(site['redirect_from'])

    return all_sites

def nginx_search_by_ssl_name(sites, ssl_name):
    if isinstance(ssl_name, list):
        comp_ssl_name = ssl_name[0]
    else:
        comp_ssl_name = ssl_name

    res = None
    for site in sites:
        if site.has_key('ssl_name') and site['ssl_name'] == comp_ssl_name:
            res = site
            break
    return res

class FilterModule(object):
    ''' Nginx module '''

    def filters(self):
        return {
            'nginx_site_filename': nginx_site_filename,
            'nginx_site_name': nginx_site_name,
            'nginx_ssl_dir': nginx_ssl_dir,
            'nginx_key_path': nginx_key_path,
            'nginx_cert_path': nginx_cert_path,
            'nginx_all_site_names': nginx_all_site_names,
            'nginx_search_by_ssl_name': nginx_search_by_ssl_name
        }
