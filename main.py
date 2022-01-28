import subprocess


def get_networks():
    information_command = subprocess.check_output("netsh wlan show profiles", encoding="cp858", shell=True)
    for line in information_command.split('\n'):
        if "Todos os Perfis de Usuários" in line:
            position = line.find(":")
            network = line[position + 2:]
            password = information_network(network)
            print(network + " - " + password)


def information_network(wifi):
    information_command = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key", "=", "clear"],
                                                  encoding="cp858", shell=True)
    network = ''
    for line in information_command.split('\n'):
        if "Conteúdo da Chave" in line:
            position = line.find(":")
            network = line[position + 2:]
            break
    return network


if __name__ == "__main__":
    get_networks()
