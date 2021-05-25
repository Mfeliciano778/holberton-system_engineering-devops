# increase ULIMIT of default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/5000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->
# NGINX restart
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
