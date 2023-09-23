# This script sets up your client SSH configuration file

file { 'ssh_config':
  ensure  => present,
  path    => '~/.ssh/school',
  content => "Host *\n  PasswordAuthentication no\n  IdentityFile ~/.ssh/school\n"
}
