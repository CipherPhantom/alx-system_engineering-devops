#This script installs nginx and configures the server

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}

exec { 'sed':
  provider => shell,
  command  => 'sed -i -r "s/^}$/\tlocation \/redirect_me {\n\t\treturn 301 https:\/\/www.youtube.com\/watch\?v=QH2-TGUlwu4;\n\t}\n}/" /etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
