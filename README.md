Nginx for Debian Ansible role
=============================

[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-HanXHX.nginx-blue.svg)](https://galaxy.ansible.com/list#/roles/4399) [![Build Status](https://travis-ci.org/HanXHX/ansible-nginx.svg)](https://travis-ci.org/HanXHX/ansible-nginx)

Install and configure Nginx on Debian.

This role is not production ready. SSL management wille come later.

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
  - `nginx_events`: key/value in events block
  - `nginx_http`: key/value in http block

### Vhost management

  - `nginx_vhosts`: List of dict. A vhost has few keys. See bellow.

####

  - `name`: (M) List of domain used. The first occurence is the most important!
  - `template`: (M) template used to create vhost
  - `enable`: (O) Enable the vhost (default is true)
  - `delete`: (O) Delete the vhost (default is false)
  - `redirect_from`: (O) Domain list to redirect to the first `name`. You can use this key to redirect non-www to www
  - `location`: (O) Add new custom locations (it does not overwrite!)
  - `more`: (O) Add more custom infos.
  - `upstream_params`: (O) Add upstream params (useful when you want to pass variables to PHP)

(O) : Optional
(M) : Mandatory

#### Templates

  - `base`: static template
  - `php`: PHP base template. Can work with many frameworks/tools.
  - `wordpress`
  - `dokuwiki`

Templates works as parent-child.

You can see many examples in: [tests/test.yml](tests/test.yml).

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: HanXHX.nginx }

License
-------

GPLv2

Author Information
------------------

  - You can find many other roles in my GitHub "lab": https://github.com/HanXHX/my-ansible-playbooks
  - All issues, pull-request are welcome :)

