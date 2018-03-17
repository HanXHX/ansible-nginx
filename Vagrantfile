# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set tabstop=2 :
# vi: set shiftwidth=2 :

Vagrant.configure("2") do |config|

  vms_debian = [
    { :name => "debian-jessie", :box => "debian/jessie64", :vars => { "nginx_php": [{"version": "5.6"}] }},
    { :name => "debian-jessie-backports", :box => "debian/jessie64", :vars => { "nginx_php": [{"version": "5.6"}], "nginx_backports": true }},
    { :name => "debian-jessie-dotdeb", :box => "debian/jessie64", :vars => { "nginx_php": [{"version": "7.0"}, {"version": "5.6", "upstream_name": "legacy"} ], "dotdeb": true }},
    { :name => "debian-stretch", :box => "debian/stretch64", :vars => { "nginx_php": [{"version": "7.0"}] }},
    { :name => "debian-stretch-sury", :box => "debian/stretch64", :vars => { "nginx_php": [{"version": "7.1"}], "sury": true }}
  ]

  vms_freebsd = [
    { :name => "freebsd-11", :box => "freebsd/FreeBSD-11.1-STABLE",  :vars => {} },
    { :name => "freebsd-12", :box => "freebsd/FreeBSD-12.0-CURRENT", :vars => {} }
  ]

  conts = [
    { :name => "docker-debian-jessie", :docker => "hanxhx/vagrant-ansible:debian8", :vars => { "nginx_php" => [{"version" => "5.6"}] }},
    { :name => "docker-debian-jessie-backports", :docker => "hanxhx/vagrant-ansible:debian8", :vars => { "nginx_php": [{"version": "5.6"}], "nginx_backports": true }},
    { :name => "docker-debian-jessie-dotdeb", :docker => "hanxhx/vagrant-ansible:debian8", :vars => { "nginx_php": [{"version": "7.0"}, {"version": "5.6", "upstream_name": "legacy"} ], "dotdeb": true }},
    { :name => "docker-debian-stretch", :docker => "hanxhx/vagrant-ansible:debian9", :vars => { "nginx_php": [{"version": "7.0"}] }},
    { :name => "docker-debian-stretch-sury", :docker => "hanxhx/vagrant-ansible:debian9", :vars => { "nginx_php": [{"version": "7.1"}], "sury": true }}
  ]

  config.vm.network "private_network", type: "dhcp"
  config.vm.synced_folder ".", "/vagrant", id: "vagrant-root", disabled: true

  conts.each do |opts|
    config.vm.define opts[:name] do |m|
      m.vm.provider "docker" do |d|
        d.image = opts[:docker]
        d.remains_running = true
        d.has_ssh = true
      end
      m.vm.provision "ansible" do |ansible|
        ansible.playbook = "tests/test.yml"
        ansible.verbose = 'vv'
        ansible.become = true
        ansible.extra_vars = opts[:vars].merge({ "nginx_debug_role": true })
      end
    end
  end

  vms_debian.each do |opts|
    config.vm.define opts[:name] do |m|
      m.vm.box = opts[:box]
      m.vm.provider "virtualbox" do |v|
        v.cpus = 1
        v.memory = 256
      end
      m.vm.provision "ansible" do |ansible|
        ansible.playbook = "tests/test.yml"
        ansible.verbose = 'vv'
        ansible.become = true
        ansible.extra_vars = opts[:vars].merge({ "nginx_debug_role": true })
      end
    end
  end

  vms_freebsd.each do |opts|
    config.ssh.shell = "csh"
    config.vm.base_mac = "080027D14C66"
    config.vm.define opts[:name] do |m|
      m.vm.box = opts[:box]
      m.vm.provider "virtualbox" do |v|
        v.cpus = 2
        v.memory = 512
      end
      m.vm.provision "shell", inline: "pkg install -y python bash"
      m.vm.provision "ansible" do |ansible|
        ansible.playbook = "tests/test.yml"
        ansible.verbose = 'vv'
        ansible.become = true
        ansible.extra_vars = opts[:vars].merge({ "nginx_debug_role": true, "ansible_python_interpreter": '/usr/local/bin/python' })
      end
    end
  end

end
