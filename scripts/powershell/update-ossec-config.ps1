update-ossec-config.ps1

<#
Name: update-ossec-config.ps1
Description: Updates ossec.conf by adding a localfile entry for Sysmon logs using XML parsing.
Use Case: Automates configuration changes and bypasses manual permission issues.
#>

# Converting the config to an XML object to bypass permission errors
$xml = [xml](Get-Content "C:\Program Files (x86)\ossec-agent\ossec.conf")
# Appending the Sysmon channel
$newLocalFile = $xml.CreateElement("localfile")
# ... (Adding location and log_format tags)
$xml.Save("C:\Program Files (x86)\ossec-agent\ossec.conf")
