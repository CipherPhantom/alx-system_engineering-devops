#This script installs nginx and configures the server

exec { 'Server Config':
  provider => shell;
  command => 'sudo apt-get -y update; sudo apt-get -y install nginx; echo "Hello World!" > /var/www/html/index.html; sudo sed -i -r "s/^}$/\tlocation \/redirect_me {\n\t\treturn 301 https:\/\/www.youtube.com\/watch\?v=QH2-TGUlwu4;\n\t}\n}/" /etc/nginx/sites-available/default; sudo service nginx restart',
}
