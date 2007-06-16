# TODO:
# - PLD patch renames man.conf to man.config, but all manuals are named man.conf(5)
Summary:	Manual page reader
Summary(de.UTF-8):	Manual-Page-Reader
Summary(es.UTF-8):	Lector de páginas de manual (man)
Summary(fr.UTF-8):	Lecteur de pages de man
Summary(ko.UTF-8):	문서 관련 도구 모음 : 맨, apropos 그리고 whatis
Summary(pl.UTF-8):	Czytnik stron man
Summary(pt_BR.UTF-8):	Leitor de páginas de manuais (man)
Summary(ru.UTF-8):	Набор утилит для документации: man, apropos и whatis
Summary(tr.UTF-8):	Kılavuz sayfası okuyucusu
Summary(uk.UTF-8):	Набір утиліт для документації: man, apropos та whatis
Name:		man
Version:	1.6e
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://primates.ximian.com/~flucifredi/man/%{name}-%{version}.tar.gz
# Source0-md5:	d8187cd756398baefc48ba7d60ff6a8a
Source1:	makewhatis.crondaily
Source2:	makewhatis.cronweekly
Source3:	%{name}-additional-%{name}-pages.tar.bz2
# Source3-md5:	16c3fde2243289524cf40c1d2e7150e4
Source4:	%{name}-mess.ru
Patch0:		%{name}-manpaths.patch
Patch1:		%{name}-PLD.patch
Patch2:		%{name}-fhs.patch
Patch3:		%{name}-safer.patch
Patch4:		%{name}-security.patch
Patch5:		%{name}-roff.patch
Patch6:		%{name}-sofix.patch
Patch7:		%{name}-bug11621.patch
Patch8:		%{name}-gencat.patch
Patch9:		%{name}-nls-priority.patch
Patch10:	%{name}-pmake.patch
Patch11:	%{name}-fmntbug.patch
Patch12:	%{name}-awk_path.patch
Patch13:	%{name}-cgi_paths.patch
Patch14:	%{name}-relat.patch
Patch15:	%{name}-encoding.patch
Patch16:	%{name}-man-pages.patch
Patch17:	%{name}-i18n_nroff.patch
Patch18:	%{name}-i18n_makewhatis.patch
Patch19:	%{name}-apropos.patch
Patch20:	%{name}-rpm.patch
URL:		http://primates.ximian.com/~flucifredi/man/
BuildRequires:	iconv
BuildRequires:	less
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
Requires(post,preun):	fileutils
Requires:	%{name}-config = %{version}-%{release}
Requires:	/bin/awk
Requires:	groff >= 1:1.18.1.4
Requires:	gzip
Requires:	iconv
Requires:	less
Requires:	mktemp >= 1.5-8
Obsoletes:	man-cs
Obsoletes:	man-da
Obsoletes:	man-de
Obsoletes:	man-es
Obsoletes:	man-fr
Obsoletes:	man-it
Obsoletes:	man-nl
Obsoletes:	man-pl
Obsoletes:	man-pt
Obsoletes:	man-sl
Conflicts:	tmpwatch < 2.9.6-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cgibinmandir		/usr/lib/cgi-bin/man
%define		_cgiauxmandir		/usr/share/man2html-cgi
%define		_webapps	/etc/webapps
%define		_webapp		man2html
%define		_webappdir	%{_webapps}/%{_webapp}

%description
The man package includes three tools for finding information and/or
documentation about your Linux system: man, apropos and whatis. The
man system formats and displays on-line manual pages about commands or
functions on your system. Apropos searches the whatis database
(containing short descriptions of system commands) for a string.
Whatis searches its own database for a complete word.

Whatis and apropos are in a separate package, man-whatis.

%description -l de.UTF-8
Die man-Seiten-Suite, einschließlich Handbuch, Apropos und Whatis.
Diese Programme dienen zum Einsehen des Großteils der Dokumentation,
die auf einem Linux-System verfügbar ist. Die Whatis- und
Apropos-Programme dienen dazu, Beschreibungen zu bestimmten Themen zu
finden.

