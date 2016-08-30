Nginx for Debian/FreeBSD Ansible role
=====================================

[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-HanXHX.nginx-blue.svg)](https://galaxy.ansible.com/HanXHX/nginx/) [![Build Status](https://travis-ci.org/HanXHX/ansible-nginx.svg?branch=master)](https://travis-ci.org/HanXHX/ansible-nginx)

Install and configure Nginx on Debian/FreeBSD.

Features:

- SSL/TLS "hardened" support
- Manage basic auth on vhost / location
- Proxy + Upstream
- Fast PHP configuration
- Preconfigured vhost templates (should work on many app)
- Auto-configure HTTP2 on SSL/TLS vhosts

Requirements
------------

None. If you set true to `nginx_backports`, you must install backports repository before lauching this role.

Role Variables
--------------

### Packaging

Debian:

- `nginx_apt_package`: APT nginx package (try: apt-cache search ^nginx)
- `nginx_backports`: Install nginx from backport repository (bool)

FreeBSD:

- `nginx_pkgng_package`: PKGNG nginx package (should be "nginx" or "nginx-devel")

### Shared

- `nginx_root`: root directory where you want to have your files
- `nginx_log_dir`: log directory (if you change it, don't forget to change logrotate config)
- `nginx_resolver`: list of DNS resolver (default: OpenDNS)
- `nginx_error_log_level`: default log level
- `nginx_auto_config_httpv2`: boolean, auto configure HTTP2 where possible
- `nginx_fastcgi_fix_realpath`: boolean, use realpath for fastcgi (fix problems with symlinks and PHP opcache)

### Nginx Configuration

- `nginx_user`
- `nginx_worker_processes`
- `nginx_pid`: daemon pid file
- `nginx_events_*`: all variables in events block
- `nginx_http_*`: all variables in http block
- `nginx_custom_http`: instructions list (will put data in `/etc/nginx/conf.d/custom.conf`)

Fine configuration
------------------

[Vhost configuration](doc/vhost.md)

[PHP configuration](doc/php.md)

[Upstream Configuration](doc/upstream.md)

[SSL/TLS Configuration](doc/ssl.md)

[Basic Auth](doc/auth.md)

[FreeBSD](doc/freebsd.md)


Note
----

- Active support for Debian.
- FreeBSD support is experimental (no Travis). I only test (for the moment) 10.2 (but it can work on other versions).
- I don't manage BackupPC for FreeBSD (PR welcome).

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

