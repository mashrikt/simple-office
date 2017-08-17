# Django web developer test:

============

You are requested to create a super simple app which have multiple organizations.Each organization can have multiple user who can add  multiple iframe links to their organization and view them.

• super admin will be able to create organization and user(email/password) under that organization

• created user will be able to login with that credentials and add iframe links for his organization and view (as an Iframe) his organization’s past created links

• user will also be able to delete any particular entry


Please make sure you meet the following criteria

    1. Your authentication should implement JWT as authenticator. Here’s the link what you need to learn to implement this

        a. https://jwt.io/introduction/

        b. https://github.com/GetBlimp/django-rest-framework-jwt


    2. Your HTML should not bind with a view. It means when you are visiting a url `/create`. The Django view would return/render only the HTML. All the form interaction and other data fetching things will be done through Django Rest Framework

        a. http://www.django-rest-framework.org/


    3. Django Rest framework comes with a beautiful in built documentation generator. You are encouraged to use that (optional)

    4. Make use of Django admin for super admin related tasks.


•