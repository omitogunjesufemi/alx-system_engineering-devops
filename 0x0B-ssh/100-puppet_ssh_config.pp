# Puppet to make changes to ssh configuration file

$config_str = "Host *
IdentityFile ~/.ssh/school
PasswordAuthentication no
"

file { 'ssh_config':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config_',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => $config_str
}
