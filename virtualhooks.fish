set -gx SALT_CONFIG_DIR $VIRTUAL_ENV/salt
set -gx DJANGO_SETTINGS_MODULE settings.development
set -gx PYTHONPATH $VIRTUAL_ENV/web/web $PYTHONPATH

cdvirtualenv

function saltwatcher
  cdvirtualenv
  cd salt/srv
  watchmedo tricks tricks.yaml
end  