# tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Account, Tree, PlantedTree
from django.urls import reverse

User = get_user_model()

class TreeTestCase(TestCase):
    def setUp(self):
        # Criar contas
        self.account1 = Account.objects.create(name='Account 1')
        self.account2 = Account.objects.create(name='Account 2')
        
        # Criar usuários
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.user3 = User.objects.create_user(username='user3', password='password')
        
        # Associar usuários às contas
        self.account1.user_set.add(self.user1, self.user2)
        self.account2.user_set.add(self.user2, self.user3)
        
        # Criar árvores
        self.tree1 = Tree.objects.create(name='Ipê Amarelo', scientific_name='Handroanthus albus')
        self.tree2 = Tree.objects.create(name='Jacarandá', scientific_name='Jacaranda mimosifolia')
        
        # Plantar árvores
        PlantedTree.objects.create(user=self.user1, tree=self.tree1, age=5, location_lat=-23.55, location_long=-46.63)
        PlantedTree.objects



class TreeTemplateTests(TreeTestCase):
    def test_user_tree_list_view(self):
        self.client.login(username='user1', password='password')
        response = self.client.get(reverse('user_trees'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ipê Amarelo')
        self.assertNotContains(response, 'Jacarandá')



    def test_user_tree_list_forbidden(self):
        self.client.login(username='user1', password='password')
        response = self.client.get(reverse('tree_detail', kwargs={'pk': 2}))  # Tentando acessar árvore de user2
        self.assertEqual(response.status_code, 403)
    def test_account_tree_list_view(self):
        self.client.login(username='user2', password='password')
        response = self.client.get(reverse('user_trees'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ipê Amarelo')
        self.assertContains(response, 'Jacarandá')


        
class UserPlantTreeTests(TreeTestCase):
    def test_plant_tree_method(self):
        self.client.login(username='user1', password='password')
        tree = Tree.objects.create(name='Aroeira', scientific_name='Schinus terebinthifolia')
        self.user1.plant_tree(tree, (-23.58, -46.66))
        self.assertTrue(PlantedTree.objects.filter(user=self.user1, tree=tree).exists())
        
    def test_plant_trees_method(self):
        self.client.login(username='user3', password='password')
        trees = [
            (self.tree1, (-23.59, -46.67)),
            (self.tree2, (-23.60, -46.68))
        ]
        self.user3.plant_trees(trees)
        self.assertEqual(PlantedTree.objects.filter(user=self.user3).count(), 3)  # Já há uma árvore plantada no setUp
















  # Teste para verificar se as coordenadas da árvore plantada são salvas corretamente
    def test_planted_tree_coordinates(self):
        # Verifica se a latitude da árvore plantada é 0.0
        self.assertEqual(self.planted_tree.latitude, 0.0)  # Verifica a latitude
        # Verifica se a longitude da árvore plantada é 0.0
        self.assertEqual(self.planted_tree.longitude, 0.0)  # Verifica a longitude



    

     # Teste para verificar se o usuário tem a árvore plantada corretamente
    def test_user_planted_trees(self):
        # Verifica se o usuário tem exatamente uma árvore plantada
        self.assertEqual(self.user.planted_trees.count(), 1)  # Verifica se o usuário tem 1 árvore plantada

     # Teste para verificar a remoção de uma árvore plantada
    def test_planted_tree_removal(self):
        # Deleta a árvore plantada
        self.planted_tree.delete()  # Exclui a árvore plantada
        # Verifica se o usuário não tem mais árvores plantadas após a exclusão
        self.assertEqual(self.user.planted_trees.count(), 0)  # Verifica se o número de árvores plantadas é 0 após a exclusão
