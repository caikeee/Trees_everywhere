from django.urls import path
from .views import (
    account_list_view,
    home_view, 
    login_view, 
    tree_detail_view, 
    user_trees_view, 
    add_tree_view, 
    account_trees_view, 
    user_trees_api
)

# Define the URL patterns for the application
urlpatterns = [
    # URL for user login
    path('login/', login_view, name='login'),

    # URL for the home page
    path('', home_view, name='home'), 

    # URL for viewing trees planted by the logged-in user
    path('user/trees/', user_trees_view, name='user_trees'),

    # URL for adding a new tree
    path('tree/add/', add_tree_view, name='add_tree'),

    # URL for viewing trees planted in accounts the user is part of
    path('account/trees/', account_trees_view, name='account_trees'),

    # URL for viewing trees planted in accounts the user is part of
    path('account/list/', account_list_view, name='account_list'),

    
    


    # URL for viewing details of a specific tree
    path('tree/<int:pk>/', tree_detail_view, name='tree_detail'),  # Accepts a tree ID as a parameter

    # API endpoint for retrieving trees planted by the logged-in user
    path('api/user/trees/', user_trees_api, name='user_trees_api'),
]
