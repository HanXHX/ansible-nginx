SSL/TLS Management
==================

You can put all this variables in a separated vault file.

Variables
---------

- `nginx_dh`: DH content
- `nginx_dh_length`: DH key length (default is 2048)
- `nginx_dh_path`: file localation
- `nginx_ssl_dir`: directory where you install your SSL/TLS keys
- `nginx_ssl_pairs`

Cert/Key pairs
--------------

Each pair must have a `name`.
Note: `name` is used to deploy key/cert. With defaults values dans `name` = "foo", key is -> /etc/nginx/ssl/foo/foo.key

### Content mode

Key/Cert content is stored in variable. Usefull with vault.

- `key`: content of the private key
- `cert`: content of the public key

### Remote file

You can use these variables if you use another task/role to manages your certificates.

- `dest_cert`: remote path where certificate is located
- `dest_key`: remote path where key is located

### Self signed

Create a self-signed pair and deploy it. Do not use this feature in production.

- `self_signed`: set true to use this featrure
- `force`: optional feature (default: false), force regen pair (not idempotent)

### Acme

Uses acme.sh to create free certificates. It uses HTTP-01 challenge. Use this feature for standalone servers.

- `acme`: set true to use this feature. It uses `name` (can be a string or string list).

Have a look to [acme configuratuion](acme.md configuration).

Tips
----

- In `nginx_sites`, `ssl_name` is mandatory. This role will search in `nginx_ssl_pairs` with site `name` (first in list if it's a list).  

Diffie-Hellman
--------------

If you do not specify any dh param, this role auto generates it.

Example
-------

```yaml
nginx_sites;
  - name: 'test-ssl.local'
    proto: ['http', 'https']
    template: '_base'
    ssl_name: 'mysuperkey'
  - name: 'test-ssl2.local'
    proto: ['http', 'https']
    template: '_base'
  - name: 'test-ssl3.local'
    proto: ['http', 'https']
    template: '_base'
  - name: 'test-self-signed.local'
    proto: ['http', 'https']
    template: '_base'
    ssl_name: 'this.is.self.signed'

nginx_ssl_pairs:
  - name: mysuperkey
    key: |
      -----BEGIN RSA PRIVATE KEY-----
      ....(snip)....
      -----END RSA PRIVATE KEY-----
    cert: |
      -----BEGIN CERTIFICATE-----
      ....(snip)....
      -----END CERTIFICATE-----
  - name: test-ssl2.local
    acme: true
  - name: this.is.self.signed
    self_signed: true
    force: false
```

