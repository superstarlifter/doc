## Send a scheduled email from Windows via Powershell
You can use PowerShell to send and email with an attachment to a designated StarLifter email address.

### Create the Poweshell script

Open the Powershell environment by searching for Powershell in the Windows search and selecting Windows Powershell ISE.

Select File --> New from the taskbar menu to create a new Powershell doucument

<img src="../assets/powershell_send_email_1.png"  style="width:600px" class="border"></img>

Select File --> New from the taskbar menu to create a new Powershell doucument

<img src="../assets/powershell_send_email_11.png"  style="width:600px" class="border"></img>

Copy/Paste the example Powershell script from section below [Example](#example-powershell-command) and change the values in the brackets.

<img src="../assets/powershell_send_email_2.png"  style="width:600px" class="border"></img>



### Create a Windows scheduled task to run the Powershell command



<img src="../assets/powershell_send_email_3.png"  style="width:600px" class="border"></img>

<img src="../assets/powershell_send_email_4.png"  style="width:600px" class="border"></img>

<img src="../assets/powershell_send_email_5.png"  style="width:600px" class="border"></img>

<img src="../assets/powershell_send_email_6.png"  style="width:600px" class="border"></img>

<img src="../assets/powershell_send_email_7.png"  style="width:600px" class="border"></img>

<img src="../assets/powershell_send_email_8.png"  style="width:600px" class="border"></img>

<img src="../assets/powershell_send_email_9.png"  style="width:600px" class="border"></img>

<img src="../assets/powershell_send_email_10.png"  style="width:600px" class="border"></img>

### Example PowerShell command 
The following example uses a Gmail email address to send the email.
*Items in brackets [] need to be replaced.*

```
Send-MailMessage -From "[SEND EMAIL]" `
                 -To "[RECEPIENT EMAIL]" `
                 -Subject "[SUBJECT]" `
                 -Body "[BODY]" `
                 -Attachment "[PATH OF ATTACHEMENT]" `
                 -SmtpServer [SMTP SERVER] `
                 -Port 587 `
                 -UseSsl `
                 -Credential (New-Object `
                   -TypeName System.Management.Automation.PSCredential `
                   -ArgumentList "[EMAIL USERNAME]", `
                   (ConvertTo-SecureString `
                     -String "[EMAIL PASSWORD]" `
                     -AsPlainText -Force))

```
