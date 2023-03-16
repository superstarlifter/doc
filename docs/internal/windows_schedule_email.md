## Send a scheduled email from Windows via Powershell
You can use PowerShell to send and email with an attachment to a designated StarLifter email address.

### Create the Poweshell script

Open the Powershell environment by searching for Powershell in the Windows search and selecting Windows Powershell ISE.



<img src="../assets/powershell_send_email_1.png"  style="width:600px" class="border"></img>

Select File --> New from the taskbar menu to create a new Powershell document.

<img src="../assets/powershell_send_email_12.png"  style="width:600px" class="border"></img>

Copy/Paste the example Powershell script from section below [Example](#example-powershell-command) and change the values in the brackets.

<img src="../assets/powershell_send_email_11.png"  style="width:600px" class="border"></img>

<img src="../assets/powershell_send_email_13.png"  style="width:600px" class="border"></img>

Select File --> Save As from the taskbar menu and name your new Powershell document.


<img src="../assets/powershell_send_email_2.png"  style="width:600px" class="border"></img>



### Create a Windows scheduled task to run the Powershell command

Add a name and description for the scheduled task.

Click Next.

<img src="../assets/powershell_send_email_3.png"  style="width:600px" class="border"></img>

Choose the frequency to run the task.

Click Next.

<img src="../assets/powershell_send_email_4.png"  style="width:600px" class="border"></img>

Set the date, time, and reccurance of the task.

Click Next.

<img src="../assets/powershell_send_email_5.png"  style="width:600px" class="border"></img>

Choose Start a program.

Click Next.

<img src="../assets/powershell_send_email_6.png"  style="width:600px" class="border"></img>

Enter the path of the Powershell application in the Program/Script box. Default - C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

Enter the path of your newly created Powershell script in the Add Arguments box.

Click Next.

<img src="../assets/powershell_send_email_7.png"  style="width:600px" class="border"></img>

Select the checkbox, “Open the Properties dialog for this task when I click Finish”.

Click Finish.

<img src="../assets/powershell_send_email_8.png"  style="width:600px" class="border"></img>

In the properties dialog, under the General tab, check the “Run when user is logged on or not” and “Run with highest privileges” checkboxes are selected.

#Read more: https://www.sharepointdiary.com/2013/03/create-scheduled-task-for-powershell-script.html#ixzz7w9TiO6a1

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
