import paramiko

# --- CONFIGURATION (REDACTED FOR GITHUB) ---
host = "REDACTED" 
port = REDACTED        
user = "REDACTED_USER"      
password = "REDACTED_PASSWORD"  
# -------------------------------------------

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    print(f"Connecting to {host}:{port}...")
    ssh.connect(host, port=port, username=user, password=password)

    # Transfer the Sigma Rule via SFTP
    sftp = ssh.open_sftp()
    sftp.put("../../sigma-rules/win_encoded_ps.yml", "/tmp/win_encoded_ps.yml")
    sftp.close()
    print("File transferred to /tmp/ successfully.")

    # Deploy to Wazuh Rules directory and Restart Manager
    ssh.exec_command("sudo mv /tmp/win_encoded_ps.yml /var/ossec/etc/rules/")
    ssh.exec_command("sudo systemctl restart wazuh-manager")
    print("Wazuh Manager restarted. Rule is now LIVE.")

    ssh.close()

except Exception as e:
    print(f"An error occurred: {e}")
