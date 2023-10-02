# This script installs nginx and configures the server

exec { 'apt update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt update'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}

file_line { 'http header':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  line     => '\tlocation / {\n\t\tadd_header X-Served-By $hostname;',
  match    => '^\tlocation / {',
  multiple => false,
  require  => Package['nginx'],
  notify   => Service['nginx'],
}
