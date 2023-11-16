exec {'replace_limit-hard':
  provider => shell,
  command  => 'sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
}

exec {'replace_limit-soft':
  provider => shell,
  command  => 'sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
