# Puppet manifest to configure the nginx server

include stdlib

package { 'nginx':
  ensure => 'installed'
}

file { 'index.html':
  path => "/var/www/html/index.html",
  content => "Hello World!\n",
  require => Package['nginx']
}

exec { 'redirection':
  path => '/usr/bin/',
  command => "sudo sed -i 's|^[^#].*server_name.*;|\\tserver_name _;\\n\\trewrite ^/redirect_me$ http://x.com permanent;\\n\\trewrite ^/redirect_me/$ http://x.com permanent;|' /etc/nginx/sites-enabled/default;",
}
