Summary:	Manual page reader
Summary(de):	Manual-Page-Reader
Summary(fr):	Lecteur de pages de man
Summary(pl):	Czytnik stron man
Summary(tr):	Kýlavuz sayfasý okuyucusu
Name:		man
Version:	1.5h1
Release:	27
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
Requires:	gzip
Requires:	/bin/awk
Requires:	mktemp >= 1.5-8
Prereq:		fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l tr
Kýlavuz sayfa takýmý: man, apropos, whatis. Bu programlar Linux
sisteminde bulunan birçok belgenin okunmasýnda kullanylyr. whatis ve
apropos programlarý özel bir konu ile alakalý belgeleri bulmak için
kullanýlabilir.

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
Program man2html s³u¿y do konwersji plików manuala zapisanych w
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
Skrypty znajduj±ce siê w pakiecie pozwalaj± czytaæ strony man przy
pomocy przegl±darki WWW. Skrtpty wykorzystuj± program man2html do
konwesji stron man na html. Programy s± ci±gle w stadium alfa i mog±
nie byæ bezpieczne.

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
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" \
./configure -default +fhs +lang all

%{__make} CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/cron.{daily,weekly},%{_bindir},%{_mandir},%{_sbindir}}

echo '%defattr(644,root,root,755)' > man.lang
for i in "" bg cs da de es fi fr hu id it ja ko nl pl pt pt_BR ru sl sv zh_CN.GB2312 zh_TW.Big5; do
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

%clean
rm -rf $RPM_BUILD_ROOT

%files -f man.lang
%defattr(644,root,root,755)
%attr(750,root,root) %config(noreplace) %verify(not size mtime md5) /etc/cron.weekly/makewhatis.cron
%attr(750,root,root) %config(noreplace) %verify(not size mtime md5) /etc/cron.daily/makewhatis.cron

%attr(2755,root,man) %{_bindir}/man

%attr(755,root,root) %{_bindir}/apropos
%attr(755,root,root) %{_bindir}/whatis
%attr(755,root,root) %{_sbindir}/makewhatis
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/man.config

%config(noreplace,missingok) %verify(not md5 mtime size) /var/cache/man/whatis

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
