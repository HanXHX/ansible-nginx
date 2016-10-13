#!/bin/sh

# Thanks to https://servercheck.in/blog/testing-ansible-roles-travis-ci-github

DIR=$( dirname $0 )
PLAYBOOK="$DIR/test.yml"


set -ev

ANSIBLE_VARS="{ nginx_php56: $NGINX_PHP56, nginx_php70: $NGINX_PHP70, nginx_backports: $NGINX_BACKPORTS, dotdeb: $DOTDEB }"

echo $ANSIBLE_VARS

# Check syntax
ansible-playbook -i localhost, -c local --syntax-check -vv $PLAYBOOK

# Check role
ansible-playbook -i localhost, -c local -e "$ANSIBLE_VARS" --sudo -vv $PLAYBOOK

# Check indempotence
ansible-playbook -i localhost, -c local -e "$ANSIBLE_VARS" --sudo -vv $PLAYBOOK \
| grep -q 'changed=0.*failed=0' \
&& (echo 'Idempotence test: pass' && exit 0) \
|| (echo 'Idempotence test: fail' && exit 1)