whatis und apropos sind im Paket man-whatis.

%description -l es.UTF-8
Es un conjunto de páginas de manual, incluyendo man, apropos y whatis.
Estos programas se usan para leer la mayoría de la documentación
disponible en el sistema Linux. Los programas whatis y apropos pueden
ser usados para encontrar documentación relacionada con un asunto
particular.

%description -l fr.UTF-8
Ensemble des pages man. Contient man, apropos et whatis. Ces
programmes servent à lire la plupart de la documentation disponible
sur un système Linux. Les programmes whatis et apropos servent à
trouver la documentation relative à un sujet précis.

%description -l pl.UTF-8
Pakiet man zawiera man, apropos i whatis. Te programy są używane do
czytania większości dokumentacji dostępnej w systemie Linux. Programy
whatis i apropos mogą być użyte do znalezienia dokumentacji na tematy
powiązane z poszukiwanym.

Narzędzia whatis i apropos są w oddzielnym pakiecie - man-whatis.

%description -l pt_BR.UTF-8
É um conjunto de páginas de manual, incluindo man, apropos e whatis.
Estes programas são usados para ler a maioria da documentação
disponível no sistema Linux. Os programas whatis e apropos podem ser
usados para achar documentação relacionada com um assunto particular.

%description -l tr.UTF-8
Kılavuz sayfa takımı: man, apropos, whatis. Bu programlar Linux
sisteminde bulunan birçok belgenin okunmasında kullanylyr. whatis ve
apropos programları özel bir konu ile alakalı belgeleri bulmak için
kullanılabilir.

%description -l ru.UTF-8
Пакет man содержит три утилиты для поиска информации и/или
документации о вашей системе: man, apropos и whatis. Система man
форматирует и показывает онлайновые страницы мануала о командах и
функциях вашей системы. Apropos ищет заданную строку в базе данных
whatis (содержащей короткие описания системных команд). Whatis ищет в
своей базе данных завершенные слова.

%description -l uk.UTF-8
Пакет man містить три утиліти для пошуку інформації та/або
документації про вашу систему: man, apropos та whatis. Система man
форматує та показує онлайнові сторінки мануалу про команди та функції
вашої системи. Apropos шукає заданий рядок у базі даних whatis (яка
містить короткі описи системних команд). Whatis шукає у своїй базі
закінчені слова.

%package config
Summary:	Manual page reader configuration
Summary(pl.UTF-8):	Konfiguracja czytników podręczników
Group:		Applications/System

%description config
Configuration file for different manual page browsers.

%description config -l pl.UTF-8
Plik konfiguracyjny dla różnych czytników podręczników.

%package whatis
Summary:	whatis utilities
Summary(pl.UTF-8):	Narzędzia whatis
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	crondaemon

%description whatis
This package provides the following utilities: apropos, whatis and
makewhatis.

%description whatis -l pl.UTF-8
Ten pakiet dostracza następujące narzędzia: apropos, whatis i
makewhatis.

%package -n man2html
Summary:	manroff to html converter
Summary(pl.UTF-8):	Konwerter formatu manroff na html
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n man2html
This program can convert man pages stored in manroff format to html.

%description -n man2html -l pl.UTF-8
Program man2html służy do konwersji plików manuala zapisanych w
formacie manroff na format html.

%package -n man2html-cgi
Summary:	CGI interface to man2html
Summary(pl.UTF-8):	Interfejs CGI dla man2html
Group:		Applications/System
Requires:	%{name}-whatis = %{version}-%{release}
Requires:	filesystem >= 3.0-11
Requires:	man2html = %{version}-%{release}
Requires:	webapps
Conflicts:	apache-base < 2.2.0-7.2
Conflicts:	apache1 < 1.3.34-5.11

%description -n man2html-cgi
These scripts allows read man pages throught WWW browser. It uses
man2htlm program to convert man pages to html format. Scripts are
still in alpha stage, could be not secure.

