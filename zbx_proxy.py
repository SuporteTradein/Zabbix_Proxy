#!/usr/bin/env python
#
#        zbx_tdn.py - Instalador de pacotes zabbix
# --------------------------------------
# __versao__ = "3.0"
# __author__ = "Matheus Oliveira Viana"
# __email __ = "matheus.viana@tradein.com.br"
# --------------------------------------
#	DESCRICAO:
#		Este programa tem como funcao auxiliar a
#		instalacao, configuracao e manutencao dos
#		pacotes zabbix da TradeIN.
# --------------------------------------
#	NOTAS:
# --------------------------------------
#	MODIFICADO POR(DD/MM/YYYY)
#	Matheus.Viana 	14/03/2019 - Primeira versao
#   Matheus.Viana	11/03/2021 - Adicionado Suporte a RHEL 8 e Debian 10, removido suporte a Debian 7
#	Matheus.Viana	11/08/2021 - Padronizado suporte somente a Debian 10, removida funcao repositorio.
#
# ----------- BUGS ENCONTRADOS ---------
#   
# ----------- IMPORTS ------------
import os
import subprocess
import socket
# ----- CABECALHO DO PROGRAMA -----
cabecalho = '\n[+] - Bem-vindo ao instalador zabbix_tdn - [+]\n[+] - Desenvolvido por Matheus Viana - [+]\n[+] - Para informar bugs mande o print para matheus.viana@tradein.com.br - [+]\n'
# ---------- LIMPAR TELA ----------
def clearner():
	os.system("clear")
	print(cabecalho)

clearner()
# --------- VAREAVEIS GLOBAIS ------------
pwd = subprocess.getoutput('pwd')
# ----------- FUNCOES DO PROGRAMA ------------
def download():
	print('\n Preparando ambiente para instalacao...\n')
	os.system("cp /etc/apt/sources.list /etc/apt/sources.list.old")
	os.system('echo "deb http://deb.debian.org/debian buster main contrib non-free" > /etc/apt/sources.list')
	os.system('echo "deb-src http://deb.debian.org/debian buster main contrib non-free" >> /etc/apt/sources.list')
	print('Baixando pacotes...')
	os.system('wget -q https://repo.zabbix.com/zabbix/5.0/debian/pool/main/z/zabbix-release/zabbix-release_5.0-1+buster_all.deb 1>/dev/null')
	print('Instalando pacotes...')
	os.system('dpkg -i {}/zabbix-release_5.0-1+buster_all.deb 1>/dev/null'.format(pwd))
	print('Atualizando pacotes...')
	os.system('apt update 1>/dev/null')
	print('Download de pacotes completo.')

def configure():
	conf_file = os.path.isfile('/etc/zabbix/zabbix_proxy.conf')

	if conf_file == 'True':
		os.system('mv /etc/zabbix/zabbix_proxy.conf /etc/zabbix/zabbix_proxy.conf-bkp')
		passdb = subprocess.getoutput('cat /etc/zabbix/zabbix_proxy.conf-bkp | grep -v "#" | grep "DBPassword=" | cut -d "=" -f 2')
		userdb = subprocess.getoutput('cat /etc/zabbix/zabbix_proxy.conf-bkp | grep -v "#" | grep "DBUser=" | cut -d "=" -f 2')
		namedb = subprocess.getoutput('cat /etc/zabbix/zabbix_proxy.conf-bkp | grep -v "#" | grep "DBName=" | cut -d "=" -f 2')
	else:
		passdb = '_zabbix@sql'
		userdb = 'zabbix'
		namedb = 'zabbix'

	hostname = socket.gethostname()
	conf = open("/etc/zabbix/zabbix_proxy.conf","w +")
	conf.write("CacheSize=1G\nDBName={}\nDBPassword={}\nDBUser={}\nDebugLevel=3\nEnableRemoteCommands=1\nExternalScripts=/usr/lib/zabbix/externalscripts\nFping6Location=/usr/sbin/fping6\nFpingLocation=/usr/sbin/fping\nHistoryCacheSize=128M\nHistoryIndexCacheSize=32M\nHostname={}\nLogFileSize=1024\nLogFile=/var/log/zabbix/zabbix_proxy.log\nLogSlowQueries=3000\nPidFile=/var/run/zabbix/zabbix_proxy.pid\nServer=monitoramento.tradein.com.br\nSNMPTrapperFile=/var/log/snmptrap/snmptrap.log\nSocketDir=/var/run/zabbix\nStartDBSyncers=8\nStartPollers=10\nStartPollersUnreachable=5\nTimeout=30\nUnreachablePeriod=60\n".format(namedb, passdb, userdb, hostname))
	conf.close()

def configure_agent():
	conf_file = os.path.isfile('/etc/zabbix/zabbix_agentd.conf')
	hostname = socket.gethostname()
	ipa = input('Qual o ip do proxy?: ')
	
	if conf_file == 'True':
		os.system('mv /etc/zabbix/zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf-bkp')
	
	conf = open("/etc/zabbix/zabbix_agentd.conf","w +")
	conf.write("PidFile=/var/run/zabbix/zabbix_agentd.pid\nLogFile=/var/log/zabbix/zabbix_agentd.log\nLogFileSize=0\nEnableRemoteCommands=1\nServer={}\nHostname={}\nTimeout=30\nAllowRoot=1\nInclude=/etc/zabbix/zabbix_agentd.d/*.conf\nUserParameter=zbx_upd[*],/etc/zabbix/scripts/zbx_agnt_lnx.sh update debian 10".format(ipa, hostname))
	conf.close()

def install():
	clearner()
	download()
	comando_sql = "grant all privileges on zabbix.* to zabbix@localhost identified by '_zabbix@sql';"
	print('Pre-instalando mais alguns pacotes necessarios...')
	os.system('apt install -y vim mlocate snmp-mibs-downloader snmp htop 1>/dev/null')
	print('Instalando sistema...')
	os.system('apt install -y mariadb-server zabbix-proxy-mysql zabbix-get 1>/dev/null')
	os.system('service mariadb start')
	print('Criando banco de dados...')
	os.system('mysql -uroot -p -e"create database zabbix character set utf8 collate utf8_bin;"')
	os.system('mysql -uroot -p -e"{}"'.format(comando_sql))
	os.system('zcat /usr/share/doc/zabbix-proxy-mysql*/schema.sql.gz | mysql -Dzabbix -uzabbix -p_zabbix@sql')
	configure()
	configure_agent()
	os.system('update-rc.d zabbix-proxy enable')
	clearner()

def update():
	download()
	os.system("apt-get upgrade -y")

# ----- CONTROLADOR DE FLUXO SECUNDARIO -----
def menu():
	acao = input('--- Escolha uma opcao do menu ---\n\n[1] - Instalar\t\tExecuta a instalacao do proxy e agente Zabbix.\n[2] - Update\t\tExecuta o upgrade dos pacotes Zabbix.\n[3] - Download\t\tFaz o download dos repositorios Zabbix, mas nao executa a instalacao do sistema.\n\n[0] - Exit\t\tSai do programa.\n\n[+] - Selecione uma opcao[0-7]: \n\n')
	if acao == '1':
		install()
	elif acao == '2':
		update()
	elif acao == '3':
		download()
	elif acao == '0':
		exit()
	else:
		print('Voce informou a opcao {} e ela nao e valida!!!\n'.format(acao))
		menu()
	

menu()
