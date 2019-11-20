#!/usr/bin/env python
#
#        zbx_tdn.py - Instalador de pacotes zabbix
# --------------------------------------
# __versao__ = "2.0"
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
#
# ----------- BUGS ENCONTRADOS ---------
#   VARIAVEIS DE COLETA DE SO NÃO ESTA FUNCIONANDO PARA RHEL - 14/08/2019
#   REESCREVER TODO O CODIGO PARA RHEL
# ----------- IMPORTS ------------
import os
import commands
import socket
# ----- CABECARIO DO PROGRAMA -----
cabecario = '\n[+] - Bem-vindo ao instalador zabbix_tdn - [+]\n[+] - Desenvolvido por Matheus Viana - [+]\n[+] - Para informar bugs mande o print para matheus.viana@tradein.com.br - [+]\n'
# ---------- LIMPAR TELA ----------
def clearner():
	os.system("clear")
	print(cabecario)

clearner()
# --------- PREINSTALANDO PACOTES ------------
print('Verificando se todos os pacotes necessarios estao instalados...')
os.system('apt install lsb-release')
print('Tudo ok.')
os.system('sleep 0.7')
# -------- VARIAVEIS DE COLETA DE SO ---------  ## ESTA PARTE NÃO ESTA FUNCIONANDO PARA SISTEMAS RHEL
system = commands.getoutput("lsb_release -a")
lista = system.split(' ')

distro = lista[5].replace('\t','').split(':')
distro = distro[2].lower()