%description -n man2html-cgi -l pl.UTF-8
Skrypty znajdujące się w pakiecie pozwalają czytać strony man przy
pomocy przeglądarki WWW. Skrtpty wykorzystują program man2html do
konwersji stron man na html. Programy są ciągle w stadium alfa i mogą
nie być bezpieczne.

%prep
%setup -q -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1

cp -f %{SOURCE4} msgs/mess.ru   # replace bad ru trans

for i in $(find man -name man.conf.man); do
	mv $i ${i%man.conf.man}man.config.man
done

for src in msgs/mess.[a-z][a-z]; do
	lang=${src##*.}
	case ${lang} in
		ja) charset=euc-jp ;;
		ko) charset=euc-kr ;;
		ru) charset=koi8-r ;;
		da) charset=iso-8859-1 ;;
		de) charset=iso-8859-1 ;;
		en) charset=iso-8859-1 ;;
		es) charset=iso-8859-1 ;;
		fi) charset=iso-8859-1 ;;
		fr) charset=iso-8859-1 ;;
		it) charset=iso-8859-1 ;;
		pt) charset=iso-8859-1 ;;
		nl) charset=iso-8859-1 ;;
		cs) charset=iso-8859-2 ;;
		hr) charset=iso-8859-2 ;;
		pl) charset=iso-8859-2 ;;
		ro) charset=iso-8859-2 ;;
		sl) charset=iso-8859-2 ;;
		hu) charset=iso-8859-2 ;;
		bg) charset=cp1251 ;;
		el) charset=iso-8859-7 ;;
		*)
			echo "=== LANGUAGE ${lang}: MUST SPECIFY CHARSET/ENCODING"
			exit 1
		;;
	esac
	iconv -t utf-8 -f ${charset} -o ${src}.utf ${src} && mv ${src}.utf ${src}
done

# use gzip (not bzip2) to compress formatted man pages
%{__sed} -i -e 's/compress=$/compress=gzip/' configure

cat << 'EOF' > apache.conf
ScriptAlias /cgi-bin/man %{_cgibinmandir}
<Directory %{_cgibinmandir}>
	Allow from all
</Directory>
EOF

%build
./configure \
	-default \
	+fhs \
	+lang all \
	-confdir %{_sysconfdir}

# HACK: Make output default to using -c; otherwise it appears broken.
%{__sed} -i -e 's/nroff /nroff -c /' conf_script

%{__make} \
	BUILD_CC="%{__cc} %{rpmcflags} %{rpmldflags}" \
	CC="%{__cc} %{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/cron.{daily,weekly},%{_bindir},%{_mandir},%{_sbindir},%{_cgibinmandir},%{_cgiauxmandir}} \
	$RPM_BUILD_ROOT{%{_mandir}/{hu,ja,ko}/man{1,5,8},%{_webappdir},/etc/tmpwatch}

echo '# Cleanup man temporary files:' > $RPM_BUILD_ROOT/etc/tmpwatch/man.conf
echo "/var/cache/man 240 -d" >> $RPM_BUILD_ROOT/etc/tmpwatch/man.conf
> man.lang
for i in '' bg ca cs da de el eo es fi fr gl hr hu id it ja ko nl pl pt pt_BR ro ru \
	 sk sl sr sv tr uk zh_CN zh_TW; do
	if [ "$i" ]; then
		lng="%lang($i) "
		i="/$i"
	else
		lng=""
	fi
	for cdir in '' /local ; do
		install -d $RPM_BUILD_ROOT/var/cache/man${cdir}$i/cat{1,2,3,4,5,6,7,8,9,n}
		echo "${lng}%dir /var/cache/man${cdir}$i" >> man.lang
		echo "${lng}%attr(775,root,man) /var/cache/man${cdir}$i/cat[1-9n]" >> man.lang
	done
done

%{__make} install \
	PREFIX="$RPM_BUILD_ROOT"

%{__make} -C man2html install-scripts \
	PREFIX="$RPM_BUILD_ROOT"

