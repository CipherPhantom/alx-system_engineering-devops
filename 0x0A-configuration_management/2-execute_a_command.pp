# This script kills a process named killmenow

exec { 'command':
  command => '/bin/pkill "killmenow"'
}
