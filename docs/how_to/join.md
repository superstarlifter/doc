## How to create a join
How-to video links:
Part 1 - https://youtu.be/i9q6_quxxq8 
Part 2 - https://youtu.be/wTQMEDzP8HA

A join is used to connect multiple collections together using a common key. StarLifter uses a Left Join when creating a Join. This type of join will return all records from the left table, and the matching records from the right table. 

<img src="../assets/Join_diagram.jpg"  style="width:200px" class="border"></img>

To create a join:  
1.	Right click ➔ **Join Definitions**

<img src="../assets/join.png"  style="width:200px" class="border"></img>

2.  Select **New Join Definition** from the drop down

<img src="../assets/join_1.png"  style="width:1000px" class="border"></img>

3.  Select the collection names to connect

<img src="../assets/join_2.png"  style="width:800px" class="border"></img>

4.  Select the key.  Note:  The name of the key does not need to match.  In the example below **Year** and **Date** are fields whose format match (e.g. MM/DD/YYYY)

<img src="../assets/join_3.png"  style="width:800px" class="border"></img>

5.  Select a **Rollup** if applicable.  

<img src="../assets/join_4.png"  style="width:200px" class="border"></img>

Rollups are necessary when the rows of data are not aligned.  A weekly rollup would be required to join these two datasets together.

<img src="../assets/join_6.png"  style="width:600px" class="border"></img>

6.  Select the fields desired in the join
7.  Add additional collections with the **+**
8.  If necessary, add a filter to one or both collections
9.  Select **OK**

<img src="../assets/join_5.png"  style="width:800px" class="border"></img>

10.  The join is added as a collection.

<img src="../assets/join_7.png"  style="width:600px" class="border"></img>

