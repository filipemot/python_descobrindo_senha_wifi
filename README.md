No windows para visualizar as informações de uma rede é o comando `netsh wlan show profiles`.

O resultado para deste comando é uma listagem das redes gravadas no seu computador:

```python
Perfis da política de grupo (somente leitura)
---------------------------------
    <Nenhum>

Perfis do usuário
-------------
Todos os Perfis de Usuários: Rede 1
Todos os Perfis de Usuários: Rede 2
Todos os Perfis de Usuários: Rede 3
```

Para as informações mais detalhadas, é através do comando `netsh wlan show profile "Rede 1" key = clear`

O resultado deste comando é todas as informações de rede. A senha é apresentado no campo Conteúdo da Chave.

```python
Perfil Rede 1 na interface Wi-Fi:
=======================================================================

Aplicado: Todos os Perfis de Usuários

Informações do perfil
-------------------
    Versão                : 1
    Tipo                   : LAN sem Fio
    Nome                   : Rede 1
    Opções de controle        :
        Modo de conexão    : Conectar automaticamente
        Alternância automática : Não alternar para outra rede
        Uso de MAC Aleatório: Desabilitado

Configurações de conectividade
---------------------
    Número de SSIDs        : 1
    Nome SSID              : "Rede 1"
    Tipo de rede           : Infraestrutura
    Tipo de Rádio               : [ Qualquer Tipo de Rádio ]
    Extensão do fornecedor       : Não presente

Configurações de segurança
-----------------
    Autenticação         : WPA2-Personal
    Codificação         : CCMP
    Autenticação         : WPA2-Personal
    Codificação         : GCMP
    Chave de segurança           : Presente
    Conteúdo da Chave            : 123456

Configurações de custo
-------------
    Custo                   : Irrestrito
    Congestionado              : Não
    Limite de Dados Aproximado: Não
    Limite de Dados Excedido        : Não
    Roaming                : Não
    Origem de Custo            : Padrão
```

**Execução**

`py main.py`

**Resultados do Script**

['Rede 1 - 123456','Rede 2 - 12345678']

**Execução Testes**

Entrar na pasta `tests` e executar o script `pytest TestMain.py`

**Script**

- get_networks: Lista todas as redes configuradas, com as senhas
- information_network: Buscas as informações detalhadas e retorna a senha armazenada

```python
import subprocess

def get_networks():
    information_command = subprocess.check_output("netsh wlan show profiles", encoding="cp858", shell=True)
    networks = []
    for line in information_command.split('\n'):
        if "Todos os Perfis de Usuários" in line:
            position = line.find(":")
            network = line[position + 2:]
            password = information_network(network)
            networks.append(network + " - " + password)
    return networks

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
    print(get_networks())
```
