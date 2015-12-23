Nginx for Debian Ansible role
=============================

[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-HanXHX.nginx-blue.svg)](https://galaxy.ansible.com/list#/roles/4399) [![Build Status](https://travis-ci.org/HanXHX/ansible-nginx.svg?branch=master)](https://travis-ci.org/HanXHX/ansible-nginx) 

Install and configure Nginx on Debian.

SSL management will come later.

Requirements
------------

None.

Role Variables
--------------

  - `nginx_apt_package`: APT nginx package (try: apt-cache search ^nginx)
  - `nginx_root`: root directory where you want to have your files
  - `nginx_log_dir`: log directory (if you change it, don't forget to change logrotate config)
  - `nginx_ssl_dir`: directory where you install your SSL/TLS keys
  - `nginx_resolver`: list of DNS resolver (default: OpenDNS)
  - `nginx_error_log_level`: default log level
  - `nginx_dh_length`: DH key length (default is 2048)

### PHP

  - `nginx_php`: boolean if you need to preconfigure PHP (default: false)
  - `nginx_php_sockets`: list of //sockets//

You should see [Nginx upstream module doc](http://nginx.org/en/docs/http/ngx_http_upstream_module.html).

Socket:
  - `unix_socket`
  - `host`
  - `port`
  - `weight`
  - `max_fails`
  - `fail_timeout`

### Nginx Configuration

  - `nginx_user`
  - `nginx_worker_processes`
  - `nginx_pid`: daemon pid file 
  - `nginx_events_*`: all variables in events block
  - `nginx_http_*`: all variables in http block
  - `nginx_custom_http`: instructions list (will put data in `/etc/nginx/conf.d/custom.conf`)

### Vhost management

You can see many examples in: [tests/test.yml](tests/test.yml).

  - `nginx_vhosts`: List of dict. A vhost has few keys. See bellow.

#### Common

  - `name`: (M) Domain or list of domain used.
  - `template`: (D) template used to create vhost. Optional if you set `delete` to true or using `redirect_tor`.
  - `enable`: (O) Enable the vhost (default is true)
  - `delete`: (O) Delete the vhost (default is false)
  - `redirect_from`: (O) Domain list to redirect to the first `name`. You can use this key to redirect non-www to www
  - `redirect_to`: (O) Redirect all requests to this domain. Please set scheme (http:// or https:// or $sheme).
  - `redirect_to_code`: Redirect code (default: 302)
  - `location`: (O) Add new custom locations (it does not overwrite!)
  - `more`: (O) Add more custom infos.
  - `upstream_params`: (O) Add upstream params (useful when you want to pass variables to PHP)
  - `override_try_files`: (O) overrides default try\_files defined in template
  - `manage_local_content`: (O) Boolean. Set to false if you don't want to manage local content (images, css...). This option is useless if you use `_proxy` template or `redirect_to` feature.
  - `htpasswd`: (0) References name key in `nginx_htpasswd`. Enable auth basic on all vhost.

(O): Optional
(M): Mandatory
(D): Depends other keys...

#### Templates

  - `_base`: static template
  - `_backuppc`: access to [BackupPC](http://backuppc.sourceforge.net/) (be careful: you need to install [fcgiwrap](https://packages.debian.org/jessie/fcgiwrap))
  - `_dokuwiki`
  - `_redirect`: should not be called explicitly
  - `_phalcon`: Phalcon PHP Framework
  - `_php`: PHP base template. Can work with many frameworks/tools
  - `_php_index`: Same as above. But you can only run index.php
  - `_proxy`
  - `_wordpress`

Templates works as parent-child.

#### About proxy template

Proxy template allow you to use Nginx as reverse proxy. Usefull when you have application serveur such as Redmine, Jenkins...

You have many key added to vhost key:

  - `upstream_name`: (O) upstream name used to pass proxy
  - `proxy_params`: (M) list of raw params passed to the vhost

(O) : Optional
(M) : Mandatory

#### About custom location

`location` is list of instructions (like *echo*, *return*...). Do not forget to end all your instructions with *;*. You can use a special key to use auth basic. It works in the same way as in `nginx_vhost`

### Upstream management

  - `nginx_upstreams`: List of dict. An upstream has few keys. See bellow.

Note: Few params are unavailable on old Nginx version. But this role don't put it if your version is too old!

#### Upstream params

- `name`: upstream name. Can be use in vhost with *proxy_pass http://upstream_name*
- `params`: list of param (hash, zone...)
- `servers`: each upstream MUST have at least 1 server

#### Server params

You must set a `path`. For example: *192.168.0.50:8080* or *unix:/tmp/my.sock*.

All this params are optional. You should see [Nginx upstream doc](http://nginx.org/en/docs/http/ngx_http_upstream_module.html).

  - `weight`
  - `max_fails`
  - `fail_timeout`
  - `backup`
  - `down`
  - `route`
  - `slow`start`

### Auth Basic management

Auth basic is managed in a separate list. Each auth file can be shared between locations or vhosts.

Each htpasswd has few keys:

  - `name`: (M) used to create file and as pointee
  - `description`: (M) Used for the message box :)
  - `users`: each users is composed with 3 keys: `name` (M), `password` (M) and `state` present/absent (default: present)
  - `state`: (O) present or absent. Default: present


Dependencies
------------

None

Example Playbook
----------------

See [tests/test.yml](tests/test.yml).

License
-------

GPLv2

Author Information
------------------

- Twitter: [@hanxhx_](https://twitter.com/hanxhx_)