dir=$RPM_BUILD_ROOT%{_mandir}
for src in man/{*/,}*/*.[1-9n]; do
	# src is like: man/nl/man.config.5 or man/pl/man1/man2html.1
	noman=${src#*/}
	lang=${noman%%%%/*}
	page=${src##*/}
	sect=man${src##*.}

	case ${lang} in
		ja) charset=euc-jp ;;
		ko) charset=euc-kr ;;
		ru) charset=koi8-r ;;
		da) charset=iso-8859-1 ;;
		de) charset=iso-8859-1 ;;
		en) charset=iso-8859-1 ;;
		es) charset=iso-8859-1 ;;
		fi) charset=iso-8859-1 ;;
		fr) charset=iso-8859-1 ;;
		it) charset=iso-8859-1 ;;
		pt) charset=iso-8859-1 ;;
		nl) charset=iso-8859-1 ;;
		cs) charset=iso-8859-2 ;;
		hr) charset=iso-8859-2 ;;
		pl) charset=iso-8859-2 ;;
		ro) charset=iso-8859-2 ;;
		sl) charset=iso-8859-2 ;;
		hu) charset=iso-8859-2 ;;
		bg) charset=cp1251 ;;
		el) charset=iso-8859-7 ;;
		*)
			echo "=== LANGUAGE ${lang}: MUST SPECIFY CHARSET/ENCODING"
			exit 1
		;;
	esac
	mkdir -p ${dir}/${lang}/${sect}
	iconv -t utf-8 -f ${charset} -o ${dir}/${lang}/${sect}/${page} ${src}

	# ensure POSIX/C locale only has ASCII subset and no latin-1
	if [ ${lang} = en ]; then
		mkdir -p ${dir}/${sect}
		iconv -t ascii//translit -f ${charset} -o ${dir}/${sect}/${page} ${src}
	fi
done

rm -rf $RPM_BUILD_ROOT%{_mandir}/en

# for man_db and xman compatibility
ln -sf soelim $RPM_BUILD_ROOT%{_bindir}/zsoelim

install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.daily/makewhatis
install %{SOURCE2} $RPM_BUILD_ROOT/etc/cron.weekly/makewhatis

touch $RPM_BUILD_ROOT/var/cache/man/whatis

