# Fabfile to:
#    - update the remote system(s)
#    - download and install an application

# Import Fabric's API module
from fabric.api import *

# Set the hosts
env.hosts = [
    '18.206.232.73',  # Web server 1
    '54.172.247.161', # Web server 2
]

# Set the username
env.user = "root"

# Set the private key file
env.key_filename = "/root/.ssh/id_rsa"

def update_upgrade():
    """
    Update the default OS installation's basic default tools.
    """
    run("aptitude update")
    run("aptitude -y upgrade")

def install_memcached():
    """
    Download and install memcached.
    """
    run("aptitude install -y memcached")

def update_install():
    # Update
    update_upgrade()
    
    # Install
    install_memcached()
