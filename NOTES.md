# This file contains some notes i write for myself.


- ## Commands
- `django-admin` - provides the list of commands
- `django-admin startproject <name>` - starts a new project.
- `python manage.py runserver` - starts the server.
- `python manage.py makemigrations` - creates preperations for migrations.
- `python manage.py migrate` - migrates the changes.
- `python manage.py startapp <name>` - starts a new app (component for the project)
- `python manage.py shell` - to get an interactive shell.
- `python manage.py loaddata` - this is used to load data, for example for seeding data, it will look for `json`/`xml`/`yml` files inside of `fixtures` folders, inside of apps folders.

# General Django 
- ## General Info
    - `djangorestframework` - To use django as a RESTApi.
    - `django-cors-headers` - Solves CORS issues.
- ## Apps
    - New apps / plugins (for example `DRF`) should be registered to `settings.py` inside `INSTALLED_APPS`
    - New `views` are added to `views.py` of the app, example:
        ```
        from rest_framework.views import APIView
        from rest_framework.response import Response

        class ReportingViewSet(APIView):
            def get(self, request):
                answer = {'id': "42", 'name': "question"}
                return Response(answer)
        ```
    - You need to register the url pattern for each view.  
    **[NOTE - Its better a `router`]**
        - create `urls.py` inside the `app` folder. 
        - add something like this:
            ```
            from reporting.views import ReportingViewSet
            from django.urls import path

            urlpatterns = [
                path('reporting/',ReportingViewSet.as_view(),name='reporting')
            ]
            ``` 
    - You need to add it to the global `urls.py` file which is inside the `project` folder, using `include`

        ```
        from django.contrib import admin
        from django.urls import include,path

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('api/',include('reporting.urls'))
        ]
        ```
- ## Serialization / Models

- You create a model by adding it to the `models.py` inside the app folder.  
    `models.py`:
    ```
    from django.db import models

    class Order(models.Model):
        
        amount = models.CharField(max_length=50)
        description = models.CharField(max_length=100)
        created_time = models.DateTimeField()
    ```
- You serialize it by creating `serializers.py` file inside the app folder.  
    `serializers.py`:
    ```
    from rest_framework import serializers
    from reporting.models import Order

    class OrderSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = ['id','amount','description','created_time']
    ```
- ### Views
    - When using `viewsets.ModelViewSet` we are getting a bunch of functionality:
        ```
        A viewset that provides default `create()`, `retrieve()`, `update()`,
        `partial_update()`, `destroy()` and `list()` actions.
        ```
    - Example (`reporting/views.py`):
        ```
        class OrderViewSet(viewsets.ModelViewSet):

            serializer_class = OrderSerializer
            
            def get_queryset(self):
                return Order.objects.all().order_by('-created_time')

        ```

- ### Router
    - Example of adding router (`urls.py`):
    ```
    from reporting.views import OrderViewSet, ReportingViewSet
    from django.urls import include, path
    from rest_framework.routers import DefaultRouter


    router = DefaultRouter()
    router.register('orders',OrderViewSet, basename='orders')


    urlpatterns = [
        path('reporting/',ReportingViewSet.as_view(),name='reporting'),
        path('', include(router.urls))
    ]
    ```
- ## Settings
    - Allows hosts - `ALLOWED_HOSTS = ["*"]`
    - Allows All Cors - `CORS_ORIGIN_ALLOW_ALL = True`
# General VUE
- Instead of installing VUE using CLI (if you don't want to run `npm install -g @vue/cli`) you can use `NPX` to directly run the commands : `npx -p @vue/cli vue create <name>`
- `npm run serve` to start the server.
- `npm install axios` - to install `axios`


- ## Hooks (Composition API)
- `setup(){}` - When using composition API, view it as an entrypoint for the component.
- `onMounted()` hook in Vue's Composition API is a lifecycle hook that gets called after the component is fully mounted (i.e., added to the DOM). It is equivalent to the mounted lifecycle method in the Options API.

- ## Functions
- `ref()` is a reactive reference used to manage state within the Composition API. It allows you to create reactive variables that Vue can automatically track for changes. When the value inside a ref changes, Vue will automatically update any parts of the DOM or other computations that depend on that value.

- ## SASS / SCSS
- This is how you add scss to the project (create `/styles/main.scss`):  
    `vue.config.js`
    ```
      css: {
        loaderOptions: {
            sass: {
                additionalData: `@import "~@/styles/main.scss";`,
                }
            }
        },

    ```