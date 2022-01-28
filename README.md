
# Descobrindo as Senhas de Wi-Fi salvas com Python

No windows para visualizar as informações de uma rede é o comando `netsh wlan show profiles`.

O resultado para deste comando é uma listagem das redes gravadas no seu computador:

    Perfis da política de grupo (somente leitura)
    ---------------------------------
        <Nenhum>
    
    Perfis do usuário
    -------------
    Todos os Perfis de Usuários: Rede 1
    Todos os Perfis de Usuários: Rede 2
    Todos os Perfis de Usuários: Rede 3

Para as informações mais detalhadas, é através do comando `netsh wlan show profile "Rede 1"  key = clear` 

O resultado deste comando é todas as informações de rede. A senha é apresentado no campo Conteúdo da Chave.

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
