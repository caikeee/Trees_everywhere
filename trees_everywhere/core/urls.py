from django.urls import path
from .views import home_view, login_view, tree_detail_view, user_trees_view, add_tree_view, account_trees_view, user_trees_api


urlpatterns = [
    path('', home_view, name='home'), 
    path('login/', login_view, name='login'),
    path('user/trees/', user_trees_view, name='user_trees'),
    path('tree/add/', add_tree_view, name='add_tree'),
    path('account/trees/', account_trees_view, name='account_trees'),
    path('tree/<int:pk>/', tree_detail_view, name='tree_detail'), # Nova URL para detalhes
    path('api/user/trees/', user_trees_api, name='user_trees_api'),
]
