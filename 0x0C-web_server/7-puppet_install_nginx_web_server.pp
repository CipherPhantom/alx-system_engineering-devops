#This script installs nginx and configures the server

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\n\troot /var/www/html;\n\n\tserver_name _;\n\n\tindex index.html index.htm index.nginx-debian.html;\n\n\tlocation / {\n\t\ttry_files \$uri \$uri/ =404;\n\t}\n\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n}",
}
