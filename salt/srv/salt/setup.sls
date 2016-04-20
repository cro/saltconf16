{{ pillar['PROJECT_DIR']}}/web/web/settings/common.py:
  file.managed:
    - source: salt://files/common.py
    - template: jinja

{{ pillar['PROJECT_DIR'] }}/web/web/settings/development.py:
  file.managed:
    - source: salt://files/development.py
    - template: jinja

{{ pillar['PROJECT_DIR'] }}/web/web/settings/production.py:
  file.managed:
    - source: salt://files/production.py
    - template: jinja

{{ pillar['PROJECT_DIR'] }}/web/web/settings/staging.py:
  file.managed:
    - source: salt://files/staging.py
    - template: jinja
