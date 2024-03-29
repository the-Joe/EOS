# EOS - Eye of Sauron
<img src="eye.png" style="width:250px;height:250px;">

Connect your Statuspage.io Dashboard and other 3rd party webhook-enabled services to Slack. Automate Slack Channel member interactions. EOS is a Python application built for bi-directional communication between internal systems, SaaS Platforms and Internal users that processes slash commands and written language in Slack as well as WebHooks from external sources. Alerting frequency can be tuned to your businesses needs based on 3rd party service activity status or type.

## Dependencies

- Python 3.10.6
- Slack
- Statuspage.io

## Packages

      Package                Version
      ---------------------- ---------------
      attrs                  21.2.0
      Automat                20.2.0
      Babel                  2.8.0
      bcrypt                 3.2.0
      blinker                1.4
      certifi                2020.6.20
      chardet                4.0.0
      click                  8.0.3
      cloud-init             22.2
      colorama               0.4.4
      command-not-found      0.3
      configobj              5.0.6
      constantly             15.1.0
      cryptography           3.4.8
      dbus-python            1.2.18
      distro                 1.7.0
      distro-info            1.1build1
      ec2-hibinit-agent      1.0.0
      Flask                  2.1.2
      hibagent               1.0.1
      httplib2               0.20.2
      hyperlink              21.0.0
      idna                   3.3
      importlib-metadata     4.6.4
      incremental            21.3.0
      itsdangerous           2.1.2
      jeepney                0.7.1
      Jinja2                 3.0.3
      jsonpatch              1.32
      jsonpointer            2.0
      jsonschema             3.2.0
      keyring                23.5.0
      launchpadlib           1.10.16
      lazr.restfulclient     0.14.4
      lazr.uri               1.0.6
      MarkupSafe             2.0.1
      more-itertools         8.10.0
      netifaces              0.11.0
      oauthlib               3.2.0
      pexpect                4.8.0
      pip                    22.0.2
      ptyprocess             0.7.0
      pyasn1                 0.4.8
      pyasn1-modules         0.2.1
      PyGObject              3.42.1
      PyHamcrest             2.0.2
      PyJWT                  2.3.0
      pyOpenSSL              21.0.0
      pyparsing              2.4.7
      pyrsistent             0.18.1
      pyserial               3.5
      python-apt             2.3.0+ubuntu2.1
      python-debian          0.1.43ubuntu1
      pytz                   2022.1
      PyYAML                 5.4.1
      requests               2.25.1
      SecretStorage          3.3.1
      service-identity       18.1.0
      setuptools             59.6.0
      six                    1.16.0
      slack-bolt             1.14.0
      slack-sdk              3.16.2
      sos                    4.3
      ssh-import-id          5.11
      systemd-python         234
      Twisted                22.1.0
      ubuntu-advantage-tools 27.10
      ufw                    0.36.1
      unattended-upgrades    0.1
      urllib3                1.26.5
      wadllib                1.3.6
      Werkzeug               2.1.2
      wheel                  0.37.1
      zipp                   1.0.0
      


## Environment

- AWS t2.micro EC2 Instance
- Ubuntu 22.04.1 LTS

## Installation

- Copy source files to directory of your choice '<dir>'
- Update eos_access.py with your own 'SLACK_BOT_TOKEN' and 'SLACK_SIGNING_SECRET' - be sure to safeguard these credentials.
- Run '<dir>/make install'
- 'systemctl start eos'
- 'systemctl enable eos'

## Usage

- Accepts webhooks related to status updates from 3rd party providers
- Announces status in defined channels
- Discrete pattern match interaction with Slack channel members

#### Demo Status Page
![Demo Status Page](img2.png)

#### Expanded Status Page Detail
![Expanded Status Page Detail](img3.png)

#### Slack alerting of statuspage activity
![Slack alerting of statuspage activity](img4.png)

#### Incident / Maintenance Notification
![Incident / Maintenance Notification](img5.png)

#### EOS can perform pattern match interactions with channel members. Various applications including Slack etiquette, policy, etc.
![EOS can perform pattern match interactions with channel members. Various applications including Slack etiquette, policy, etc.](img6.png)

#### EOS can discretely intervene or publicly. It's your choice given any situation. Member interactions can be tailored for bi-directinoal webhook action to support escalation, logging, etc.
![EOS can discretely intervene or publicly. It's your choice given any situation. Member interactions can be tailored for bi-directinoal webhook action to support escalation, logging, etc.](img7.png)

      
      
// (c) 2023 Vetere
// This code is licensed under MIT license (see license.txt for details)
