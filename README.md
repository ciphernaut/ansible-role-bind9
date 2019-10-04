# bind9

Role to install and configure BIND9.

## Requirements

- Ansible >= 2.7

### Supported platforms

```yml
- EL
  - 7
```

## Default role variables

| Name | Description | Type | Default | Required |
| -----| ----------- | :--: | :------:| :------: |
| bind__package_state | Whether to install a package or not | string | `present` | True |
| bind__listen | Defines the IP address(es) on which BIND will listen for incoming queries | string | `127.0.0.1` | True |
| bind__listen6 | Defines the IPv6 address(es) on which BIND will listen for incoming queries | string | `None` | True |
| bind__allow_query | Defines an match list of IP address(es) which are allowed to issue queries to the server | string | `localhost` | True |
| bind__allow_query_cache | Defines an address_match_list of IP address(es) which are allowed to issue queries that access the local cache | string | `None` | True |
| bind__recursion | Defines DNS query requests recursion behaviour | bool | `True` | True |
| bind__allow_recursion | Specifies which hosts are allowed to make recursive queries through this server | string | `None` | True |
| bind__allow_transfer | IP address(es) that are allowed to transfer (copy) the zone information from the server (master or slave for the zone) | string | `none` | True |
| bind__forwarders | Specifies the name servers (mostly of the provider) to which DNS requests should be forwarded if they cannot be resolved directly | list | `[]` | True |
| bind__auth_nxdomain | Whether to allow the server to answer authoritatively when returning NXDOMAIN | bool | `False` | True |
| bind__acl | BIND address match lists allowing control over what hosts or users may perform what operations on the name server | dict | `{}` | True |
| bind__version | Version of BIND | string | `none` | True |
| bind__dnssec_enable | Whether a secure DNS service is being used | bool | `True` | True |
| bind__dnssec_validation | Indicates that a resolver (a caching or caching-only name server) will attempt to validate replies from DNSSEC enabled (signed) zones | bool | `True` | True |
| bind__zone | zone field in named.conf DNS config file | dict | `{'.': {'type': 'hint', 'file': 'named.ca'}}` | True |
| bind__include | The 'include' statement reads the specified file at the point it is encountered (named.conf) | list | `['/etc/named.rfc1912.zones', '/etc/named.root.key']` | True |
| bind__zone_def_ttl | Time to Live value for the zone | int | `86400` | True |
| bind__zone_soa_def_refresh | The elapsed time after which the primary nameserver notifies secondary nameservers to refresh their database | int | `21600` | True |
| bind__zone_soa_def_retry | The time to wait after which a refresh fails before trying to refresh again | int | `3600` | True |
| bind__zone_soa_def_expire | The time after which the zone is no longer authoritative and the root nameservers must be queried | int | `604800` | True |
| bind__zone_soa_def_minttl | The amount of that time that other nameservers cache the zone’s information | int | `86400` | True |
| bind__zone_def_ns1 | Nameserver, specifies the system that provides DNS records for the domain | string | `127.0.0.1` | True |
| bind__zone_def_ns2 | Secondary Nameserver | string | `127.0.0.2` | True |
| bind__view | The view clause allows BIND to provide different functionality based on the hosts accessing it | dict | `{}` | True |
| bind__environmentfile_options | These additional options will be passed to named at startup. | list | `[]` | True |

**All default variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Static role variables

This section describes static variables implemented in the role.

### Main variables

| Name | Description | Type | Default |
| -----| ----------- | :--: | :-----: |
| bind__data_dir | Directory for all zone files. | string | `/var/named` |
| bind__group_name | Group name for bind | string | `named` |
| bind__user_name | User to run bind | string | `named` |

**All static main variables are described in [vars/main.yml](vars/main.yml) file.**

### centos variables

| Name | Description | Type | Default |
| -----| :---------: | :--: | ------- |
| bind__package_name | Package name to be installed | string | `bind` |
| bind__config_file | Configuration file for bind | string | `/etc/named.conf` |
| bind__service_name | Service name | string | `named` |
| bind__environment_file | File to be used by named deamon at boot time | string | `/etc/sysconfig/named` |

**All static centos variables are described in [vars/centos.yml](vars/centos.yml)**

## Example Playbook

```yaml
    - hosts: all
      become: true
      roles:
        - role: zerodowntime.bind9
```

## License

[Apache License 2.0](LICENSE)

## Support

ZeroDowntime Team <support@zdt.io>

For more information about the project, please visit https://www.zdt.io/building-blocks/.
