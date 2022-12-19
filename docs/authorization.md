# Documentation

## Explanation for Authorization using JWT token based Authentication and Authorization

There are two types of users of the system
   1. **System Users**: Users who are admin and have access to the whole system.
   2. **Customers**: Customers who are using the system to access their insurance policies.

System Users -
   1. Admin
   2. Support
   3. Finance
   4. Tech team

Customers -
   1. Users who want to buy policies for themselves.

The choice of authentication for the system is JWT Token based authentication and authorization. It's widely
used as an industry standard for Auth. The idea behind using these token is very simple.

1. The token is generated per user for a fixed amount of time.
2. Additional information can be added in the token which can be decrypted in the routes to determine the
roles and actions. This is very helpful with regards to providing certain users with total priviledge vs
restricted access.
3. The token expires after a certain duration and a new token can be generated for a user by sending the
refresh token to the correct endpoint.

### Groups,Roles and Permissions
Django has excellent built in support for groups. Users can be added in specific groups and each of these
groups have their own set of permissions. Custom permissions can also be created in the model class.

The group information can be added in the Token which can help to determine the level of access given to
the user.

