PHP
===

`nginx_php`:
  - `upstream_name` (M)
  - `sockets`: (O) socket list

If `sockets` is not provided, if uses local unix socket (based on PHP version).

You should see [Nginx upstream module doc](http://nginx.org/en/docs/http/ngx_http_upstream_module.html).

Each socket have:

- `unix`

XOR

- `host` (M)
- `port` (M)
- `weight` (O)
- `max_fails` (O)
- `fail_timeout` (O)
