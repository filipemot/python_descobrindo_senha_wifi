import unittest
from unittest.mock import patch

import main


class TestMain(unittest.TestCase):

    @patch("subprocess.check_output")
    @patch("main.information_network")
    def test_get_networks_with_profile_with_password(self, spy_information_network, spy_check_output):
        spy_check_output.return_value = "Todos os Perfis de Usuários: Rede 1\n"
        spy_information_network.return_value = "123456"
        self.assertEqual(main.get_networks(), ["Rede 1 - 123456"])

    @patch("subprocess.check_output")
    @patch("main.information_network")
    def test_get_networks_without_profile_with_password(self, spy_information_network, spy_check_output):
        spy_check_output.return_value = "Todoss: Rede 1\n"
        spy_information_network.return_value = "123456"
        self.assertEqual(main.get_networks(), [])

    @patch("subprocess.check_output")
    @patch("main.information_network")
    def test_get_networks_without_profile_without_password(self, spy_information_network, spy_check_output):
        spy_check_output.return_value = "Todos: Rede 1\n"
        spy_information_network.return_value = ""
        self.assertEqual(main.get_networks(), [])

    @patch("subprocess.check_output")
    def test_information_network_get_network_with_password(self, spy_check_output):
        spy_check_output.return_value = "Conteúdo da Chave: 123456\n"
        self.assertEqual(main.information_network("Rede 1"), "123456")

    @patch("subprocess.check_output")
    def test_information_network_get_network_without_password(self, spy_check_output):
        spy_check_output.return_value = "Credencial de autenticação 802.1X : Credencial da máquina ou do usuário\n"
        self.assertEqual(main.information_network("Rede 2"), "")
