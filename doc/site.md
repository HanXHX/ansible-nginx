Site management
===============

You can see many examples in: [tests/test.yml](../tests/test.yml).

`nginx_sites`: List of dict. A site has few keys. See bellow.

Common
------

- `name`: (M) Domain or list of domain used.
- `state`: (O) Site status. Can be "present" (default), "absent" and "disabled".
- `filename`: (O) Specify filename in `/etc/nginx/sites-*`. Do NOT specify default (reserved keyword). It will be used for log filenames and directories creation.

(O): Optional
(M): Mandatory
(D): Depends other keys...

You can use 2 config (at the same time time):

- pre-built: Some configuration are templated (Wordpress, Symfony...), auto create root dir, perform an "A+" on ssllabs for https... etc
- custom: Push your own site config template. Usefull when you have a complex configuration.


Pre-built site config
---------------------

# Keys

- `template`: (M) template used to create site. Optional if you set `state`=`absent` or using `redirect_to`.
- `redirect_from`: (O) Domain list to redirect to the first `name`. You can use this key to redirect non-www to www
- `redirect_to`: (O) Redirect all requests to this domain. Please set scheme (http:// or https:// or $sheme).
- `headers`: (O) Set additionals header as key/value list. You can append "always" to the value. Show [nginx doc](http://nginx.org/en/docs/http/ngx_http_headers_module.html).
- `redirect_to_code`: Redirect code (default: 302)
- `redirect_https`: (O) Boolean. Redirect HTTP to HTTPS. If "true", you _MUST_ set `proto` to `['https']`.
- `location`: (O) Add new custom locations (it does not overwrite!)
- `location_order`: (O) Due to non preditive `location` order, you can provide the good order (see test-location.local in [tests/test.yml](../tests/test.yml)).
- `location_before`: (O) Add new custom locations before generated location by template
- `location_order_before`: (O) Manages location order for `location_before`
- `more`: (O) Add more custom infos.
- `upstream_params`: (O) Add upstream params (useful when you want to pass variables to PHP)
- `override_try_files`: (O) overrides default try\_files defined in template
- `manage_local_content`: (O) Boolean. Set to false if you do not want to manage local content (images, css...). This option is useless if you use `_proxy` template or `redirect_to` feature.
- `htpasswd`: (O) References name key in `nginx_htpasswd`. Enable auth basic on all site. Set "false" to disable.
- `proto`: (O) list of protocol used. Default is a list with "http". If you need http and https, you must set a list with "http" and "https". You can only set "https" without http support.
- `ssl_name`: (D) name of the key used when using TLS/SSL. Optional when `proto` contains "https". If you don't set this value, it will search by `name`.
- `ssl_template` (O) "strong" (default) or "legacy". You can disable SSL helpers and add your own directives by setting "false".
- `listen_proxy_protocol` (O) Enable proxy protocol on http port.
- `listen_proxy_protocol_ssl` (O) Enable proxy protocol on https port.
- `hsts` (O) overwrite default header for hsts

### Templates

- `_base`: static template
- `_dokuwiki`
- `_redirect`: should not be called explicitly
- `_phalcon`: Phalcon PHP Framework
- `_php`: PHP base template. Can work with many frameworks/tools
- `_php_index`: Same as above. But you can only run index.php
- `_proxy`
- `_wordpress`

Templates works as parent-child.

### About proxy template

Proxy template allow you to use Nginx as reverse proxy. Usefull when you have an application service such as Redmine, Jenkins...

You have many key added to site key:

- `upstream_name`: (O) upstream name used to pass proxy
- `proxy_params`: (M) list of raw params passed to the site

(O) : Optional

### Default sites

You can manage default site by setting domain name to these variables.

- `nginx_default_site`
- `nginx_default_site_ssl`

*IT WORKS ONLY WITH PRE-BUIT SITES*


### Example


```yaml
- nginx_sites:
  - name: 'mywebsite.com'
    template: '_wordpress'
    headers:
      x-ansibled: '1'
    manage_local_content: false
```


Custom site config 
------------------

### Keys

- `custom_template`: (M) template path used 

You can add some extra infos if needed.

### Example:

```yaml
- nginx_sites:
  - name: 'mycustom-website.com'
    custom_template: 'my/template_dir/the-template.conf.j2'
    allow_admin: '192.168.0.0/24'
```

In `my/template_dir/the-template.conf.j2`:

```
#
# {{ ansible_managed }} - {{ item.name }}
#

server {
	listen 8080 http2 proxy_protocol;
    server_name {{ item.name }};
	index index.html;
    root /var/www/{{ item.name }};

	location / {
		try_files $uri $uri/ =404;
	}

	location /admin {
		allow {{ item.allow_admin }};
		deny all;
	}
}
```