install man/el/hman.man $RPM_BUILD_ROOT%{_mandir}/el/man1/hman.1
install man/el/man2html.man $RPM_BUILD_ROOT%{_mandir}/el/man1/man2html.1
install man/hu/man1/* $RPM_BUILD_ROOT%{_mandir}/hu/man1
install man/ja/man1/{hman,man2html}.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1
install man/ja/man8/makewhatis.8 $RPM_BUILD_ROOT%{_mandir}/ja/man8
install man/pl/man1/man2html.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1
install man/ro/man2html.man $RPM_BUILD_ROOT%{_mandir}/ro/man1/man2html.1

install apache.conf $RPM_BUILD_ROOT%{_webappdir}/apache.conf
install apache.conf $RPM_BUILD_ROOT%{_webappdir}/httpd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%pre
rm -f /var/cache/man/X11/cat[123456789n]/*
rm -f /var/cache/man/X11R6/cat[123456789n]/*
rm -f /var/cache/man/X11R6/??/cat[123456789n]/*
rm -f /var/cache/man/X11R6/??_??/cat[123456789n]/*

%preun
rm -f /var/cache/man/cat[123456789n]/*
rm -f /var/cache/man/local/cat[123456789n]/*
rm -f /var/cache/man/??/cat[123456789n]/*
rm -f /var/cache/man/??_??/cat[123456789n]/*
rm -f /var/cache/man/local/??/cat[123456789n]/*
rm -f /var/cache/man/local/??_??/cat[123456789n]/*

%post
rm -f /var/cache/man/cat[123456789n]/*
rm -f /var/cache/man/local/cat[123456789n]/*
rm -f /var/cache/man/??/cat[123456789n]/*
rm -f /var/cache/man/??_??/cat[123456789n]/*
rm -f /var/cache/man/local/??/cat[123456789n]/*
rm -f /var/cache/man/local/??_??/cat[123456789n]/*

%triggerin -n man2html-cgi -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -n man2html-cgi -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -n man2html-cgi -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -n man2html-cgi -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerpostun -n man2html-cgi -- man2html-cgi < 1.6b-2.16
# rescue apache config
if [ -f /etc/man/apache-man2html-cgi.conf.rpmsave ]; then
	if [ -d /etc/apache/webapps.d ]; then
		cp -f %{_webappdir}/apache.conf{,.rpmnew}
		cp -f /etc/man/apache-man2html-cgi.conf.rpmsave %{_webappdir}/apache.conf
	fi

	if [ -d /etc/httpd/webapps.d ]; then
		cp -f %{_webappdir}/httpd.conf{,.rpmnew}
		cp -f /etc/man/apache-man2html-cgi.conf.rpmsave %{_webappdir}/httpd.conf
	fi
	rm -f /etc/man/apache-man2html-cgi.conf.rpmsave
fi

# re-register with webapp
if [ -L /etc/apache/conf.d/09_man.conf ]; then
	rm -f /etc/apache/conf.d/09_man.conf
	/usr/sbin/webapp register apache %{_webapp}
	%service -q apache reload
fi
if [ -L /etc/httpd/httpd.conf/09_man.conf ]; then
	rm -f /etc/httpd/httpd.conf/09_man.conf
	/usr/sbin/webapp register httpd %{_webapp}
	%service -q httpd reload
fi

%files -f man.lang
%defattr(644,root,root,755)
%doc HISTORY README TODO
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/tmpwatch/*.conf
%attr(2755,root,man) %{_bindir}/man
%attr(755,root,root) %{_bindir}/man2dvi
%attr(755,root,root) %{_bindir}/zsoelim
%{_mandir}/man1/man.1*

# Supported languages bg cs da de en es fi fr hr it ja nl pl pt ro sl  + hu
%lang(bg) %{_mandir}/bg/man1/man.1*
%lang(cs) %{_mandir}/cs/man1/man.1*
%lang(da) %{_mandir}/da/man1/man.1*
%lang(de) %{_mandir}/de/man1/man.1*
%lang(el) %{_mandir}/el/man1/man.1*
%lang(es) %{_mandir}/es/man1/man.1*
%lang(fi) %{_mandir}/fi/man1/man.1*
%lang(fr) %{_mandir}/fr/man1/man.1*
%lang(hr) %{_mandir}/hr/man1/man.1*
%lang(hu) %{_mandir}/hu/man1/man.1*
%lang(it) %{_mandir}/it/man1/man.1*
%lang(ja) %{_mandir}/ja/man1/man.1*
%lang(ko) %{_mandir}/ko/man1/man.1*
%lang(nl) %{_mandir}/nl/man1/man.1*
%lang(pl) %{_mandir}/pl/man1/man.1*
%lang(pt) %{_mandir}/pt/man1/man.1*
%lang(ro) %{_mandir}/ro/man1/man.1*
%lang(sl) %{_mandir}/sl/man1/man.1*

%{_datadir}/locale/en/man
%lang(bg) %{_datadir}/locale/bg/man
%lang(cs) %{_datadir}/locale/cs/man
%lang(da) %{_datadir}/locale/da/man
%lang(de) %{_datadir}/locale/de/man
%lang(el) %{_datadir}/locale/el/man
%lang(es) %{_datadir}/locale/es/man
%lang(fi) %{_datadir}/locale/fi/man
%lang(fr) %{_datadir}/locale/fr/man
%lang(hr) %{_datadir}/locale/hr/man
%lang(it) %{_datadir}/locale/it/man
%lang(ja) %{_datadir}/locale/ja/man
%lang(ko) %{_datadir}/locale/ko/man
%lang(nl) %{_datadir}/locale/nl/man
%lang(pl) %{_datadir}/locale/pl/man
%lang(pt) %{_datadir}/locale/pt/man
%lang(ro) %{_datadir}/locale/ro/man
%lang(ru) %{_datadir}/locale/ru/man
%lang(sl) %{_datadir}/locale/sl/man

%files config
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/man.config
%{_mandir}/man5/*
%lang(bg) %{_mandir}/bg/man5/*
%lang(cs) %{_mandir}/cs/man5/*
%lang(da) %{_mandir}/da/man5/*
%lang(de) %{_mandir}/de/man5/*
%lang(el) %{_mandir}/el/man5/*
%lang(es) %{_mandir}/es/man5/*
%lang(fi) %{_mandir}/fi/man5/*
%lang(fr) %{_mandir}/fr/man5/*
%lang(hr) %{_mandir}/hr/man5/*
%lang(it) %{_mandir}/it/man5/*
%lang(ja) %{_mandir}/ja/man5/*
%lang(ko) %{_mandir}/ko/man5/*
%lang(nl) %{_mandir}/nl/man5/*
%lang(pl) %{_mandir}/pl/man5/*
%lang(pt) %{_mandir}/pt/man5/*
%lang(ro) %{_mandir}/ro/man5/*
%lang(sl) %{_mandir}/sl/man5/*

%files whatis
%defattr(644,root,root,755)
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.weekly/makewhatis
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.daily/makewhatis
%attr(755,root,root) %{_bindir}/apropos
%attr(755,root,root) %{_bindir}/whatis
%attr(755,root,root) %{_sbindir}/makewhatis
%config(noreplace,missingok) %verify(not md5 mtime size) /var/cache/man/whatis
%{_mandir}/man1/[aw]*
%{_mandir}/man8/*
%lang(bg) %{_mandir}/bg/man1/[aw]*
%lang(bg) %{_mandir}/bg/man8/*
%lang(cs) %{_mandir}/cs/man1/[aw]*
%lang(da) %{_mandir}/da/man1/[aw]*
%lang(de) %{_mandir}/de/man1/[aw]*
%lang(el) %{_mandir}/el/man1/[aw]*
%lang(el) %{_mandir}/el/man8/*
%lang(es) %{_mandir}/es/man1/[aw]*
%lang(fi) %{_mandir}/fi/man1/[aw]*
%lang(fr) %{_mandir}/fr/man1/[aw]*
%lang(fr) %{_mandir}/fr/man8/*
%lang(hr) %{_mandir}/hr/man1/[aw]*
%lang(hu) %{_mandir}/hu/man1/[aw]*
%lang(it) %{_mandir}/it/man1/[aw]*
%lang(it) %{_mandir}/it/man8/*
%lang(ja) %{_mandir}/ja/man1/[aw]*
%lang(ja) %{_mandir}/ja/man8/*
%lang(ko) %{_mandir}/ko/man1/[aw]*
%lang(nl) %{_mandir}/nl/man1/[aw]*
%lang(pl) %{_mandir}/pl/man1/[aw]*
%lang(pt) %{_mandir}/pt/man1/[aw]*
%lang(ro) %{_mandir}/ro/man1/[aw]*
%lang(ro) %{_mandir}/ro/man8/*
%lang(sl) %{_mandir}/sl/man1/[aw]*

%files -n man2html
%defattr(644,root,root,755)
%doc {man2html/README,man2html/TODO}
%attr(755,root,root) %{_bindir}/man2html
%{_mandir}/man1/man2html.1*
%lang(el) %{_mandir}/el/man1/man2html.1*
%lang(ja) %{_mandir}/ja/man1/man2html.1*
%lang(pl) %{_mandir}/pl/man1/man2html.1*
%lang(ro) %{_mandir}/ro/man1/man2html.1*

%files -n man2html-cgi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hman
%dir %{_cgibinmandir}
%attr(755,root,root) %{_cgibinmandir}/*
%{_cgiauxmandir}
%dir %attr(775,root,http) /var/cache/man2html
/var/cache/man2html/.glimpse_filters
%{_mandir}/man1/hman.1*
%lang(el) %{_mandir}/el/man1/hman.1*
%lang(ja) %{_mandir}/ja/man1/hman.1*
%dir %attr(750,root,http) %{_webappdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/httpd.conf
