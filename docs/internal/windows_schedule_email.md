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
