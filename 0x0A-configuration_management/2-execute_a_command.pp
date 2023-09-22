# kill a process named killmenow using exec 

exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
