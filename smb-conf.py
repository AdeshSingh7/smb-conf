#!/usr/bin/python3
import os

def install_samba():
    os.system(f"sudo apt-get -y update")
    os.system(f"sudo apt-get -y install samba samba-common samba-common-bin")
    #os.system(f"sudo apt-get -y install --reinstall gvfs-backends")
    os.system(f"sudo apt-get -y autoremove")

def configure_samba(username,shared_path):
    # Create the Samba user account
    os.system(f"sudo smbpasswd -a {username}")
    # Create a backup of the original Samba configuration file
    os.system(f"sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.bak")
    # Create a new Samba configuration file
    with open(f"/etc/samba/smb.conf", 'w') as f:
        f.write(f"[global]\n")
        f.write(f"workgroup = WORKGROUP\n")
        f.write(f"server string = Samba Server %v\n")
        f.write(f"netbios name = smb_server\n")
        f.write(f"security = user\n")
        f.write(f"map to guest = bad user\n")
        f.write(f"\n")
        f.write(f"[Shared]\n")
        f.write(f"path = {shared_path}\n")
        f.write(f"browsable = yes\n")
        f.write(f"writable = yes\n")
        f.write(f"guest ok = yes\n")
        f.write(f"read only = no\n")
    # Create the shared directory
    # os.system(f"sudo mkdir -p {shared_path}")
    # Restart the Samba service
    os.system(f"sudo service smbd restart")

if __name__ == "__main__":
    try:
        install_samba()
        username = input("Enter a username: ")
        shared_path = input("Shared folder location: ")
        configure_samba(username,shared_path)
    except KeyboardInterrupt:pass
    except Exception:pass
    finally:os.system("clear")
