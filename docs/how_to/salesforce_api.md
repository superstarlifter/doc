## Integrate with Salesforce
[**Video Tutorial**](https://youtu.be/RA0sLW_FuU8?feature=shared)

Creating StarLifter collections from your Salesforce data only takes a few minutes.

Before you begin, contact your Salesforce Administrator for the following information:
* Instance URL
* User login
* User password
* [**Security Token**](https://help.salesforce.com/s/articleView?id=sf.user_security_token.htm&type=5)

**Note:** The user login must be a Salesforce API license with ModifyAllData or ModifyMetadata permissions.

### Set up API Integration
1. From the menu at the upper left of the screen, select **Toggle menu**.

<img src="../assets/salesforce_api0.png"  style="width:400px" class="border"></img>

2. Select **Salesforce Integration** under the Additional Links dropdown.

<img src="../assets/salesforce_api1.png"  style="width:300px" class="border"></img>

3. Enter the information provided by your Salesforce Administrator.

<img src="../assets/salesforce_api3.png"  style="width:800px" class="border"></img>


### Upload data
1. Select the Objects and Fields you wish to upload.

<img src="../assets/salesforce_api4.png"  style="width:800px" class="border"></img>
   
2. Check **Preview only** and select **Go** to preview the collection.

<img src="../assets/salesforce_api5.png"  style="width:800px" class="border"></img>

3. When you are ready to upload the collection, uncheck **Preview**. You have several options available to you when you upload a collection:
   * **Drop current collection first:** If a StarLifter collection already exists, drop the current collection and replace it with the new collection. Alternatively, StarLifter will update the current collection.
   * **Copy all rows:** Download all records in a Salesforce object, rather than specifying the number of records to pull.
   * **Set references:** Automatically set StarLifter references for Salesforce reference fields.

<img src="../assets/salesforce_api6.png"  style="width:800px" class="border"></img>
  
4. Push **Go** to upload the Salesforce data as a StarLifter collection. Once uploaded, the data is available as a new StarLifter collection.

<img src="../assets/salesforce_api7.png"  style="width:800px" class="border"></img>




To learn more or ask additional questions, head over to the [StarLifter Community](https://community.starlifter.io).