versao = lista[7].split('.')
versao = versao[0]
pwd = commands.getoutput('pwd')
# ----------- PERGUNTAS AO USUARIO -----------
clearner()
confirma = raw_input('************MENU INICIAL ************** \n\n A distro identificada foi: {}\n A versao identificada foi: {} \n\n Confirma as informacoes? (s/N): '.format(distro, versao))
# ----------- FUNCOES DO PROGRAMA ------------
def download():
	print('\n Preparando ambiente para instalacao...\n')
	if distro == 'debian' and versao == '9':
		os.system("cp /etc/apt/sources.list /etc/apt/sources.list.old")
		os.system('echo "deb http://deb.debian.org/debian stretch main contrib non-free" > /etc/apt/sources.list')
		os.system('echo "deb-src http://deb.debian.org/debian stretch main contrib non-free" >> /etc/apt/sources.list')
		print('Baixando pacotes...')
		os.system('wget -q https://repo.zabbix.com/zabbix/4.0/debian/pool/main/z/zabbix-release/zabbix-release_4.0-2+stretch_all.deb 1>/dev/null')
		print('Instalando pacotes...')
		os.system('dpkg -i {}/zabbix-release_4.0-2+stretch_all.deb 1>/dev/null'.format(pwd))
		print('Atualizando pacotes...')
		os.system('apt update 1>/dev/null')
	elif distro == 'debian' and versao == '8':
		os.system("cp /etc/apt/sources.list /etc/apt/sources.list.old")
		os.system('echo "deb http://deb.debian.org/debian jessie main contrib non-free" > /etc/apt/sources.list')
		os.system('echo "deb-src http://deb.debian.org/debian jessie main contrib non-free" >> /etc/apt/sources.list')
		print('Baixando pacotes...')
		os.system('wget -q https://repo.zabbix.com/zabbix/4.0/debian/pool/main/z/zabbix-release/zabbix-release_4.0-2+jessie_all.deb 1>/dev/null')
		print('Instalando pacotes...')
		os.system('dpkg -i {}/zabbix-release_4.0-2+jessie_all.deb 1>/dev/null'.format(pwd))
		print('Atualizando pacotes...')
		os.system('apt update 1>/dev/null')
	elif distro == 'debian' and versao == '7':
		os.system("cp /etc/apt/sources.list /etc/apt/sources.list.old")
		os.system('echo "deb http://deb.debian.org/debian wheezy main contrib non-free" > /etc/apt/sources.list')
		os.system('echo "deb-src http://deb.debian.org/debian wheezy main contrib non-free" >> /etc/apt/sources.list')
		print('Baixando pacotes...')
		os.system('wget -q https://repo.zabbix.com/zabbix/4.0/debian/pool/main/z/zabbix-release/zabbix-release_4.0-2+wheezy_all.deb 1>/dev/null')
		print('Instalando pacotes...')
		os.system('dpkg -i {}/zabbix-release_4.0-2+wheezy_all.deb 1>/dev/null'.format(pwd))
		print('Atualizando pacotes...')
		os.system('apt update 1>/dev/null')
	elif distro == 'ubuntu' and versao == '18':
		os.system("cp /etc/apt/sources.list /etc/apt/sources.list.old")
		os.system('echo "deb http://us.archive.ubuntu.com/ubuntu/ bionic main restricted universe multiverse" > /etc/apt/sources.list')
		os.system('echo "deb-src http://us.archive.ubuntu.com/ubuntu/ bionic main restricted universe multiverse" >> /etc/apt/sources.list')
		print('Baixando pacotes...')
		os.system('wget https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+bionic_all.deb 1>/dev/null')
		print('Instalando pacotes...')
		os.system('dpkg -i {}/zabbix-release_4.0-2+bionic_all.deb 1>/dev/null'.format(pwd))
		print('Atualizando pacotes...')
		os.system('apt update 1>/dev/null')
	elif distro == 'ubuntu' and versao == '16':
		os.system("cp /etc/apt/sources.list /etc/apt/sources.list.old")
		os.system('echo "deb http://us.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse" > /etc/apt/sources.list')
		os.system('echo "deb-src http://us.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse" >> /etc/apt/sources.list')
		print('Baixando pacotes...')
		os.system('wget https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+xenial_all.deb 1>/dev/null')
		print('Instalando pacotes...')
		os.system('dpkg -i {}/zabbix-release_4.0-2+xenial_all.deb 1>/dev/null'.format(pwd))
		print('Atualizando pacotes...')
		os.system('apt update 1>/dev/null')
	elif distro == 'ubuntu' and versao == '14':
		os.system("cp /etc/apt/sources.list /etc/apt/sources.list.old")
		os.system('echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty main restricted universe multiverse" > /etc/apt/sources.list')
		os.system('echo "deb-src http://us.archive.ubuntu.com/ubuntu/ trusty main restricted universe multiverse" >> /etc/apt/sources.list')
		print('Baixando pacotes...')
		os.system('wget https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+trusty_all.deb 1>/dev/null')
		print('Instalando pacotes...')
		os.system('dpkg -i {}/zabbix-release_4.0-2+trusty_all.deb 1>/dev/null'.format(pwd))
		print('Atualizando pacotes...')
		os.system('apt update 1>/dev/null')
	elif distro == 'rhel' and versao == '7':
		os.system('rpm -i https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm 1>/dev/null')
	elif distro == 'rhel' and versao == '6':
		os.system('rpm -i https://repo.zabbix.com/zabbix/4.0/rhel/6/x86_64/zabbix-release-4.0-1.el6.noarch.rpm 1>/dev/null')
	else:
		print('\n O programa nao conseguiu identificar o SO e versao especificada: \n {} \n {}'.format(distro, versao))

	print('Preparacao de ambiente completo.')

def repositorio():
	print('Iniciando instalacao do repositorio offline...')
	if distro == 'debian' or distro == 'ubuntu':
		print('Instalando Apache...')
		os.system('apt install apache2 -y 1>/dev/null')
		os.system('mkdir /var/www/html/repozbx/ 1>/dev/null')
		print('Reiniciando Apache...')
		os.system('service apache2 restart 1>/dev/null')
	elif distro == 'rhel':
		print('Instalando Apache...')
		os.system('yum install apache2 -y 1>/dev/null')
		os.system('mkdir /var/www/html/repozbx/ 1>/dev/null')
		print('Reiniciando Apache...')
		os.system('systemctl restart httpd')

	print('Montando repositorio offline aguarde...')
	os.system('wget -q -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/debian/pool/main/z/zabbix-release/zabbix-release_4.0-2+stretch_all.deb')
	os.system('wget -q -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/debian/pool/main/z/zabbix-release/zabbix-release_4.0-2+jessie_all.deb')
	os.system('wget -q -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/3.4/debian/pool/main/z/zabbix-release/zabbix-release_3.4-1+wheezy_all.deb')
	os.system('wget -q -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm')
	os.system('wget -q -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/rhel/6/x86_64/zabbix-release-4.0-1.el6.noarch.rpm')
	os.system('wget -q -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+bionic_all.deb')
	os.system('wget -q -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+xenial_all.deb')
	os.system('wget -q -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+trusty_all.deb')
	print('Repositorio offline pronto.')

