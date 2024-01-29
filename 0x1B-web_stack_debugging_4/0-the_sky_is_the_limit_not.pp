# increased the max number of files opened by nginx

exec {'nofiles':
  command => "sudo sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/g' /etc/default/nginx",
  path    => '/usr/local/bin/:/bin/',
}
