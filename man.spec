Summary:	Manual page reader
Summary(de):	Manual-Page-Reader
Summary(fr):	Lecteur de pages de man.
Summary(pl):	Czytnik stron man
Summary(tr):	K�lavuz sayfas� okuyucusu
Name:		man
Version:	1.5h1
Release:	3
License:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/doctools/man/%{name}-%{version}.tar.gz
Source1:	makewhatis.crondaily
Source2:	makewhatis.cronweekly
Patch0:		man-manpaths.patch
Patch1:		man-PLD.patch
Patch2:		man-msgs.patch
Patch3:		man-man2html.patch
Patch4:		man-fhs.patch
Patch5:		man-makewhatis.patch
Patch6:		man-safer.patch
Patch7:		man-security.patch
Patch8:		man-locales.patch
Requires:	groff
Requires:	less
Requires:	/bin/awk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The man package includes three tools for finding information and/or
documentation about your Linux system: man, apropos and whatis. The
man system formats and displays on-line manual pages about commands or
functions on your system. Apropos searches the whatis database
(containing short descriptions of system commands) for a string.
Whatis searches its own database for a complete word.

%description -l de
Die man-Seiten-Suite, einschlie�lich Handbuch, Apropos und Whatis.
Diese Programme dienen zum Einsehen des Gro�teils der Dokumentation,
die auf einem Linux-System verf�gbar ist. Die Whatis- und
Apropos-Programme dienen dazu, Beschreibungen zu bestimmten Themen zu
finden.

%description -l fr
Ensemble des pages man. Contient man, apropos et whatis. Ces
programmes servent � lire la plupart de la documentation disponible
sur un syst�me Linux. Les programmes whatis et apropos servent �
trouver la documentation relative � un sujet pr�cis.

%description -l pl
Pakiet man zawiera man, apropos i whatis. Te programy s� u�ywane do
czytania wi�kszo�ci dokumentacji dost�pnej w systemie Linux. Programy
whatis i apropos mog� by� u�yte do znalezienia dokumentacji na tematy
powi�zane z poszukiwanym.

%description -l tr
K�lavuz sayfa tak�m�: man, apropos, whatis. Bu programlar Linux
sisteminde bulunan bir�ok belgenin okunmas�nda kullanylyr. whatis ve
apropos programlar� �zel bir konu ile alakal� belgeleri bulmak i�in
kullan�labilir.

%package -n man2html
Summary:	manroff to html converter
Summary(pl):	Konwerter formatu manroff na html
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Requires:	%{name} = %{version}

%description -n man2html
This program can convert man pages stored in manroff format to html

%description -l pl -n man2html
Program man2html s�u�y do konwersji plik�w manuala zapisanych w
formacie manroff na format html.

%package -n man2html-cgi
Summary:	CGI interface to man2html
Summary(pl):	Interfejs CGI dla man2html
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Requires:	man2html = %{version}

%description -n man2html-cgi
These scripts allows read man pages throught www browser. It uses
man2htlm program to convert man pages to html format. Scripts are
still in alpha stage, could be not secure.

%description -l pl -n man2html-cgi
Skrypty znajduj�ce si� w pakiecie pozwalaj� czyta� strony man przy
pomocy przegl�darki WWW. Skrtpty wykorzystuj� program man2html do
konwesji stron man na html. Programy s� ci�gle w stadium alfa i mog�
nie by� bezpieczne.

%prep
%setup  -q
%patch0 -p1 
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
./configure -default +fhs +lang all

%{__make} CC="gcc $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/cron.{daily,weekly},%{_bindir},%{_mandir},%{_sbindir}}

%{__make} install BINROOTDIR="$RPM_BUILD_ROOT"

(cd man2html
%{__make} install-scripts BINROOTDIR="$RPM_BUILD_ROOT"
)

install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.weekly

