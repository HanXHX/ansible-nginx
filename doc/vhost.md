Vhost management
================

You can see many examples in: [tests/test.yml](../tests/test.yml).

`nginx_vhosts`: List of dict. A vhost has few keys. See bellow.

Common
------

- `name`: (M) Domain or list of domain used.
- `template`: (D) template used to create vhost. Optional if you set `delete` to true or using `redirect_tor`.
- `filename`: (O) Specify filename in /etc/nginx/sites-*. Do NOT specify default (reserved keyword). It will be used for log filenames and directories creation.
- `state`: (O) Vhost status. Can be "present" (default), "absent" and "disabled".
- `redirect_from`: (O) Domain list to redirect to the first `name`. You can use this key to redirect non-www to www
- `redirect_to`: (O) Redirect all requests to this domain. Please set scheme (http:// or https:// or $sheme).
- `headers`: (O) Set additionals header as key/value list. You can append "always" to the value. Show [nginx doc](http://nginx.org/en/docs/http/ngx_http_headers_module.html).
- `redirect_to_code`: Redirect code (default: 302)
- `redirect_https`: (O) Boolean. Redirect HTTP to HTTPS. If "true", you _MUST_ set `proto` to ```['https']```.
- `location`: (O) Add new custom locations (it does not overwrite!)
- `more`: (O) Add more custom infos.
- `upstream_params`: (O) Add upstream params (useful when you want to pass variables to PHP)
- `override_try_files`: (O) overrides default try\_files defined in template
- `manage_local_content`: (O) Boolean. Set to false if you do not want to manage local content (images, css...). This option is useless if you use `_proxy` template or `redirect_to` feature.
- `htpasswd`: (O) References name key in `nginx_htpasswd`. Enable auth basic on all vhost.
- `proto`: (O) list of protocol used. Default is a list with "http". If you need http and https, you must set a list with "http" and "https". You can only set "https" without http support.
- `ssl_name`: (D) name of the key used when using TLS/SSL. Mandatory when `proto` contains "https"
- `ssl_template` (O) "strong" (default) or "legacy". You can disable SSL helpers and add your own directives by setting "false". 
- `php_version` (O) Sepecify PHP version (5 or 7)

(O): Optional
(M): Mandatory
(D): Depends other keys...

Templates
---------

- `_base`: static template
- `_backuppc`: access to [BackupPC](http://backuppc.sourceforge.net/) (be careful: you need to install [fcgiwrap](https://packages.debian.org/jessie/fcgiwrap))
- `_dokuwiki`
- `_redirect`: should not be called explicitly
- `_nagios3`: access to Nagios3 (be careful: you need to install [fcgiwrap](https://packages.debian.org/jessie/fcgiwrap))
- `_owncloud`: access to Owncloud (note: you must set `nginx_apt_package` to //nginx-extras//) **UNSTABLE**
- `_phalcon`: Phalcon PHP Framework
- `_php`: PHP base template. Can work with many frameworks/tools
- `_php_index`: Same as above. But you can only run index.php
- `_proxy`
- `_wordpress`

Templates works as parent-child.

About proxy template
--------------------

Proxy template allow you to use Nginx as reverse proxy. Usefull when you have an application service such as Redmine, Jenkins...

You have many key added to vhost key:

- `upstream_name`: (O) upstream name used to pass proxy
- `proxy_params`: (M) list of raw params passed to the vhost

(O) : Optional

Default vhosts
--------------

You can manage default vhost by setting domain name to these variables.

- `nginx_default_vhost`
- `nginx_default_vhost_ssl`
