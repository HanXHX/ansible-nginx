# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set tabstop=2 :
# vi: set shiftwidth=2 :

Vagrant.configure("2") do |config|

  vms_debian = [
    { :name => "debian-jessie",           :box => "debian/jessie64",           :vars => { "nginx_php56": true,  "nginx_php70": false, "dotdeb": false, "nginx_backports": false }},
    { :name => "debian-jessie-backports", :box => "debian/jessie64",           :vars => { "nginx_php56": true,  "nginx_php70": false, "dotdeb": false, "nginx_backports": true  }},
    { :name => "debian-jessie-dotdeb",    :box => "debian/jessie64",           :vars => { "nginx_php56": true,  "nginx_php70": true,  "dotdeb": true,  "nginx_backports": false }},
    { :name => "debian-stretch",          :box => "sharlak/debian_stretch_64", :vars => { "nginx_php56": false, "nginx_php70": true,  "dotdeb": false, "nginx_backports": false }}
  ]

  vms_freebsd = [
		{ :name => "freebsd-10.2", :box => "freebsd/FreeBSD-10.2-STABLE" }
  ]

  config.vm.provider "virtualbox" do |v|
    v.cpus = 1
    v.memory = 256
  end

  vms_debian.each do |opts|
    config.vm.define opts[:name] do |m|
      m.vm.box = opts[:box]
      m.vm.network "private_network", type: "dhcp"
      m.vm.provision "ansible" do |ansible|
        ansible.playbook = "tests/test.yml"
        ansible.verbose = 'vv'
        ansible.sudo = true
				ansible.extra_vars = opts[:vars]
      end
    end
  end
  # See: https://forums.freebsd.org/threads/52717/
  vms_freebsd.each do |opts|
    config.vm.define opts[:name] do |m|
      m.vm.box = opts[:box]
      m.vm.network "private_network", type: "dhcp"
      m.vm.guest = :freebsd
      m.vm.synced_folder ".", "/vagrant", id: "vagrant-root", disabled: true
      m.ssh.shell = "sh"
      m.vm.base_mac = "080027D14C66"
      m.vm.provision "shell", inline: "pkg install -y python bash"
      m.vm.provision "ansible" do |ansible|
        ansible.playbook = "tests/test.yml"
        ansible.verbose = 'vv'
        ansible.sudo = true
        ansible.extra_vars = {
          ansible_python_interpreter: '/usr/local/bin/python'
        }
      end
    end
  end
end
