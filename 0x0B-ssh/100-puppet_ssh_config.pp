# Puppet to make changes to ssh configuration file

include stdlib
file_line { 'Turn off passwd auth':
  ensure             => 'present',
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => 'PasswordAuthentication',
  append_on_no_match => true
}

file_line { 'Declare identity file':
  ensure             => 'present',
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => 'IdentityFile',
  multiple           => true,
  append_on_no_match => true
}
