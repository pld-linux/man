Summary:	Manual page reader
Summary(de):	Manual-Page-Reader
Summary(fr):	Lecteur de pages de man
Summary(pl):	Czytnik stron man
Summary(tr):	K�lavuz sayfas� okuyucusu
Name:		man
Version:	1.5h1
Release:	23
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/doctools/man/%{name}-%{version}.tar.gz
Source1:	makewhatis.crondaily
Source2:	makewhatis.cronweekly
Patch0:		%{name}-manpaths.patch
Patch1:		%{name}-PLD.patch
Patch2:		%{name}-msgs.patch
Patch3:		%{name}-man2html.patch
Patch4:		%{name}-fhs.patch
Patch5:		%{name}-makewhatis.patch
Patch6:		%{name}-safer.patch
Patch7:		%{name}-security.patch
Patch8:		%{name}-locales.patch
Patch9:		%{name}-roff.patch
Patch10:	%{name}-sofix.patch
Patch11:	%{name}-sec.patch
Patch12:	%{name}-ro-usr.patch
Patch13:	%{name}-mansect.patch
Patch14:	%{name}-lookon.patch
Patch15:	%{name}-bug11621.patch
Patch16:	%{name}-gencat.patch
Requires:	groff
Requires:	less
Requires:	/bin/awk
Requires:	mktemp >= 1.5-8
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
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	%{name} = %{version}

%description -n man2html
This program can convert man pages stored in manroff format to html

%description -l pl -n man2html
Program man2html s�u�y do konwersji plik�w manuala zapisanych w
formacie manroff na format html.

%package -n man2html-cgi
Summary:	CGI interface to man2html
Summary(pl):	Interfejs CGI dla man2html
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
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
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g}}" LDFLAGS="%{!?debug:-s}"
./configure -default +fhs +lang all

%{__make} CC="%{__cc} %{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/cron.{daily,weekly},%{_bindir},%{_mandir},%{_sbindir}}
for i in "" cs da de es fi fr it nl pl pt sl; do
	install -d $RPM_BUILD_ROOT/var/cache/man/$i/cat{1,2,3,4,5,6,7,8,9,n}
	install -d $RPM_BUILD_ROOT/var/cache/man/local/$i/cat{1,2,3,4,5,6,7,8,9,n}
	install -d $RPM_BUILD_ROOT/var/cache/man/X11R6/$i/cat{1,2,3,4,5,6,7,8,9,n}
done

%{__make} install BINROOTDIR="$RPM_BUILD_ROOT"

(cd man2html
%{__make} install-scripts BINROOTDIR="$RPM_BUILD_ROOT"
)

install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.weekly

install %{SOURCE2} $RPM_BUILD_ROOT/etc/cron.daily/makewhatis.cron
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.weekly/makewhatis.cron

touch $RPM_BUILD_ROOT/var/cache/man/whatis

gzip -9nf man2html/README man2html/TODO	

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
%attr(750,root,root) %config(noreplace) %verify(not size mtime md5) /etc/cron.weekly/makewhatis.cron
%attr(750,root,root) %config(noreplace) %verify(not size mtime md5) /etc/cron.daily/makewhatis.cron

%attr(2755,root,man) %{_bindir}/man

%attr(755,root,root) %{_bindir}/apropos
%attr(755,root,root) %{_bindir}/whatis
%attr(755,root,root) %{_sbindir}/makewhatis
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/man.config

# Supported languages cs da de en es fi fr it nl pl pt sl

