# puppet manifest to configure web server

# update software packages list
exec { 'dist update':
    command  => '/usr/bin/apt-get update',
    provider => 'shell'
}

package { 'nginx':
    ensure  => 'installed',
    require => Exec['dist update']
}

# allow HTTP
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

# create index html file
file {'/var/www/html/index.html':
    path    => '/var/www/html/index.html',
    content => 'Hello World!',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '7624'
}

exec {'redirect_me':
    command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
    provider => 'shell'
}


# add error and redirection page
file { 'Nginx default config file':
    ensure  => file,
    path    => '/etc/nginx/sites-enabled/default',
    content =>
    "server {
        listen 80 default_server;
        listen [::]:80 default_server;
            root /var/www/html;
        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }
        error_page 404 /404.html;
        location  /404.html {
            internal;
        }
    }
    ",
}

# restart nginx
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}


service {'nginx':
    ensure  => running,
    require => Package['nginx']
}