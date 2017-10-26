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

class FilterModule(object):
    ''' Nginx module '''

    def filters(self):
        return {
            'nginx_site_filename': nginx_site_filename,
            'nginx_site_name': nginx_site_name
        }
