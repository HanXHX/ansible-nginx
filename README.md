Nginx for Debian/Ubuntu Ansible role
=====================================

[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-HanXHX.nginx-blue.svg)](https://galaxy.ansible.com/HanXHX/nginx/) ![GitHub Workflow Status (master branch)](https://img.shields.io/github/actions/workflow/status/hanxhx/ansible-nginx/molecule.yml?branch=master)

Install and configure Nginx on Debian/Ubuntu.

Features:

- SSL/TLS "hardened" support
- Manage basic auth on site / location
- Proxy + Upstream
- Fast PHP configuration
- Preconfigured site templates (should work on many app)
- Auto-configure HTTP2 on SSL/TLS sites
- Manage dynamic modules (install and loading)
- Deploy custom facts.d with sites config
- Can listen with proxy protocol
- Generate certificates with acme.sh (let's encrypt) -- *EXPERIMENTAL*

Supported OS:

| OS                   | Working | Stable (active support)                                                                              |
|----------------------|---------|------------------------------------------------------------------------------------------------------|
| Debian Jessie (8)    | Yes     | Check latest supported version ([1.5.0](https://github.com/HanXHX/ansible-nginx/releases/tag/1.5.0)) |
| Debian Stretch (9)   | Yes     | Check latest supported version ([1.9.0](https://github.com/HanXHX/ansible-nginx/releases/tag/1.9.0)) | 
| Debian Buster (10)   | Yes     | Yes                                                                                                  |
| Debian Bullseye (11) | Yes     | Yes                                                                                                  |
| Debian Bookworm (12) | Yes     | Not yet :)                                                                                           |
| Ubuntu 20.04         | Yes     | Yes                                                                                                  |
| Ubuntu 22.04         | Yes     | Yes                                                                                                  |

Requirements
------------

- Ansible >=2.11
- If you set true to `nginx_backports`, you must install backports repository before lauching this role.

Role Variables
--------------

### Packaging

Debian:

- `nginx_apt_package`: APT nginx package (try: apt-cache search ^nginx)
- `nginx_backports`: Install nginx from backport repository (bool)

### Shared

- `nginx_root`: root directory where you want to have your files
- `nginx_log_dir`: log directory (if you change it, don't forget to change logrotate config)
- `nginx_resolver`: list of DNS resolver (default: OpenDNS)
- `nginx_error_log_level`: default log level
- `nginx_auto_config_httpv2`: boolean, auto configure HTTP2 where possible
- `nginx_fastcgi_fix_realpath`: boolean, use realpath for fastcgi (fix problems with symlinks and PHP opcache)
- `nginx_default_hsts`: string, default header sent for HSTS

### Nginx Configuration

- `nginx_user`
- `nginx_worker_processes`
- `nginx_pid`: daemon pid file
- `nginx_events_*`: all variables in events block
- `nginx_http_*`: all variables in http block
- `nginx_custom_core`: instructions list (for core, will put data in `/etc/nginx/nginx.conf`)
- `nginx_custom_http`: instructions list (will put data in `/etc/nginx/conf.d/custom.conf`)
- `nginx_module_packages`: package list module to install (Debian)

### Misc

- `nginx_debug_role`: set _true_ if you need to see output of no\_log tasks

About modules
-------------

Last updates from Debian backports loads modules from /etc/nginx/modules-enabled directory. Disabling/Enabling is not supported anymore. Please wait further update.

Fine configuration
------------------

[Site configuration](doc/site.md)

[PHP configuration](doc/php.md)

[Upstream Configuration](doc/upstream.md)

[SSL/TLS Configuration](doc/ssl.md)

[Basic Auth](doc/auth.md)

[acme.sh](doc/acme.md)

Note
----

- Active support for Debian/Ubuntu.

Dependencies
------------

See: [requirements.yml](requirements.yml).


If you need to dev this role locally with molecule
--------------------------------------------------

Check available scenarios in [molecule](molecule) directory.

With `debian-12` scenario:

```commandline
molecule -v -c molecule/_shared/base.yml verify -s debian-12
```

License
-------

GPLv2


Donation
--------

If this code helped you, or if you’ve used them for your projects, feel free to buy me some :beers:

- Bitcoin: `1BQwhBeszzWbUTyK4aUyq3SRg7rBSHcEQn`
- Ethereum: `63abe6b2648fd892816d87a31e3d9d4365a737b5`
- Litecoin: `LeNDw34zQLX84VvhCGADNvHMEgb5QyFXyD`
- Monero: `45wbf7VdQAZS5EWUrPhen7Wo4hy7Pa7c7ZBdaWQSRowtd3CZ5vpVw5nTPphTuqVQrnYZC72FXDYyfP31uJmfSQ6qRXFy3bQ`

No crypto-currency? :star: the project is also a way of saying thank you! :sunglasses:

Author Information
------------------

- Twitter: [@hanxhx_](https://twitter.com/hanxhx_)

