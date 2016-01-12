PHP
===

- `nginx_php`: boolean if you need to preconfigure PHP (default: false)
- `nginx_php_sockets`: list of sockets (see bellow)

You should see [Nginx upstream module doc](http://nginx.org/en/docs/http/ngx_http_upstream_module.html).

Each socket have:

- `unix_socket`
- `host`
- `port`
- `weight`
- `max_fails`
- `fail_timeout`

