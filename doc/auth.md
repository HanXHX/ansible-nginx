Auth Basic management
=====================

Description
-----------

Auth basic is managed in a separate list. Each auth file can be shared between locations or vhosts.

Each htpasswd has few keys:

- `name`: (M) used to create file and as pointee
- `description`: (M) Used for the message box :)
- `users`: each users is composed with 3 keys: `name` (M), `password` (M) and `state` (O) present/absent (default: present)
- `state`: (O) present or absent. Default: present

`nginx_htpasswd` should be placed in a vault file.

Example
-------

```yaml
nginx_vhosts:
# htpasswd on all vhost
  - name: test.local
    htpasswd: 'hello'
    template: '_base'

# htpasswd only in /hello
  - name: test-location.local
    template: '_base'
    location:
      '/hello':
        - htpasswd: 'hello'

nginx_htpasswd:
  - name: 'hello'
    description: 'Please login!'
    users:
      - name: 'bob'
        password: 'my_pass'
```
