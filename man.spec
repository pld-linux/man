Summary:	Manual page reader
Summary(de):	Manual-Page-Reader
Summary(es):	Lector de páginas de manual (man)
Summary(fr):	Lecteur de pages de man
Summary(ko):	¹®¼­ °ü·Ã µµ±¸ ¸ðÀ½ : ¸Ç, apropos ±×¸®°í whatis
Summary(pl):	Czytnik stron man
Summary(pt_BR):	Leitor de páginas de manuais (man)
Summary(ru):	îÁÂÏÒ ÕÔÉÌÉÔ ÄÌÑ ÄÏËÕÍÅÎÔÁÃÉÉ: man, apropos É whatis
Summary(tr):	Kýlavuz sayfasý okuyucusu
Summary(uk):	îÁÂ¦Ò ÕÔÉÌ¦Ô ÄÌÑ ÄÏËÕÍÅÎÔÁÃ¦§: man, apropos ÔÁ whatis
Name:		man
Version:	1.6c
Release:	4
License:	GPL
Group:		Applications/System
Source0:	http://primates.ximian.com/~flucifredi/man/%{name}-%{version}.tar.gz
# Source0-md5:	ac1e7d60dfedb7d1c6f398ae5b038996
Source1:	makewhatis.crondaily
Source2:	makewhatis.cronweekly
Source3:	%{name}-additional-%{name}-pages.tar.bz2
# Source3-md5:	16c3fde2243289524cf40c1d2e7150e4
Patch0:		%{name}-manpaths.patch
Patch1:		%{name}-PLD.patch
Patch2:		%{name}-fhs.patch
Patch3:		%{name}-makewhatis.patch
Patch4:		%{name}-safer.patch
Patch5:		%{name}-security.patch
Patch6:		%{name}-roff.patch
Patch7:		%{name}-sofix.patch
Patch8:		%{name}-ro-usr.patch
Patch9:		%{name}-bug11621.patch
Patch10:	%{name}-gencat.patch
Patch11:	%{name}-nls-priority.patch
Patch12:	%{name}-pmake.patch
Patch13:	%{name}-fmntbug.patch
Patch14:	%{name}-awk_path.patch
Patch15:	%{name}-cgi_paths.patch
Patch16:	%{name}-relat.patch
URL:		http://primates.ximian.com/~flucifredi/man/
BuildRequires:	less
BuildRequires:	rpmbuild(macros) >= 1.276
BuildRequires:	sed >= 4.0
Requires(post,preun):	fileutils
Requires:	%{name}-config = %{version}-%{release}
Requires:	/bin/awk
Requires:	groff
Requires:	gzip
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

%description -l de
Die man-Seiten-Suite, einschließlich Handbuch, Apropos und Whatis.
Diese Programme dienen zum Einsehen des Großteils der Dokumentation,
die auf einem Linux-System verfügbar ist. Die Whatis- und
Apropos-Programme dienen dazu, Beschreibungen zu bestimmten Themen zu
finden.

whatis und apropos sind im Paket man-whatis.

%description -l es
Es un conjunto de páginas de manual, incluyendo man, apropos y whatis.
Estos programas se usan para leer la mayoría de la documentación
disponible en el sistema Linux. Los programas whatis y apropos pueden
ser usados para encontrar documentación relacionada con un asunto
particular.

%description -l fr
Ensemble des pages man. Contient man, apropos et whatis. Ces
programmes servent à lire la plupart de la documentation disponible
sur un système Linux. Les programmes whatis et apropos servent à
trouver la documentation relative à un sujet précis.

%description -l pl
Pakiet man zawiera man, apropos i whatis. Te programy s± u¿ywane do
czytania wiêkszo¶ci dokumentacji dostêpnej w systemie Linux. Programy
whatis i apropos mog± byæ u¿yte do znalezienia dokumentacji na tematy
powi±zane z poszukiwanym.

Narzêdzia whatis i apropos s± w oddzielnym pakiecie - man-whatis.

%description -l pt_BR
É um conjunto de páginas de manual, incluindo man, apropos e whatis.
Estes programas são usados para ler a maioria da documentação
disponível no sistema Linux. Os programas whatis e apropos podem ser
usados para achar documentação relacionada com um assunto particular.

