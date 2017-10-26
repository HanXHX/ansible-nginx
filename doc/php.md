PHP
===

`nginx_php`:
  - `version`: (M) PHP version
  - `upstream_name` (O)
  - `sockets`: (O) socket list

If `sockets` is not provided, if uses local unix socket (based on PHP version).

You should see [Nginx upstream module doc](http://nginx.org/en/docs/http/ngx_http_upstream_module.html).

Each socket have:

- `unix`

XOR

- `host`
- `port`
- `weight`
- `max_fails`
- `fail_timeout`
