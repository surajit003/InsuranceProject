# Endpoint Guidelines

1. Customer:
   1. **/api/v1/create_customer - POST{"first_name": "test", "last_name": "user", "dob": "21-03-1990"}**: Create a customer.
   2. **/api/v1/customers/**: GET all customers.
   3. **/api/v1/customers/{customer_id}/**: GET a single customer.
   4. **/api/v1/customers?first_name="xyz"**: Search customers by first_name.
   5. **/api/v1/customers/?last_name="abc"**: Search customers by last_name.
   6. **/api/v1/customers/?dob="21-03-1990"**: Search customers by dob.


2. Policy:
   1. **/api/v1/quote - POST{"type": "health", "customer_id": 2}**: Create a Quote.
   2. **/api/v1/quotes/{quote_id}/**: Get quote by quote_id.
   3. **/api/v1/quotes}/**: GET all quotes.
   4. **/api/v1/quotes?customer_id="2"**: Search quotes by customer_id.
   5. **/api/v1/quotes/?type="abc"**: Search customers by quote type.
   6. **/api/v1/quotes/{quote_id}/ - PATCH{"state:"accepted"}**: Update a quote as accepted for a quote_id.


## Open endpoints
By default, all endpoints are kept open which is a bad idea. However, the initial set up for JWT Token Auth
is added in the project which can be easily plugged into the routes.

### Policy State transition management
In the current implementation, the state management is very if..else heavy which is not the right approach.
A better approach would be to use the django_fsm library. However, the current implementation is very strict
with the state transition .
 1. NEW -> ACCEPTED -> ACTIVE

* A policy already in active state cannot be changed back to accepted/new state
* A policy in new state cannot directly be changed to active without first changing to accepted
* A policy marked as accepted automatically transitions to active with a simulated payment made for the policy.