def configure():
	conf_file = os.path.isfile('/etc/zabbix/zabbix_proxy.conf')

	if conf_file == 'True':
		os.system('mv /etc/zabbix/zabbix_proxy.conf /etc/zabbix/zabbix_proxy.conf-bkp')
		passdb = commands.getoutput('cat /etc/zabbix/zabbix_proxy.conf-bkp | grep -v "#" | grep "DBPassword=" | cut -d "=" -f 2')
		userdb = commands.getoutput('cat /etc/zabbix/zabbix_proxy.conf-bkp | grep -v "#" | grep "DBUser=" | cut -d "=" -f 2')
		namedb = commands.getoutput('cat /etc/zabbix/zabbix_proxy.conf-bkp | grep -v "#" | grep "DBName=" | cut -d "=" -f 2')
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
	ipa = raw_input('Qual o ip do proxy?: ')
	
	if conf_file == 'True':
		os.system('mv /etc/zabbix/zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf-bkp')
	
	conf = open("/etc/zabbix/zabbix_agentd.conf","w +")
	conf.write("PidFile=/var/run/zabbix/zabbix_agentd.pid\nLogFile=/var/log/zabbix/zabbix_agentd.log\nLogFileSize=0\nEnableRemoteCommands=1\nServer={}\nHostname={}\nTimeout=30\nAllowRoot=1\nInclude=/etc/zabbix/zabbix_agentd.d/*.conf\nUserParameters=zbx_upd[*],/etc/zabbix/scripts/zbx_agnt_lnx.sh update {} {}".format(ipa, hostname, distro, versao))
	conf.close()

def install():
	clearner()
	download()
	comando_sql = "grant all privileges on zabbix.* to zabbix@localhost identified by '_zabbix@sql';"
	if distro == 'debian' or distro == 'ubuntu':
		print('Pre-instalando mais alguns pacotes necessarios...')
		os.system('apt install -y vim mlocate snmp-mibs-downloader snmp htop 1>/dev/null')
		print('Instalando sistema...')
		os.system('apt install -y mysql-server zabbix-proxy-mysql zabbix-get zabbix-agent 1>/dev/null')
		os.system('service mysql start')
		print('Criando banco de dados...')
		os.system('mysql -uroot -p -e"create database zabbix character set utf8 collate utf8_bin;"')
		os.system('mysql -uroot -p -e"{}"'.format(comando_sql))
		os.system('zcat /usr/share/doc/zabbix-proxy-mysql*/schema.sql.gz | mysql -Dzabbix -uzabbix -p_zabbix@sql')
		configure()
		configure_agent()
		os.system('update-rc.d zabbix-proxy enable')
		clearner()
		repositorio()

		# --- INICIANDO SISTEMA ---
		log = raw_input('Iniciando sistema... Deseja acompanhar os logs?(s/N): ')
		if log == 's' or log == 'S':
			os.system('service zabbix-proxy start')
			os.system('sleep 3')
			os.system('tail /var/log/zabbix/zabbix_proxy.log')
		elif log == 'n' or log =='N':
			os.system('service zabbix-proxy start')
			print('Zabbix Proxy iniciado... Instalacao concluida com sucesso\n')
		else:
			print('\n Instalacao foi concluida, porem o sistema nao foi iniciado.\n Voce nao informou nenhum parametro valido.\n\tExecute agora "service zabbix-proxy start" para iniciar o sistema.\n')

	elif distro == 'rhel':
		print('Pre-instalando pacotes necessarios...')
		os.system('yum install vim mlocate snmp-mibs-downloader snmp htop -y 1>/dev/null')
		print('Instalando sistema...')
		os.system('yum install mariadb-server zabbix-proxy-mysql zabbix-get zabbix-agent -y 1>/dev/null')
		os.system('systemctl start mariadb')
		os.system('systemctl enable mariadb')
		print('Criando bando de dados...')
		os.system('mysql -uroot -p -e"create database zabbix character set utf8 collate utf8_bin;"')
		os.system('mysql -uroot -p -e"{}"'.format(comando_sql))
		os.system('zcat /usr/share/doc/zabbix-proxy-mysql*/schema.sql.gz | mysql -Dzabbix -uzabbix -p_zabbix@sql')
		configure()
		configure_agent()
		repositorio()
		# --- INICIANDO SISTEMA ---
		log = raw_input('Iniciando sistema... Deseja acompanhar os logs?(s/N): ')
		if log == 's' or log == 'S' and versao == '7':
			os.system("systemctl enable zabbix-proxy")
			os.system('systemctl start zabbix-proxy')
			os.system('sleep 3')
			os.system('tail /var/log/zabbix_proxy.log')
		elif log =='n' or log == 'N' and versao == '7':
			os.system("systemctl enable zabbix-proxy")
			os.system('systemctl start zabbix-proxy')
		elif log == 's' or log == 'S' and versao == '6':
			os.system('chkconfig --level 12345 zabbix-proxy on')
			os.system('systemctl start zabbix-proxy')
			os.system('sleep 3')
			os.system('tail /var/log/zabbix_proxy.log')
		elif log == 'n' or log == 'N' and versao == '6':
			os.system('chkconfig --level 12345 zabbix-proxy on')
			os.system('systemctl start zabbix-proxy')
		else:
			print('\n Instalacao foi concluida, porem o sistema nao foi iniciado.\n Voce nao informou nenhum parametro valido.\n\tExecute agora "systemctl start zabbix-proxy" para iniciar o sistema.\n')

