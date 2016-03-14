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

This list have 3 mandatory keys:

- `name`: MUST be unique

- `key`: content of the private key
- `cert`: content of the public key

OR

- `dest_cert`: remote path where certificate is located
- `dest_key`: remote path where key is located

Note: `name` is used to deploy key/cert. With defaults values dans `name` = "foo", key is -> /etc/nginx/ssl/foo/foo.key

Tips
----

Deploying key/cert is not mandatory with this role. You can manage it in other place ([letsencrypt](https://letsencrypt.org/)? :)). You just need to set `dest_cert` and `dest_key`!

Diffie-Hellman
--------------

If you do not specify any dh param, this role auto generates it.

Example
-------

```yaml
nginx_vhosts;
  - name: 'test-ssl.local'
    proto: ['http', 'https']
    template: '_base'
    ssl_name: 'mysuperkey'

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
```

