# CSV-PARSER

The application is meant to analyse data from csv file that is uploaded to give meaningful information on various business activities.


<h2>Upload a csv file</h2>
<p>Enables a user to upload the sample csv file.
_Router_ used 'api/v1/upload' POST METHOD.</p>

<h2>Monthly total amount endpoint</h2>
<p> Returns a summary of total amount incurred for each month
_Router used_'api/v1/monthly-total' GET METHOD.</p>

<h2>Get top five customers endpoint</h2>
<p>Returns he Top Five customers according Total amount (quantity * 
unitAmount) due for a given year </p>
_Router used_'api/v1/top-customers-amount' GET METHOD</p>

<h2>GET top five customers according to quantity bought</h2>
<p>Returns the Top Five customers, according to Quantity bought. 
_Router used_'api/v1/top-customers-quantity' GET METHOD>
  
<h2>GET Invoice transaction </h2>
<p>Returns total invoice transaction per day for all transactions that took place 
30days from a given date. 

_Router used_'api/v1/invoice' GET METHOD</p>


<div><h2>Installation</h2>
  <ol>
     <li>Open a repo in github</li>
     <li>Clone the repository into the local machine through the terminal by: git clone https://github.com/winniekariuki/Mystore-manager.git</li>
     <li>Create a virtual enviroment with the command $ virtualenv -p python3 env</li>
     <li>Activate the virtual enviroment with the command `Desktop/MysCSV-parser/env/Scripts/activate`</li>
    <li>cd back into the Challeng3 where you include all your code related files.</li>
    <li>Install requirements $ pip install -r requirements.txt</li>
  </ol>
</div>
<div><h2>How to test</h2>
  <p>The endpoints can be tested through the postman by sending the link gotten from the terminal after running the app with the their respective routers</p>
</div>
<div>
  https://csv-parse.herokuapp.com/</div>
  
