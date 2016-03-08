# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set tabstop=2 :
# vi: set shiftwidth=2 :

Vagrant.configure("2") do |config|

  vms = [
    [ "freebsd-10.2", "freebsd/FreeBSD-10.2-STABLE" ],
    [ "debian-wheezy", "debian/wheezy64" ],
    [ "debian-jessie", "debian/jessie64" ],
    [ "debian-stretch", "sharlak/debian_stretch_64" ]
  ]

  config.vm.provider "virtualbox" do |v|
    v.cpus = 1
    v.memory = 256
  end

  vms.each do |vm|
    config.vm.define vm[0] do |m|
      m.vm.box = vm[1]
      m.vm.network "private_network", type: "dhcp"

      # See: https://forums.freebsd.org/threads/52717/
      if vm[0] = "freebsd-10.2"
        m.vm.guest = :freebsd
        m.vm.synced_folder ".", "/vagrant", id: "vagrant-root", disabled: true
        m.ssh.shell = "sh"
        #m.vm.base_mac = "0800278DFFF5"
        m.vm.base_mac = "080027D14C66"
        #m.vm.network "public_network", bridge: 'enp4s0', auto_config: false
        m.vm.provision "shell", inline: "pkg install -y python bash"
      end

      m.vm.provision "ansible" do |ansible|
        ansible.playbook = "tests/test.yml"
        ansible.groups = { "test" => [ vm[0] ] }
        ansible.verbose = 'vv'
        ansible.sudo = true
        if vm[0] = "freebsd-10.2"
          ansible.extra_vars = {
            ansible_python_interpreter: '/usr/local/bin/python'
          }
        end
      end
    end
  end
end
