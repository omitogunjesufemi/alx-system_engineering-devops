# Puppet automation to configure web-02 to be identical to web-01
include stdlib

package { 'nginx':
  ensure => 'installed'
}

$str="        server_name _;
        add_header X-Served-By \"${hostname}\";

"

file_line { 'redirection_server':
  path  => '/etc/nginx/sites-enabled/default',
  line  => $str,
  match => '^\s*server_name _;.*$',
  after => '^\s*server_name _;.*$'
}

exec { 'restart nginx':
  path    => '/usr/bin',
  command => 'sudo service nginx restart',
  require => [Package['nginx'], File_line['redirection_server']]
}
