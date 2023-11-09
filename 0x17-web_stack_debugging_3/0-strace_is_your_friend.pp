# Puppet manuscript to replace a line in file on server

$edit_this_file = '/var/www/html/wp-settings.php'

#this will replace line containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${edit_this_file}",
  path    => ['/bin','/usr/bin']
}
