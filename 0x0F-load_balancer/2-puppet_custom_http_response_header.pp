# Puppet automation to configure web-02 to be identical to web-01
include stdlib

package { 'nginx':
  ensure => 'installed'
}

file_line { 'adding header':
  path  => '/etc/nginx/sites-enabled/default',
  line  => 'add_header X-Served-By $hostname;',
  after => 'listen 80 default server'
}

exec { 'restart nginx':
  path    => '/usr/bin',
  command => 'sudo service nginx restart',
  require => [Package['nginx'], File_line['adding header']]
}
