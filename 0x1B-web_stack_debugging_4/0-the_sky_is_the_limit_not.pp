
exec {'replace_limit':
  provider => shell,
  command  => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
}

exec {'restart_nginx':
  provider => shell,
  command  => 'service nginx restart',
}
