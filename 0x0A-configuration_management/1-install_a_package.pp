# Installing flask from pip3 using Puppet

package { 'flask':
  ensure   => 'installed',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => 'installed',
  provider => 'pip3',
}
