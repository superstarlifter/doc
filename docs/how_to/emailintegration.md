## Email Integration

[**Video Tutorial**](https://youtu.be/ZB8QuqRyBHs?feature=shared)

Uploading data into StarLifter is as easy as emailing a spreadsheet. Ask StarLifter to set you up with an email address for your StarLifter org.

Once an email is created, set up [**File Match Rules**](https://docs.starlifter.io/#/how_to/filematchrules) and a [**Scheduled Job**](https://docs.starlifter.io/#/how_to/scheduledintegrations) to clean and upload the data to the right collection at the right frequency.

### Upload data using Email
1. In this example, we will upload General Ledger data for July.

<img src="../assets/emailintegration_matt00.png"  style="width:400px" class="border"></img>

2. Set up File Match Rules and Scheduled job. File Match Rules tell StarLifter where and how to upload the data. Scheduled jobs determine the frequency with which data is uploaded.

<img src="../assets/emailintegration_matt01.png"  style="width:400px" class="border"></img>

3. Send an email to the address for your StarLifter organization containing the attached data in an Excel or .csv file.

<img src="../assets/emailintegration_matt02.png"  style="width:300px" class="border"></img>

4. The next time your scheduled job for your Email Integration runs, your data will be uploaded into StarLifter as determined by the File Match Rules. You can run the scheduled job manually by clicking **Try it**.

<img src="../assets/emailintegration_matt03.png"  style="width:800px" class="border"></img>

5. July data is now uploaded to the collection.

<img src="../assets/emailintegration_matt04.png"  style="width:800px" class="border"></img>

**A few tips:**
* Before data can be emailed into StarLifter, a base collection must exist that contains the fields you wish to upload. Best practice is to begin by uploading a base collection into StarLifter manually.
* Many systems allow for automated email data reporting. Consider setting this up for a hands-free experience!
