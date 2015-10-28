# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
 
  config.vm.box = "trusty64"
  config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  config.vm.synced_folder '.', '/vagrant', nfs: true

  config.vm.define "megaawesome" do |megaawesome|
    megaawesome.vm.host_name = "megaawesome"
    megaawesome.vm.network "private_network", type: "dhcp"
    megaawesome.vm.provision "ansible" do |ansible|
        ansible.playbook = "megaawesome_provision.yml"
    end
  end
        
end