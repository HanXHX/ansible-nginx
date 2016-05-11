Upstream management
===================

`nginx_upstreams`: List of dict. An upstream has few keys. See bellow.

Note: Few params are unavailable on old Nginx version. But this role do _not_ put it if your version is too old!

Upstream params
---------------

- `name`: upstream name. Can be use in vhost with *proxy_pass http://upstream_name*
- `params`: list of param (hash, zone...)
- `servers`: each upstream MUST have at least 1 server
- `state`: Optional. Can be 'absent' or 'present'

Server params
-------------

You must set a `path`. For example: *192.168.0.50:8080* or *unix:/tmp/my.sock*.

All this params are optional. You should see [Nginx upstream doc](http://nginx.org/en/docs/http/ngx_http_upstream_module.html).

- `weight`
- `max_fails`
- `fail_timeout`
- `backup`
- `down`
- `route`
- `slow_start`

Example
-------

```yaml
nginx_upstreams:
  - name: 'proxy_apache'
    servers:
      - path: '127.0.0.1:80'
        max_conns: 150
        weight: 10
        down: false
    state: 'present'
```