def agent():
	clearner()
	download()
	if distro == 'debian' or distro == 'ubuntu':
		print('Iniciando a instalacao do agente')
		os.system('apt install zabbix-agent -y 1>/dev/null')
		configure_agent()
		clearner()
		
		# --- INICIANDO SISTEMA ---
		log = raw_input('Iniciando sistema... Deseja acompanhar os logs?(s/N): ')
		if log == 's' or log == 'S':
			os.system('service zabbix-agent start')
			os.system('sleep 3')
			os.system('tail /var/log/zabbix/zabbix_agentd.log')
		elif log == 'n' or log =='N':
			os.system('service zabbix-agent start')
			print('Zabbix agent iniciado... Instalacao concluida com sucesso\n')
		else:
			print('\n Instalacao foi concluida, porem o sistema nao foi iniciado.\n Voce nao informou nenhum parametro valido.\n\tExecute agora "service zabbix-proxy start" para iniciar o sistema.\n')

	elif distro == 'rhel':
		print('Pre-instalando pacotes necessarios...')
		os.system('yum install zabbix-agent -y 1>/dev/null')
		configure_agent()
		clearner()
		os.system("systemctl restart zabbix-agent")
		print('Reiniciando agente')
		print('Instalacao concluida com sucesso...')


def update():
	download()
	os.system("apt-get upgrade -y")

def ajudante():
	clearner()
	print('\nPara ajuda pesquise no google.com')
# ----- CONTROLADOR DE FLUXO SECUNDARIO -----
def menu():
	acao = raw_input('--- Escolha uma opcao do menu ---\n\n[1] - Instalar\t\tExecuta a instalacao do proxy e agente Zabbix.\n[2] - Update\t\tExecuta o upgrade dos pacotes Zabbix.\n[3] - Repositorio\tConstroe o repositorio offline do Zabbix para este ambiente.\n[4] - Download\t\tFaz o download dos repositorios Zabbix, mas nao executa a instalacao do sistema.\n[9] - Help\t\tVai precisar de mais ajuda do que o que ja ta explicando aqui? Serio?\n\n[0] - Exit\t\tSai do programa.\n\n[+] - Selecione uma opcao[0-7]: \n\n')
	if acao == '1':
		install()
	elif acao == '2':
		update()
	elif acao == '3':
		repositorio()
	elif acao == '4':
		download()
	elif acao == '5':
		agent()
	elif acao == '9':
		ajudante()
	elif acao == '0':
		exit()
	else:
		print('Voce informou a opcao {} e ela nao e valida!!!\n'.format(acao))
		menu()
	
# --------- CONTROLADOR DO FLUXO INICIAL ----
def main():
	if confirma == 's' or confirma == 'S':
		print('')
		menu()
	elif confirma == 'n' or confirma == 'N':
		print('')
		distro = raw_input('Informe a distro deste SO. (debian/ubuntu/rhel): ')
		versao = raw_input('Informe a versao da distro informada: ')
		menu()
main()
