# TODO:
# - move http/cgi files to /usr/....
#
Summary:	Manual page reader
Summary(de):	Manual-Page-Reader
Summary(es):	Lector de páginas de manual (man)
Summary(fr):	Lecteur de pages de man
Summary(ko):	¹®¼­ °ü·Ã µµ±¸ ¸ðÀ½ : ¸Ç, apropos ±×¸®°í whatis
Summary(pl):	Czytnik stron man
Summary(pt_BR):	Leitor de páginas de manuais (man)
Summary(tr):	Kýlavuz sayfasý okuyucusu
Summary(ru):	îÁÂÏÒ ÕÔÉÌÉÔ ÄÌÑ ÄÏËÕÍÅÎÔÁÃÉÉ: man, apropos É whatis
Summary(uk):	îÁÂ¦Ò ÕÔÉÌ¦Ô ÄÌÑ ÄÏËÕÍÅÎÔÁÃ¦§: man, apropos ÔÁ whatis
Name:		man
Version:	1.5p
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.win.tue.nl/pub/linux-local/utils/man/%{name}-%{version}.tar.gz
# Source0-md5:	037d5644f8ef9ea0ef22b271bae0297d
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
BuildRequires:	less
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

%define		_servdir	/home/services
%define		_httpdir	%{_servdir}/httpd
%define		_cgidir		%{_httpdir}/cgi-bin

%description
The man package includes three tools for finding information and/or
documentation about your Linux system: man, apropos and whatis. The
man system formats and displays on-line manual pages about commands or
functions on your system. Apropos searches the whatis database
(containing short descriptions of system commands) for a string.
Whatis searches its own database for a complete word.

%description -l de
Die man-Seiten-Suite, einschließlich Handbuch, Apropos und Whatis.
Diese Programme dienen zum Einsehen des Großteils der Dokumentation,
die auf einem Linux-System verfügbar ist. Die Whatis- und
Apropos-Programme dienen dazu, Beschreibungen zu bestimmten Themen zu
finden.

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
Requires:	man2html = %{version}-%{release}

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

# use gzip (not bzip2) to compress formatted man pages
sed -i -e 's/compress=$/compress=gzip/' configure

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
install -d $RPM_BUILD_ROOT{/etc/cron.{daily,weekly},%{_bindir},%{_mandir},%{_sbindir},%{_servdir}} \
	$RPM_BUILD_ROOT%{_mandir}/{hu,ja,ko}/man{1,5,8}

echo '%defattr(644,root,root,755)' > man.lang
for i in "" bg cs da de el es fi fr hr hu id it ja ko nl pl pt pt_BR ro ru \
	 sk sl sr sv uk zh_CN zh_TW; do
	if [ "$i" ]; then
		lng="%lang($i) "
		i="/$i"
	else
		lng=""
	fi
	for cdir in "" /local /X11R6 ; do
		install -d $RPM_BUILD_ROOT/var/cache/man${cdir}$i/cat{1,2,3,4,5,6,7,8,9,n}
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

install %{SOURCE2} $RPM_BUILD_ROOT/etc/cron.daily/makewhatis
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.weekly/makewhatis

touch $RPM_BUILD_ROOT/var/cache/man/whatis

install man/el/hman.man $RPM_BUILD_ROOT%{_mandir}/el/man1/hman.1
install man/el/man2html.man $RPM_BUILD_ROOT%{_mandir}/el/man1/man2html.1
install man/hu/man1/* $RPM_BUILD_ROOT%{_mandir}/hu/man1
install man/ja/man1/{hman,man2html}.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1
install man/ja/man8/makewhatis.8 $RPM_BUILD_ROOT%{_mandir}/ja/man8
install man/pl/man1/man2html.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1
install man/ro/man2html.man $RPM_BUILD_ROOT%{_mandir}/ro/man1/man2html.1

# Play with /home/services
mv $RPM_BUILD_ROOT/home/httpd $RPM_BUILD_ROOT%{_servdir}

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

%files -f man.lang
%defattr(644,root,root,755)
%doc HISTORY README TODO
%attr(750,root,root) %config(noreplace) %verify(not size mtime md5) /etc/cron.weekly/makewhatis
%attr(750,root,root) %config(noreplace) %verify(not size mtime md5) /etc/cron.daily/makewhatis

%attr(2755,root,man) %{_bindir}/man

%attr(755,root,root) %{_bindir}/man2dvi
%attr(755,root,root) %{_bindir}/apropos
%attr(755,root,root) %{_bindir}/whatis
%attr(755,root,root) %{_bindir}/zsoelim
%attr(755,root,root) %{_sbindir}/makewhatis

%config(noreplace,missingok) %verify(not md5 mtime size) /var/cache/man/whatis

# Supported languages bg cs da de en es fi fr hr it ja nl pl pt ro sl  + hu

%{_mandir}/man1/apropos.1*
%{_mandir}/man1/man.1*
%{_mandir}/man1/whatis.1*
%{_mandir}/man[58]/*

%lang(bg) %{_mandir}/bg/man[15]/*
%lang(cs) %{_mandir}/cs/man[158]/*
%lang(da) %{_mandir}/da/man[158]/*
%lang(de) %{_mandir}/de/man[158]/*
%lang(el) %{_mandir}/el/man1/apropos.1*
%lang(el) %{_mandir}/el/man1/man.1*
%lang(el) %{_mandir}/el/man1/whatis.1*
%lang(el) %{_mandir}/el/man[58]/*
%lang(es) %{_mandir}/es/man[158]/*
%lang(fi) %{_mandir}/fi/man[158]/*
%lang(fr) %{_mandir}/fr/man[158]/*
%lang(hr) %{_mandir}/hr/man[158]/*
%lang(hu) %{_mandir}/hu/man[158]/*
%lang(it) %{_mandir}/it/man[158]/*
%lang(ja) %{_mandir}/ja/man1/apropos.1*
%lang(ja) %{_mandir}/ja/man1/man.1*
%lang(ja) %{_mandir}/ja/man1/whatis.1*
%lang(ja) %{_mandir}/ja/man[58]/*
%lang(ko) %{_mandir}/ko/man[158]/*
%lang(nl) %{_mandir}/nl/man[158]/*
%lang(pl) %{_mandir}/pl/man1/apropos.1*
%lang(pl) %{_mandir}/pl/man1/man.1*
%lang(pl) %{_mandir}/pl/man1/whatis.1*
%lang(pl) %{_mandir}/pl/man[58]/*
%lang(pt) %{_mandir}/pt/man[158]/*
%lang(ro) %{_mandir}/ro/man1/apropos.1*
%lang(ro) %{_mandir}/ro/man1/man.1*
%lang(ro) %{_mandir}/ro/man1/whatis.1*
%lang(ro) %{_mandir}/ro/man[58]/*
%lang(sl) %{_mandir}/sl/man[158]/*

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
%attr(755,root,root) %{_cgidir}/man
%{_httpdir}/cgi-aux/man
%dir %attr(775,root,http) /var/cache/man2html
/var/cache/man2html/.glimpse_filters
%{_mandir}/man1/hman.1*
%lang(el) %{_mandir}/el/man1/hman.1*
%lang(ja) %{_mandir}/ja/man1/hman.1*
# it seems to be the only package using this dir
%dir %{_httpdir}/cgi-aux
