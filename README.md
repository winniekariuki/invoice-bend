# Mystore-manager
[![Build Status](https://travis-ci.org/winniekariuki/Mystore-manager.svg?branch=develop)](https://travis-ci.org/winniekariuki/Mystore-manager)
[![Coverage Status](https://coveralls.io/repos/github/winniekariuki/Mystore-manager/badge.svg?branch=develop)](https://coveralls.io/github/winniekariuki/Mystore-manager?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/5f82c585bee66cdc4bbd/maintainability)](https://codeclimate.com/github/winniekariuki/Mystore-manager/maintainability)

Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.


<h2>Sign up endpoint</h2>
<p>Enables admin to sign up store attendant's users.
_Router_ used 'api/v2/auth/signup' POST METHOD.</p>

<h2>Login endpoint</h2>
<p>Enables a registered user to login into the application after which an 
access token is assigned to him/her to enable him/her to access 
authenticated endpoints.
_Router used_'api/v2/auth/login' POST METHOD.</p>
<h2>Post Product endpoint</h2>
<p>Enables the store admin to create a new product and post.
Only the store admin can access this endpoint.
_Router used_'api/v2/products' POST METHOD.</p>
<h2>GET product endpoint</h2>
<p>No access token required.The endpoint enables a user to
view all the available products in the inventory.
_Router used_'api/v2/products' GET METHOD.</p>
<h2>GET Single product</h2>
<p>No access token required.Enables a user to get a single
product from the inventory.
_Router used_'api/v2/products/1' GET METHOD</p>
<h2>POST sale endpoint</h2>
<p>Only the store attendant is allowed to access this endpoint.
Enables the store attendant to post a sale.
_Router used_'api/v2/sales' POST METHOD</p>
<h2>Get all sales endpoint</h2>
<p>The endpoint allows the admin to get all the sale records posted
by the store attendants.Only accessible by the admin.
_Router used_'api/v2/sales' GET METHOD.</p>
<h2>Get single sale record endpoint</h2>
<P>The endpoint is only accessible to the store attendant who created it and the store admin.
Enables the two to get the sale record.
_Router used-'api/v2/sales/1' GET METHOD.</p>

<div><h2>Installation</h2>
  <ol>
     <li>Open a repo in github</li>
     <li>Clone the repository into the local machine through the terminal by: git clone https://github.com/winniekariuki/Mystore-manager.git</li>
     <li>Create a virtual enviroment with the command $ virtualenv -p python3 env</li>
     <li>Activate the virtual enviroment with the command `Desktop/Mystore-manager/env/Scripts/activate`</li>
    <li>cd back into the Challeng3 where you include all your code related files.</li>
    <li>Install requirements $ pip install -r requirements.txt</li>
  </ol>
</div>
<div><h2>How to test</h2>
  <p>The endpoints can be tested through the postman by sending the link gotten from the terminal after running the app with the their respective routers</p>
  <p>To test if the tests pass you run the pytest command </p>
</div>
<div>
  https://mystoremanagerapp.herokuapp.com/</div>
  <div>
  https://www.pivotaltracker.com/n/projects/2202841
 </div>