install -d $RPM_BUILD_ROOT/var/cache/man/{local,X11R6}
install -d $RPM_BUILD_ROOT/var/cache/man/cat{1,2,3,4,5,6,7,8,9,n}
install -d $RPM_BUILD_ROOT/var/cache/man/local/cat{1,2,3,4,5,6,7,8,9,n}
install -d $RPM_BUILD_ROOT/var/cache/man/X11R6/cat{1,2,3,4,5,6,7,8,9,n}

for i in cs da de es fi fr it nl pl pt sl
do
	install -d $RPM_BUILD_ROOT/var/cache/man/$i/cat{1,2,3,4,5,6,7,8,9,n}
	install -d $RPM_BUILD_ROOT/var/cache/man/local/$i/cat{1,2,3,4,5,6,7,8,9,n}
	install -d $RPM_BUILD_ROOT/var/cache/man/X11R6/$i/cat{1,2,3,4,5,6,7,8,9,n}
done

install %{SOURCE2} $RPM_BUILD_ROOT/etc/cron.daily/makewhatis.cron
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.weekly/makewhatis.cron

strip $RPM_BUILD_ROOT%{_bindir}/man

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	$RPM_BUILD_ROOT%{_mandir}/*/man*/* \
	man2html/README man2html/TODO	

%preun
rm -f /var/cache/man/cat[123456789n]/*
rm -f /var/cache/man/local/cat[123456789n]/*
rm -f /var/cache/man/X11R6/cat[123456789n]/*
rm -f /var/cache/man/??/cat[123456789n]/*
rm -f /var/cache/man/local/??/cat[123456789n]/*
rm -f /var/cache/man/X11R6/??/cat[123456789n]/*

%post
rm -f /var/cache/man/cat[123456789n]/*
rm -f /var/cache/man/local/cat[123456789n]/*
rm -f /var/cache/man/X11/cat[123456789n]/*
rm -f /var/cache/man/??/cat[123456789n]/*
rm -f /var/cache/man/local/??/cat[123456789n]/*
rm -f /var/cache/man/X11R6/??/cat[123456789n]/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(750,root,root) %config /etc/cron.weekly/makewhatis.cron
%attr(750,root,root) %config /etc/cron.daily/makewhatis.cron

%attr(2755,root,man) %{_bindir}/man

%attr(755,root,root) %{_bindir}/apropos
%attr(755,root,root) %{_bindir}/whatis
%attr(755,root,root) %{_sbindir}/makewhatis
%config %verify(not size mtime md5) %{_sysconfdir}/man.config

# Supported languages cs da de en es fi fr it nl pl pt sl

%lang(cs) %{_mandir}/cs/man[15]/*
%lang(da) %{_mandir}/da/man[15]/*
%lang(de) %{_mandir}/de/man[15]/*
%lang(es) %{_mandir}/es/man[15]/*
%lang(fi) %{_mandir}/fi/man[15]/*
%lang(fr) %{_mandir}/fr/man[15]/*
%lang(it) %{_mandir}/it/man[15]/*
%lang(nl) %{_mandir}/nl/man[15]/*
%lang(pl) %{_mandir}/pl/man[15]/*
%lang(pt) %{_mandir}/pt/man[15]/*
%lang(sl) %{_mandir}/sl/man[15]/*

%attr(755,root,root) %dir /var/cache/man
%attr(775,root, man) /var/cache/man/cat*
%attr(775,root, man) /var/cache/man/local/cat*
%attr(775,root, man) /var/cache/man/X11R6/cat*

%lang(cs) %attr(775,root, man) /var/cache/man/cs/cat[1-9n]
%lang(cs) %attr(775,root, man) /var/cache/man/local/cs/cat[1-9n]
%lang(cs) %attr(775,root, man) /var/cache/man/X11R6/cs/cat[1-9n]
%lang(da) %attr(775,root, man) /var/cache/man/da/cat[1-9n]
%lang(da) %attr(775,root, man) /var/cache/man/local/da/cat[1-9n]
%lang(da) %attr(775,root, man) /var/cache/man/X11R6/da/cat[1-9n]
%lang(de) %attr(775,root, man) /var/cache/man/de/cat[1-9n]
%lang(de) %attr(775,root, man) /var/cache/man/local/de/cat[1-9n]
%lang(de) %attr(775,root, man) /var/cache/man/X11R6/de/cat[1-9n]
%lang(es) %attr(775,root, man) /var/cache/man/es/cat[1-9n]
%lang(es) %attr(775,root, man) /var/cache/man/local/es/cat[1-9n]
%lang(es) %attr(775,root, man) /var/cache/man/X11R6/es/cat[1-9n]
%lang(fi) %attr(775,root, man) /var/cache/man/fi/cat[1-9n]
%lang(fi) %attr(775,root, man) /var/cache/man/local/fi/cat[1-9n]
%lang(fi) %attr(775,root, man) /var/cache/man/X11R6/fi/cat[1-9n]
%lang(fr) %attr(775,root, man) /var/cache/man/fr/cat[1-9n]
%lang(fr) %attr(775,root, man) /var/cache/man/local/fr/cat[1-9n]
%lang(fr) %attr(775,root, man) /var/cache/man/X11R6/fr/cat[1-9n]
%lang(it) %attr(775,root, man) /var/cache/man/it/cat[1-9n]
%lang(it) %attr(775,root, man) /var/cache/man/local/it/cat[1-9n]
%lang(it) %attr(775,root, man) /var/cache/man/X11R6/it/cat[1-9n]
%lang(nl) %attr(775,root, man) /var/cache/man/nl/cat[1-9n]
%lang(nl) %attr(775,root, man) /var/cache/man/local/nl/cat[1-9n]
%lang(nl) %attr(775,root, man) /var/cache/man/X11R6/nl/cat[1-9n]
%lang(pl) %attr(775,root, man) /var/cache/man/pl/cat[1-9n]
%lang(pl) %attr(775,root, man) /var/cache/man/local/pl/cat[1-9n]
%lang(pl) %attr(775,root, man) /var/cache/man/X11R6/pl/cat[1-9n]
%lang(pt) %attr(775,root, man) /var/cache/man/pt/cat[1-9n]
%lang(pt) %attr(775,root, man) /var/cache/man/local/pt/cat[1-9n]
%lang(pt) %attr(775,root, man) /var/cache/man/X11R6/pt/cat[1-9n]
%lang(sl) %attr(775,root, man) /var/cache/man/sl/cat[1-9n]
%lang(sl) %attr(775,root, man) /var/cache/man/local/sl/cat[1-9n]
%lang(sl) %attr(775,root, man) /var/cache/man/X11R6/sl/cat[1-9n]

%lang(cs) %{_datadir}/locale/cs/man
%lang(da) %{_datadir}/locale/da/man
%lang(de) %{_datadir}/locale/de/man
%lang(en) %{_datadir}/locale/en/man
%lang(es) %{_datadir}/locale/es/man
%lang(fi) %{_datadir}/locale/fi/man
%lang(fr) %{_datadir}/locale/fr/man
%lang(it) %{_datadir}/locale/it/man
%lang(nl) %{_datadir}/locale/nl/man
%lang(pl) %{_datadir}/locale/pl/man
%lang(pt) %{_datadir}/locale/pt/man
%lang(sl) %{_datadir}/locale/sl/man

%{_mandir}/man[15]/*

%files -n man2html
%defattr(644,root,root,755)
%doc {man2html/README,man2html/TODO}.gz

%attr(755,root,root) %{_bindir}/man2html

%files -n man2html-cgi
%defattr(644,root,root,755)
/home/httpd/cgi-aux/man/*

%dir /home/httpd/cgi-bin/man
%attr(755,root,root) /home/httpd/cgi-bin/man/*

%dir %attr(755,nobody,nobody) /var/man2html
/var/man2html/.glimpse_filters

%attr(755,root,root) %{_bindir}/hman
