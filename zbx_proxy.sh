#!/bin/bash
########DEBUG ZONE#######
#trap read DEBUG		#
#set -x 				#
#########################

########VARIAVEIS########
JOB=$1
DISTRO=$2
VERSAO=$3
HOST=$(hostname)
#########################
function configure () {
	
	mv /etc/zabbix/zabbix_proxy.conf /etc/zabbix/zabbix_proxy.conf-bkp
		if test "$JOB" = "update"
			then
				PASSDB=$(cat /etc/zabbix/zabbix_proxy.conf-bkp | grep -v "#" | grep "DBPassword=" | cut -d "=" -f 2)
				USERDB=$(cat /etc/zabbix/zabbix_proxy.conf-bkp | grep -v "#" | grep "DBUser=" | cut -d "=" -f 2)
				NAMEDB=$(cat /etc/zabbix/zabbix_proxy.conf-bkp | grep -v "#" | grep "DBName=" | cut -d "=" -f 2)
		elif test "$JOB" = "install"
			then
				PASSDB="_zabbix@sql"
				USERDB="zabbix"
				NAMEDB="zabbix"
		fi


	touch -c /etc/zabbix/zabbix_proxy.conf
	echo "CacheSize=1G" >> /etc/zabbix/zabbix_proxy.conf
    echo "DBName=$NAMEDB" >> /etc/zabbix/zabbix_proxy.conf
    echo "DBPassword=$PASSDB" >> /etc/zabbix/zabbix_proxy.conf
    echo "DBUser=$USERDB" >> /etc/zabbix/zabbix_proxy.conf
    echo "DebugLevel=3" >> /etc/zabbix/zabbix_proxy.conf
    echo "EnableRemoteCommands=1" >> /etc/zabbix/zabbix_proxy.conf
    echo "ExternalScripts=/usr/lib/zabbix/externalscripts" >> /etc/zabbix/zabbix_proxy.conf
    echo "Fping6Location=/usr/sbin/fping6" >> /etc/zabbix/zabbix_proxy.conf
    echo "FpingLocation=/usr/sbin/fping" >> /etc/zabbix/zabbix_proxy.conf
    echo "HistoryCacheSize=128M" >> /etc/zabbix/zabbix_proxy.conf
    echo "HistoryIndexCacheSize=32M" >> /etc/zabbix/zabbix_proxy.conf
    echo "Hostname=$HOST" >> /etc/zabbix/zabbix_proxy.conf
    echo "LogFileSize=1024" >> /etc/zabbix/zabbix_proxy.conf
    echo "LogFile=/var/log/zabbix/zabbix_proxy.log" >> /etc/zabbix/zabbix_proxy.conf
    echo "LogSlowQueries=3000" >> /etc/zabbix/zabbix_proxy.conf
    echo "PidFile=/var/run/zabbix/zabbix_proxy.pid" >> /etc/zabbix/zabbix_proxy.conf
    echo "Server=monitoramento.tradein.com.br" >> /etc/zabbix/zabbix_proxy.conf
    echo "SNMPTrapperFile=/var/log/snmptrap/snmptrap.log" >> /etc/zabbix/zabbix_proxy.conf
    echo "SocketDir=/var/run/zabbix" >> /etc/zabbix/zabbix_proxy.conf
    echo "StartDBSyncers=8" >> /etc/zabbix/zabbix_proxy.conf
    echo "StartPingers=10" >> /etc/zabbix/zabbix_proxy.conf
    echo "StartPollers=10" >> /etc/zabbix/zabbix_proxy.conf
    echo "StartPollersUnreachable=5" >> /etc/zabbix/zabbix_proxy.conf
    echo "Timeout=30" >> /etc/zabbix/zabbix_proxy.conf
    echo "UnreachablePeriod=60" >> /etc/zabbix/zabbix_proxy.conf
}

function download (){

	if test $DISTRO = debian 2>/dev/null
		then
			if test	$VERSAO = "9" 2>/dev/null
				then
					wget https://repo.zabbix.com/zabbix/4.0/debian/pool/main/z/zabbix-release/zabbix-release_4.0-2+stretch_all.deb
					dpkg -i zabbix-release_4.0-2+stretch_all.deb
					apt update
			elif test $VERSAO = "8" 2>/dev/null
				then
					wget https://repo.zabbix.com/zabbix/4.0/debian/pool/main/z/zabbix-release/zabbix-release_4.0-2+jessie_all.deb
					dpkg -i zabbix-release_4.0-2+jessie_all.deb
					apt update
			elif test $VERSAO = "7" 2>/dev/null
				then
					wget https://repo.zabbix.com/zabbix/3.4/debian/pool/main/z/zabbix-release/zabbix-release_3.4-1+wheezy_all.deb
					dpkg -i zabbix-release_3.4-1+wheezy_all.deb
					apt update
			else
				echo "VERSAO DEBIAN NAO SUPORTADA. [9/8/7]?"
			fi
	elif test $DISTRO = ubuntu 2>/dev/null
		then
			if test	$VERSAO = "18" 2>/dev/null
				then
					wget https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+bionic_all.deb
					dpkg -i zabbix-release_4.0-2+bionic_all.deb
					apt update
			elif test $VERSAO = "16" 2>/dev/null
				then
					wget https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+xenial_all.deb
					dpkg -i zabbix-release_4.0-2+xenial_all.deb
					apt update
			elif test $VERSAO = "14" 2>/dev/null
				then
					wget https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+trusty_all.deb
					dpkg -i zabbix-release_4.0-2+trusty_all.deb
					apt update
			else 
				echo "VERSAO NAO SUPORTADA. [18/16/14]?"
			fi
	elif test  $DISTRO = rhel 2>/dev/null
		then
			if test $VERSAO = "7" 2>/dev/null
				then
					rpm -i https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm
			elif test $VERSAO= "6" 2>/dev/null
				then
					rpm -i https://repo.zabbix.com/zabbix/4.0/rhel/6/x86_64/zabbix-release-4.0-1.el6.noarch.rpm 
			else
				echo "VERSAO NAO SUPORTADA. [7/6]?"
			fi
	else
		echo "o script não ta reconhecendo esta distro ta colocando ql?[debian/ubuntu/rhel]?"
	fi
}

