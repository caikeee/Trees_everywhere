from django.test import TestCase
from core.models import Plant, PlantedTree, User


class PlantModelTest(TestCase):
    # O setUp é executado antes de cada teste. Aqui você está criando um objeto Plant.
    def setUp(self):
        self.plant = Plant.objects.create(name='Árvore Teste')  # Criação de uma planta com o nome "Árvore Teste"

    # Teste para verificar a criação de uma planta
    def test_plant_creation(self):
        # Verifica se o nome da planta criada é "Árvore Teste"
        self.assertEqual(self.plant.name, 'Árvore Teste')  # Testa se o nome da planta é o esperado



class PlantedTreeModelTest(TestCase):
    # O setUp é executado antes de cada teste. Aqui você cria um usuário, uma planta e uma árvore plantada.
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')  # Criação de um usuário de teste
        self.plant = Plant.objects.create(name='Árvore Teste')  # Criação de uma planta de teste
        # Criação de uma árvore plantada, associando o usuário e a planta, com coordenadas (0.0, 0.0)
        self.planted_tree = PlantedTree.objects.create(user=self.user, plant=self.plant, latitude=0.0, longitude=0.0)

    # Teste para verificar se a árvore foi criada corretamente
    def test_planted_tree_creation(self):
        # Verifica se a planta associada à árvore plantada tem o nome correto
        self.assertEqual(self.planted_tree.plant.name, 'Árvore Teste')  # Verifica o nome da planta
        # Verifica se o usuário associado à árvore plantada é o usuário correto
        self.assertEqual(self.planted_tree.user.username, 'test')  # Verifica o nome de usuário

















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
