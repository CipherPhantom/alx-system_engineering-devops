# This script installs nginx and configures the server

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

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page",
}

exec { 'sed':
  provider => shell,
  command  => 'sed -i -r "s/^}$/\n\terror_page 404 \/404.html;\n\tlocation \/404.html {\n\t\tinternal;\n\t}\n}/" /etc/nginx/sites-available/default',
}

exec { 'sed':
  provider => shell,
  command  => 'sed -i "/^\troot/i \ \tadd_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
