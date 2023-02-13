import os

def install_samba():
    os.system(f"sudo apt-get -y update")
    os.system(f"sudo apt-get -y install samba samba-common-bin")
    os.system(f"sudo apt-get -y autoremove")

def configure_samba(shared_path, username):
    # Create a backup of the original Samba configuration file
    os.system(f"sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bak")
    # Create a new Samba configuration file
    with open(f"/etc/samba/smb.conf", 'w') as f:
        f.write(f"[global]\n")
        f.write(f"workgroup = WORKGROUP\n")
        f.write(f"server string = Samba Server %v\n")
        f.write(f"netbios name = ubuntu_nas\n")
        f.write(f"security = user\n")
        f.write(f"map to guest = bad user\n")
        f.write(f"\n")
        f.write(f"[nas]\n")
        f.write(f"path = {shared_path}\n")
        f.write(f"browsable = yes\n")
        f.write(f"writable = yes\n")
        f.write(f"guest ok = yes\n")
        f.write(f"read only = no\n")
    # Create the shared directory
    os.system(f"sudo mkdir -p {shared_path}")
    os.system(f"sudo chown -R {username}:{username} {shared_path}")
    # Restart the Samba service
    os.system(f"sudo service smbd restart")

def create_user(username, password):
    # Create the Linux user account
    os.system(f"sudo useradd {username}")
    os.system(f"echo {username}:{password} | sudo chpasswd")
    # Create the Samba user account
    os.system(f"sudo smbpasswd -a {username}")

if __name__ == "__main__":
    install_samba()
    shared_path = "/home/"
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    configure_samba(shared_path, username)
    create_user(username, password)
