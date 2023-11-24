# Create a manifest that kills a process named killmenow

exec { 'kill process killmenow':
  path    => '/usr/bin',
  command => 'pkill killmenow'
}