function install () {
	if test $DISTRO = debian 2>/dev/null
		then
			apt install mysql-server zabbix-proxy-mysql
			service mysql start
			echo "Se durante a instalacao do mysql, o mesmo solicitou uma senha informe-a agora.
			Caso não tenha solicitado, apenas aperte enter"
			mysql -uroot -p -e"create database zabbix character set utf8 collate utf8_bin;"
			mysql -uroot -p -e"grant all privileges on zabbix.* to zabbix@localhost identified by '_zabbix@sql';"
			zcat /usr/share/doc/zabbix-proxy-mysql*/schema.sql.gz | mysql -Dzabbix -uzabbix -p_zabbix@sql
			configure
			update-rc.d zabbix-proxy enable
			service zabbix-proxy start | tail -f /var/log/zabbix/zabbix_proxy.log
	elif test $DISTRO = ubuntu 2>/dev/null
		then
			apt install mysql-server zabbix-proxy-mysql
			service mysql start
			echo "Se durante a instalacao do mysql, o mesmo solicitou uma senha informe-a agora.
			Caso não tenha solicitado, apenas aperte enter"
			mysql -uroot -p -e"create database zabbix character set utf8 collate utf8_bin;"
			mysql -uroot -p -e"grant all privileges on zabbix.* to zabbix@localhost identified by '_zabbix@sql';"
			zcat /usr/share/doc/zabbix-proxy-mysql*/schema.sql.gz | mysql -Dzabbix -uzabbix -p_zabbix@sql
			configure
			update-rc.d zabbix-proxy enable
			service zabbix-proxy start | tail -f /var/log/zabbix/zabbix_proxy.log
	elif test  $DISTRO = rhel 2>/dev/null
		then
			yum install zabbix-proxy-mysql mariadb-server
			systemctl start mariadb-server 
			systemctl enable mariadb-server
			echo "Se durante a instalacao do mysql, o mesmo solicitou uma senha informe-a agora. Caso não tenha solicitado, apenas aperte enter"
			mysql -uroot -p -e"create database zabbix character set utf8 collate utf8_bin;"
			mysql -uroot -p -e"grant all privileges on zabbix.* to zabbix@localhost identified by '_zabbix@sql';"
			zcat /usr/share/doc/zabbix-proxy-mysql*/schema.sql.gz | mysql -Dzabbix -uzabbix -p_zabbix@sql
			if test $VERSAO = "7" 2>/dev/null
				then
					systemctl enable zabbix-proxy
			elif test $VERSAO= "6" 2>/dev/null
				then
					chkconfig --level 12345 zabbix-proxy on
			fi
			configure
			systemctl start zabbix-proxy | tail -f /var/log/zabbix_proxy.log
	else
		echo "O script não sabe o quê ta fazendo, ele travou na hora de instalar os pacotes"
	fi
}

function update () {
	if test $DISTRO = debian 2>/dev/null
		then
			apt upgrade zabbix-proxy-mysql
			service zabbix-proxy restart | tail -f /var/log/zabbix/zabbix_proxy.log
	elif test $DISTRO = ubuntu 2>/dev/null
		then
			apt upgrade zabbix-proxy-mysql
			service zabbix-proxy restart | tail -f /var/log/zabbix/zabbix_proxy.log
	elif test  $DISTRO = rhel 2>/dev/null
		then
			yum upgrade zabbix-proxy-mysql
			systemctl restart zabbix-proxy | tail -f /var/log/zabbix/zabbix_proxy.log
	fi
}

function repositorio () {
	if test $DISTRO = debian 2>/dev/null
		then
			apt install apache2
			mkdir /var/www/html/repozbx/
			service apache2 restart
	elif test $DISTRO = ubuntu 2>/dev/null
		then
			apt install apache2
			mkdir /var/www/html/repozbx/
			service apache2 restart
	elif test  $DISTRO = rhel 2>/dev/null
		then
			yum install httpd
			mkdir /var/www/html/repozbx/
			systemctl restart httpd
	fi
			wget -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/debian/pool/main/z/zabbix-release/zabbix-release_4.0-2+stretch_all.deb
			wget -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/debian/pool/main/z/zabbix-release/zabbix-release_4.0-2+jessie_all.deb
			wget -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/3.0/debian/pool/main/z/zabbix-release/zabbix-release_3.4-1+wheezy_all.deb
			wget -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm
			wget -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/rhel/6/x86_64/zabbix-release-4.0-1.el6.noarch.rpm
			wget -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+bionic_all.deb
			wget -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+xenial_all.deb
			wget -c -P /var/www/html/repozbx/ https://repo.zabbix.com/zabbix/4.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_4.0-2+trusty_all.deb

}

if test "$JOB" = install
	then
		install
	elif test "$JOB" = download
		then
			download
	elif test "$JOB" = update
		then
			update
	elif test "$JOB" = repositorio
		then
			repositorio
	else
		echo "funcao nao suportada"
	fi
