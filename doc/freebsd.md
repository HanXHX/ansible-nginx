Freebsd
=======

Limitations
-----------

Due to Ansible + FreeBSD limitations (`ansible_processor_vcpus`), You must explicitely set `nginx_worker_processes`.

About modules
-------------

Dynamic modules must be set with full path (see `nginx_load_modules` path).