%description -l tr
Kýlavuz sayfa takýmý: man, apropos, whatis. Bu programlar Linux
sisteminde bulunan birçok belgenin okunmasýnda kullanylyr. whatis ve
apropos programlarý özel bir konu ile alakalý belgeleri bulmak için
kullanýlabilir.

%description -l ru
ðÁËÅÔ man ÓÏÄÅÒÖÉÔ ÔÒÉ ÕÔÉÌÉÔÙ ÄÌÑ ÐÏÉÓËÁ ÉÎÆÏÒÍÁÃÉÉ É/ÉÌÉ
ÄÏËÕÍÅÎÔÁÃÉÉ Ï ×ÁÛÅÊ ÓÉÓÔÅÍÅ: man, apropos É whatis. óÉÓÔÅÍÁ man
ÆÏÒÍÁÔÉÒÕÅÔ É ÐÏËÁÚÙ×ÁÅÔ ÏÎÌÁÊÎÏ×ÙÅ ÓÔÒÁÎÉÃÙ ÍÁÎÕÁÌÁ Ï ËÏÍÁÎÄÁÈ É
ÆÕÎËÃÉÑÈ ×ÁÛÅÊ ÓÉÓÔÅÍÙ. Apropos ÉÝÅÔ ÚÁÄÁÎÎÕÀ ÓÔÒÏËÕ × ÂÁÚÅ ÄÁÎÎÙÈ
whatis (ÓÏÄÅÒÖÁÝÅÊ ËÏÒÏÔËÉÅ ÏÐÉÓÁÎÉÑ ÓÉÓÔÅÍÎÙÈ ËÏÍÁÎÄ). Whatis ÉÝÅÔ ×
Ó×ÏÅÊ ÂÁÚÅ ÄÁÎÎÙÈ ÚÁ×ÅÒÛÅÎÎÙÅ ÓÌÏ×Á.

%description -l uk
ðÁËÅÔ man Í¦ÓÔÉÔØ ÔÒÉ ÕÔÉÌ¦ÔÉ ÄÌÑ ÐÏÛÕËÕ ¦ÎÆÏÒÍÁÃ¦§ ÔÁ/ÁÂÏ
ÄÏËÕÍÅÎÔÁÃ¦§ ÐÒÏ ×ÁÛÕ ÓÉÓÔÅÍÕ: man, apropos ÔÁ whatis. óÉÓÔÅÍÁ man
ÆÏÒÍÁÔÕ¤ ÔÁ ÐÏËÁÚÕ¤ ÏÎÌÁÊÎÏ×¦ ÓÔÏÒ¦ÎËÉ ÍÁÎÕÁÌÕ ÐÒÏ ËÏÍÁÎÄÉ ÔÁ ÆÕÎËÃ¦§
×ÁÛÏ§ ÓÉÓÔÅÍÉ. Apropos ÛÕËÁ¤ ÚÁÄÁÎÉÊ ÒÑÄÏË Õ ÂÁÚ¦ ÄÁÎÉÈ whatis (ÑËÁ
Í¦ÓÔÉÔØ ËÏÒÏÔË¦ ÏÐÉÓÉ ÓÉÓÔÅÍÎÉÈ ËÏÍÁÎÄ). Whatis ÛÕËÁ¤ Õ Ó×Ï§Ê ÂÁÚ¦
ÚÁË¦ÎÞÅÎ¦ ÓÌÏ×Á.

%package config
Summary:	Manual page reader configuration
Summary(pl):	Konfiguracja czytników podrêczników
Group:		Applications/System

%description config
Configuration file for different manual page browsers.

%description config -l pl
Plik konfiguracyjny dla ró¿nych czytników podrêczników.

%package whatis
Summary:	whatis utilities
Summary(pl):	Narzêdzia whatis
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	crondaemon

%description whatis
This package provides the following utilities: apropos, whatis and
makewhatis.

%description whatis -l pl
Ten pakiet dostracza nastêpuj±ce narzêdzia: apropos, whatis i
makewhatis.

%package -n man2html
Summary:	manroff to html converter
Summary(pl):	Konwerter formatu manroff na html
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n man2html
This program can convert man pages stored in manroff format to html.

%description -n man2html -l pl
Program man2html s³u¿y do konwersji plików manuala zapisanych w
formacie manroff na format html.

