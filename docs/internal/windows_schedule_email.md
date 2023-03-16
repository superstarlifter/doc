## Schedule an email from Windows
You can use PowerShell to send and email with an attachment to a designated StarLifter email address.


#### Below is an example PowerShell command that uses a Gmail account to send emails. 

*Items in brackets [] need to be replaced.*

```
Send-MailMessage -From "[FROM EMAIL]" `
                 -To "[TO EMAIL]" `
                 -Subject "[SUBJECT]" `
                 -Body "[BODY]" `
                 -Attachment "[PATH OF ATTACHMENT]" `
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


<img src="../assets/powershell_send_email_1.png"  style="width:200px" class="border"></img>
<img src="../assets/powershell_send_email_2.png"  style="width:200px" class="border"></img>
<img src="../assets/powershell_send_email_3.png"  style="width:200px" class="border"></img>
<img src="../assets/powershell_send_email_4.png"  style="width:200px" class="border"></img>
<img src="../assets/powershell_send_email_5.png"  style="width:200px" class="border"></img>
<img src="../assets/powershell_send_email_6.png"  style="width:200px" class="border"></img>
<img src="../assets/powershell_send_email_7.png"  style="width:200px" class="border"></img>
<img src="../assets/powershell_send_email_8.png"  style="width:200px" class="border"></img>
<img src="../assets/powershell_send_email_9.png"  style="width:200px" class="border"></img>
<img src="../assets/powershell_send_email_10.png"  style="width:200px" class="border"></img>
