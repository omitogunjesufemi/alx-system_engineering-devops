# Installing flask from pip3 using Puppet

package { 'flask':
  ensure   => 'installed',
  provider => 'pip3',
}
