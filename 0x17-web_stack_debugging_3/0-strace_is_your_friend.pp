# Fixing a typo in the wordpress settings

exec { 'fix-wordpress':
  path    => '/usr/bin',
  command => 'sudo sed -i s/phpp/php/g var/www/html/wp-settings.php'
}
