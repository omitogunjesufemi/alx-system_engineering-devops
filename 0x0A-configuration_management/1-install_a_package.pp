# Installing flask from pip3 using Puppet

package { 'python3-pip':
  ensure   => 'installed'
}

package { 'flask':
  ensure   => 'installed',
  provider => 'pip3',
  require  => Package['python3-pip']
}

package { 'werkzeug':
  ensure   => 'installed',
  provider => 'pip3',
  require  => Package['python3-pip']
}
