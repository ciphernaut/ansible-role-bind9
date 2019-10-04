import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bind_is_running_and_enabled(host):
    bind = host.service("named")
    assert bind.is_running
    assert bind.is_enabled


def test_named_dir(host):
    file = host.file("/var/named")
    assert file.exists
    assert file.is_directory
    assert file.mode == 0o2750
    assert file.group == 'named'
    assert file.user == 'root'


def test_named_data_runtime_dir_data(host):
    with host.sudo():
        file = host.file("/var/named/data")
        assert file.exists
        assert file.is_directory
        assert file.mode == 0o770
        assert file.group == 'named'
        assert file.user == 'named'


def test_named_data_runtime_dir_dynamic(host):
    with host.sudo():
        file = host.file("/var/named/dynamic")
        assert file.exists
        assert file.is_directory
        assert file.mode == 0o770
        assert file.group == 'named'
        assert file.user == 'named'


def test_named_data_runtime_dir_slaves(host):
    with host.sudo():
        file = host.file("/var/named/slaves")
        assert file.exists
        assert file.is_directory
        assert file.mode == 0o770
        assert file.group == 'named'
        assert file.user == 'named'


def test_check_zones(host):
    with host.sudo():
        file = host.file("/var/named/named.ca")
        assert file.exists
        assert file.is_file
        assert file.mode == 0o640
        assert file.group == 'named'
        assert file.user == 'root'
        assert file.contains('a.root-servers.net.')


def test_named_conf_file(host):
    with host.sudo():
        file = host.file("/etc/named.conf")
        assert file.exists
        assert file.is_file
        assert file.mode == 0o640
        assert file.group == 'named'
        assert file.user == 'root'
        assert file.contains('named.rfc1912.zones')
        assert file.contains('named.root.key')
        assert file.contains('zone "." IN {')


def test_environment_file(host):
    with host.sudo():
        file = host.file("/etc/sysconfig/named")
        assert file.exists
        assert file.is_file
        assert file.mode == 0o644
        assert file.group == 'root'
        assert file.user == 'root'