%package -n man2html-cgi
Summary:	CGI interface to man2html
Summary(pl):	Interfejs CGI dla man2html
Group:		Applications/System
Requires:	%{name}-whatis = %{version}-%{release}
Requires:	FHS >= 2.3-12
Requires:	man2html = %{version}-%{release}
Requires:	webapps
Conflicts:	apache-base < 2.2.0-7.2
Conflicts:	apache1 < 1.3.34-5.11

%description -n man2html-cgi
These scripts allows read man pages throught WWW browser. It uses
man2htlm program to convert man pages to html format. Scripts are
still in alpha stage, could be not secure.

%description -n man2html-cgi -l pl
Skrypty znajduj±ce siê w pakiecie pozwalaj± czytaæ strony man przy
pomocy przegl±darki WWW. Skrtpty wykorzystuj± program man2html do
konwersji stron man na html. Programy s± ci±gle w stadium alfa i mog±
nie byæ bezpieczne.

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

# use gzip (not bzip2) to compress formatted man pages
sed -i -e 's/compress=$/compress=gzip/' configure

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

%{__make} \
	CC="%{__cc} %{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/cron.{daily,weekly},%{_bindir},%{_mandir},%{_sbindir},%{_cgibinmandir},%{_cgiauxmandir}} \
	$RPM_BUILD_ROOT{%{_mandir}/{hu,ja,ko}/man{1,5,8},%{_webappdir},/etc/tmpwatch}

echo "# Cleanup man temporary files:" > $RPM_BUILD_ROOT/etc/tmpwatch/man.conf
echo '%defattr(644,root,root,755)' > man.lang
for i in "" bg cs da de el es fi fr gl hr hu id it ja ko nl pl pt pt_BR ro ru \
	 sk sl sr sv tr uk zh_CN zh_TW; do
	if [ "$i" ]; then
		lng="%lang($i) "
		i="/$i"
	else
		lng=""
	fi
	for cdir in "" /local /X11R6 ; do
		install -d $RPM_BUILD_ROOT/var/cache/man${cdir}$i/cat{1,2,3,4,5,6,7,8,9,n}
		echo "/var/cache/man${cdir}$i 240" >> $RPM_BUILD_ROOT/etc/tmpwatch/man.conf
		echo "${lng}%dir /var/cache/man${cdir}$i" >> man.lang
		echo "${lng}%attr(775,root, man) /var/cache/man${cdir}$i/cat[1-9n]" >> man.lang
	done
done

%{__make} install \
	PREFIX="$RPM_BUILD_ROOT"

%{__make} -C man2html install-scripts \
	PREFIX="$RPM_BUILD_ROOT"

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

%preun
rm -f /var/cache/man/cat[123456789n]/*
rm -f /var/cache/man/local/cat[123456789n]/*
rm -f /var/cache/man/X11R6/cat[123456789n]/*
rm -f /var/cache/man/??/cat[123456789n]/*
rm -f /var/cache/man/??_??/cat[123456789n]/*
rm -f /var/cache/man/local/??/cat[123456789n]/*
rm -f /var/cache/man/local/??_??/cat[123456789n]/*
rm -f /var/cache/man/X11R6/??/cat[123456789n]/*
rm -f /var/cache/man/X11R6/??_??/cat[123456789n]/*

%post
rm -f /var/cache/man/cat[123456789n]/*
rm -f /var/cache/man/local/cat[123456789n]/*
rm -f /var/cache/man/X11/cat[123456789n]/*
rm -f /var/cache/man/??/cat[123456789n]/*
rm -f /var/cache/man/??_??/cat[123456789n]/*
rm -f /var/cache/man/local/??/cat[123456789n]/*
rm -f /var/cache/man/local/??_??/cat[123456789n]/*
rm -f /var/cache/man/X11R6/??/cat[123456789n]/*
rm -f /var/cache/man/X11R6/??_??/cat[123456789n]/*

%triggerin -n man2html-cgi -- apache1
%webapp_register apache %{_webapp}

%triggerun -n man2html-cgi -- apache1
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
	if [ -f /var/lock/subsys/apache ]; then
		/etc/rc.d/init.d/apache reload 1>&2
	fi
fi
if [ -L /etc/httpd/httpd.conf/09_man.conf ]; then
	rm -f /etc/httpd/httpd.conf/09_man.conf
	/usr/sbin/webapp register httpd %{_webapp}
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd reload 1>&2
	fi
fi
exit 0

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
