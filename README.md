Nginx for Debian Ansible role
=============================

Install and configure Nginx on Debian

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
  - `nginx_pid`
  - `nginx_events`: key/value in events block
  - `nginx_http`: key/value in http block

### Vhost management

  - `nginx_vhosts`:

You need at least : "name". you can configure many templates (and yours !).

Few tips:
  - if you need another root (glpi, phpmyadmin... etc), you can specify "root"
  - you can use your own templates, you must keep the same directory organization
  - you should see COMMON.j2 to see all abilities

You can see many examples in: [tests/test.yml].

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

