# ZABBIX_PROXY 
> Desenvolvido por matheus.viana@tradein.com.br.

Scripts para automatizar instalação de proxys Zabbix em novos clientes

## INSTALAÇÃO

.sh:

1. Faça o download do script de instalação.

```sh
git clone https://github.com/SuporteTradein/Zabbix_Proxy.git
```
2. Faça o download dos pacotes de instalação informando a função, distro e versão do SO.

```sh
bash Zabbix_Proxy/zbx_proxy.sh download debian 9
```
_OBS.: INFORMAR DISTRO TOTALMENTE EM MINUSCULO, ABAIXO ESTÁ A LISTA DE DISTRO E VERSÕES SUPORTADAS._

_OBS.2: PARA OS SISTEMAS CENTOS, RED-HAT E ORACLE UTILIZAR "rhel"._

3. Em caso de primeira instalação execute o comando a seguir _INFORMANDO DISTRO E VERSÃO_.

```sh
bash Zabbix_Proxy/zbx_proxy.sh install debian 9
```

4. Por fim realize a instalação do repositório offline.

```sh
bash Zabbix_Proxy/zbx_proxy.sh repositorio debian
```

## Abaixo distros e versões suportadas
| SO DISTRO | SO VERSION|
|-----------|-----------|
| Debian    | 9 - 8 - 7 |
| Ubuntu    | 18 - 16 - 14 |
| CentOS    | 7 - 6     |
| Red Hat   | 7 - 6     |
| Oracle    | 7 - 6     |

