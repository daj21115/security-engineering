import paramiko  # This is the library that lets Python talk SSH.

# --- 1. SETTINGS ---
# We use 127.0.0.1 because of the "Bridge" (Port Proxy) we built in PowerShell.
# --- CONFIGURATION (REDACTED FOR GITHUB) ---
host = "127.0.0.1" 
port = 2222        # The "Special Door" that leads to the SIEM.
user = "REDACTED_USER"      # REPLACE THIS with your Ubuntu username.
password = "REDACTED_PASSWORD"  # REPLACE THIS with your Ubuntu password.
# -------------------------------------------

# --- 2. CONNECT ---
try:
    # This creates a "Client" object to start the connection.
    ssh = paramiko.SSHClient()
    # This line tells Python to trust the "Fingerprint" of your VM.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    print(f"Connecting to {host}:{port}...")
    ssh.connect(host, port=port, username=user, password=password)

    # --- 3. TRANSFER THE RULE ---
    # SFTP is "Secure File Transfer Protocol." It's like a digital moving van.
    sftp = ssh.open_sftp()
    
    # We move the rule from WSL to the "tmp" folder on the SIEM first.
    sftp.put("../../sigma-rules/win_encoded_ps.yml", "/tmp/win_encoded_ps.yml")
    sftp.close()
    print("File transferred to /tmp/ successfully.")

    # --- 4. DEPLOY AND RESTART ---
    # Now we tell the SIEM to move the file into the official Rules folder.
    # 'sudo' is used because that folder is protected.
    ssh.exec_command("sudo mv /tmp/win_encoded_ps.yml /var/ossec/etc/rules/")
    
    # This is the most important command. Wazuh must restart to read the new rule.
    ssh.exec_command("sudo systemctl restart wazuh-manager")
    print("Wazuh Manager restarted. Rule is now LIVE.")

    ssh.close()

except Exception as e:
    print(f"An error occurred: {e}")