%{_mandir}/man[15]/*

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

%config(noreplace,missingok) %verify(not md5 mtime size) /var/cache/man/whatis

%dir /var/cache/man
%dir /var/cache/man/local
%dir /var/cache/man/X11R6
%attr(775,root, man) /var/cache/man/cat*
%attr(775,root, man) /var/cache/man/local/cat*
%attr(775,root, man) /var/cache/man/X11R6/cat*

%lang(cs) %dir /var/cache/man/cs
%lang(cs) %dir /var/cache/man/local/cs
%lang(cs) %dir /var/cache/man/X11R6/cs
%lang(cs) %attr(775,root, man) /var/cache/man/cs/cat[1-9n]
%lang(cs) %attr(775,root, man) /var/cache/man/local/cs/cat[1-9n]
%lang(cs) %attr(775,root, man) /var/cache/man/X11R6/cs/cat[1-9n]
%lang(da) %dir /var/cache/man/da
%lang(da) %dir /var/cache/man/local/da
%lang(da) %dir /var/cache/man/X11R6/da
%lang(da) %attr(775,root, man) /var/cache/man/da/cat[1-9n]
%lang(da) %attr(775,root, man) /var/cache/man/local/da/cat[1-9n]
%lang(da) %attr(775,root, man) /var/cache/man/X11R6/da/cat[1-9n]
%lang(de) %dir /var/cache/man/de
%lang(de) %dir /var/cache/man/local/de
%lang(de) %dir /var/cache/man/X11R6/de
%lang(de) %attr(775,root, man) /var/cache/man/de/cat[1-9n]
%lang(de) %attr(775,root, man) /var/cache/man/local/de/cat[1-9n]
%lang(de) %attr(775,root, man) /var/cache/man/X11R6/de/cat[1-9n]
%lang(es) %dir /var/cache/man/es
%lang(es) %dir /var/cache/man/local/es
%lang(es) %dir /var/cache/man/X11R6/es
%lang(es) %attr(775,root, man) /var/cache/man/es/cat[1-9n]
%lang(es) %attr(775,root, man) /var/cache/man/local/es/cat[1-9n]
%lang(es) %attr(775,root, man) /var/cache/man/X11R6/es/cat[1-9n]
%lang(fi) %dir /var/cache/man/fi
%lang(fi) %dir /var/cache/man/local/fi
%lang(fi) %dir /var/cache/man/X11R6/fi
%lang(fi) %attr(775,root, man) /var/cache/man/fi/cat[1-9n]
%lang(fi) %attr(775,root, man) /var/cache/man/local/fi/cat[1-9n]
%lang(fi) %attr(775,root, man) /var/cache/man/X11R6/fi/cat[1-9n]
%lang(fr) %dir /var/cache/man/fr
%lang(fr) %dir /var/cache/man/local/fr
%lang(fr) %dir /var/cache/man/X11R6/fr
%lang(fr) %attr(775,root, man) /var/cache/man/fr/cat[1-9n]
%lang(fr) %attr(775,root, man) /var/cache/man/local/fr/cat[1-9n]
%lang(fr) %attr(775,root, man) /var/cache/man/X11R6/fr/cat[1-9n]
%lang(it) %dir /var/cache/man/it
%lang(it) %dir /var/cache/man/local/it
%lang(it) %dir /var/cache/man/X11R6/it
%lang(it) %attr(775,root, man) /var/cache/man/it/cat[1-9n]
%lang(it) %attr(775,root, man) /var/cache/man/local/it/cat[1-9n]
%lang(it) %attr(775,root, man) /var/cache/man/X11R6/it/cat[1-9n]
%lang(nl) %dir /var/cache/man/nl
%lang(nl) %dir /var/cache/man/local/nl
%lang(nl) %dir /var/cache/man/X11R6/nl
%lang(nl) %attr(775,root, man) /var/cache/man/nl/cat[1-9n]
%lang(nl) %attr(775,root, man) /var/cache/man/local/nl/cat[1-9n]
%lang(nl) %attr(775,root, man) /var/cache/man/X11R6/nl/cat[1-9n]
%lang(pl) %dir /var/cache/man/pl
%lang(pl) %dir /var/cache/man/local/pl
%lang(pl) %dir /var/cache/man/X11R6/pl
%lang(pl) %attr(775,root, man) /var/cache/man/pl/cat[1-9n]
%lang(pl) %attr(775,root, man) /var/cache/man/local/pl/cat[1-9n]
%lang(pl) %attr(775,root, man) /var/cache/man/X11R6/pl/cat[1-9n]
%lang(pt) %dir /var/cache/man/pt
%lang(pt) %dir /var/cache/man/local/pt
%lang(pt) %dir /var/cache/man/X11R6/pt
%lang(pt) %attr(775,root, man) /var/cache/man/pt/cat[1-9n]
%lang(pt) %attr(775,root, man) /var/cache/man/local/pt/cat[1-9n]
%lang(pt) %attr(775,root, man) /var/cache/man/X11R6/pt/cat[1-9n]
%lang(sl) %dir /var/cache/man/sl
%lang(sl) %dir /var/cache/man/local/sl
%lang(sl) %dir /var/cache/man/X11R6/sl
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
