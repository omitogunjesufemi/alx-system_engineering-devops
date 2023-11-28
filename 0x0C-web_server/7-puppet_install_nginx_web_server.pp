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

file_line { "default":
  path => "/etc/nginx/sites-enabled/default",
  line => "\tserver_name _;\n \trewrite ^/redirect_me$ http://x.com permanent;\n \trewrite ^/redirect_me/$ http://x.com permanent;",
  match => "server_name _;"
}
