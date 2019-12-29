# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set tabstop=2 :
# vi: set shiftwidth=2 :

Vagrant.configure("2") do |config|

  vms_debian = [
    { :name => "debian-stretch", :box => "debian/stretch64", :vars => {} },
    { :name => "debian-buster", :box => "debian/buster64", :vars => {} }
  ]

  vms_freebsd = [
    { :name => "freebsd-11", :box => "freebsd/FreeBSD-11.3-STABLE", :vars => {} },
    { :name => "freebsd-12", :box => "freebsd/FreeBSD-12.1-STABLE", :vars => {} }
  ]

  conts = [
    { :name => "docker-debian-stretch", :docker => "hanxhx/vagrant-ansible:debian9", :vars => {} },
    { :name => "docker-debian-buster", :docker => "hanxhx/vagrant-ansible:debian10", :vars => {} },
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
        ansible.extra_vars = opts[:vars].merge({ "nginx_debug_role": true, is_docker: true })
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
    config.vm.base_mac = "080027D14C66"
    config.vm.define opts[:name] do |m|
      m.vm.box = opts[:box]
      m.vm.provider "virtualbox" do |v, override|
        override.ssh.shell = "csh"
        v.cpus = 2
        v.memory = 512
      end
      m.vm.provision "shell", inline: "[ -e /usr/local/bin/bash ] || pkg install -y python bash"
      m.vm.provision "ansible" do |ansible|
        ansible.playbook = "tests/test.yml"
        ansible.verbose = 'vv'
        ansible.become = true
        ansible.extra_vars = opts[:vars].merge({ "nginx_debug_role": true, "ansible_python_interpreter": '/usr/local/bin/python' })
      end
    end
  end

end
