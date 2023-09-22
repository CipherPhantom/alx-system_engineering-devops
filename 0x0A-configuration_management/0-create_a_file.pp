# This script create a file in /tmp.

file { 'create a file':
  ensure  => present,
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
