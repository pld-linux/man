Summary:	Manual page reader
Summary(de):	Manual-Page-Reader
Summary(fr):	Lecteur de pages de man.
Summary(pl):	Czytnik stron man
Summary(tr):	Kýlavuz sayfasý okuyucusu
Name:		man
Version:	1.5g
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/doctools/%{name}-%{version}.tar.gz
Source1:	makewhatis.cron
Patch0:		man-manpath.patch
Patch1:		man-PLD.patch
Patch2:		man-msgs.patch
Patch3:		man-man2html.patch
Requires:	groff
Buildroot:	/tmp/%{name}-%{version}-root

%description
The man page suite, including man, apropos, and whatis.  These programs are
used to read most of the documentation available on a Linux system.  The
whatis and apropos programs can be used to find documentation related to a
particular subject.

%description -l pl
Pakiet man zawiera man, apropos i whatis. Te programy s± u¿ywane do
czytania wiêkszo¶ci dokumentacji dostêpnej w systemie Linux. Programy whatis
i apropos mog± byæ u¿yte do znalezienia dokumentacji na tematy powi±zane z
poszukiwanym.

%description -l de
Die man-Seiten-Suite, einschließlich Handbuch, Apropos und Whatis.  Diese
Programme dienen zum Einsehen des Großteils der Dokumentation, die auf einem
Linux-System verfügbar ist. Die Whatis- und Apropos-Programme dienen dazu,
Beschreibungen zu bestimmten Themen zu finden.

%description -l fr
Ensemble des pages man. Contient man, apropos et whatis. Ces programmes
servent à lire la plupart de la documentation disponible sur un système
Linux. Les programmes whatis et apropos servent à trouver la documentation
relative à un sujet précis.

%description -l tr
Kýlavuz sayfa takýmý: man, apropos, whatis. Bu programlar Linux sisteminde
bulunan birçok belgenin okunmasýnda kullanylyr. whatis ve apropos
programlarý özel bir konu ile alakalý belgeleri bulmak için kullanýlabilir.

%package -n man2html
Summary:	manroff to html converter
Summary(pl):	Konwerter formatu manroff na html
Group:		Utilities/System
Group(pl):	Narzêdzia/System

%description -n man2html
This program can convert man pages stored in manroff format to html

%description -l pl -n man2html
Program man2html s³u¿y do konwersji plików manuala zapisanych w formacie
manroff na format html.

%package -n man2html-cgi
Summary:	CGI interface to man2html
Summary(pl):	Interfejs CGI dla man2html
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Requires:	man2html

%description -n man2html-cgi
These scripts allows read man pages throught www browser. It uses
man2htlm program to convert man pages to html format.
Scripts are still in alpha stage, could be not secure.

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

%build
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
./configure -default +fsstnd +lang all

make CC="gcc $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/cron.weekly,usr/{bin,man,sbin}}

make install BINROOTDIR="$RPM_BUILD_ROOT"

(cd man2html
make install-scripts BINROOTDIR="$RPM_BUILD_ROOT"
)

install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.weekly

install -d $RPM_BUILD_ROOT/var/catman/{local,X11R6}
install -d $RPM_BUILD_ROOT/var/catman/cat{1,2,3,4,5,6,7,8,9,n}
install -d $RPM_BUILD_ROOT/var/catman/local/cat{1,2,3,4,5,6,7,8,9,n}
install -d $RPM_BUILD_ROOT/var/catman/X11R6/cat{1,2,3,4,5,6,7,8,9,n}
for i in cs da de es fi fr it nl pl pt sl
do
  install -d $RPM_BUILD_ROOT/var/catman/$i/cat{1,2,3,4,5,6,7,8,9,n}
  install -d $RPM_BUILD_ROOT/var/catman/local/$i/cat{1,2,3,4,5,6,7,8,9,n}
  install -d $RPM_BUILD_ROOT/var/catman/X11R6/$i/cat{1,2,3,4,5,6,7,8,9,n}
done

strip $RPM_BUILD_ROOT/usr/bin/man

#for LNG in $RPM_BUILD_ROOT/usr/lib/locale/man/*; do
#  install -d $RPM_BUILD_ROOT/usr/share/locale/`basename $LNG`
#  cp $LNG $RPM_BUILD_ROOT/usr/share/locale/`basename $LNG`/man
#done

gzip -9fn $RPM_BUILD_ROOT/usr/man/man*/* \
	$RPM_BUILD_ROOT/usr/man/*/man*/* \
	man2html/README man2html/TODO	

%preun
rm -f /var/catman/cat[123456789n]/*
rm -f /var/catman/local/cat[123456789n]/*
rm -f /var/catman/X11R6/cat[123456789n]/*
rm -f /var/catman/??/cat[123456789n]/*
rm -f /var/catman/local/??/cat[123456789n]/*
rm -f /var/catman/X11R6/??/cat[123456789n]/*

%post
rm -f /var/catman/cat[123456789n]/*
rm -f /var/catman/local/cat[123456789n]/*
rm -f /var/catman/X11/cat[123456789n]/*
rm -f /var/catman/??/cat[123456789n]/*
rm -f /var/catman/local/??/cat[123456789n]/*
rm -f /var/catman/X11R6/??/cat[123456789n]/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,man,755)
%attr(750,root,root) %config /etc/cron.weekly/makewhatis.cron

%attr(2711,root,man) /usr/bin/man

%attr(755,root,root) /usr/bin/apropos
%attr(755,root,root) /usr/bin/whatis
%attr(755,root,root) /usr/sbin/makewhatis
%attr(644,root,root) %config %verify(not size mtime md5) /etc/man.config

# Supported languages cs da de en es fi fr it nl pl pt sl

%lang(cs) /usr/man/cs/man[15]/*
%lang(da) /usr/man/da/man[15]/*
%lang(de) /usr/man/de/man[15]/*
%lang(es) /usr/man/es/man[15]/*
%lang(fi) /usr/man/fi/man[15]/*
%lang(fr) /usr/man/fr/man[15]/*
%lang(it) /usr/man/it/man[15]/*
%lang(nl) /usr/man/nl/man[15]/*
%lang(pl) /usr/man/pl/man[15]/*
%lang(pt) /usr/man/pt/man[15]/*
%lang(sl) /usr/man/sl/man[15]/*

%attr(775,root, man) %dir /var/catman
%attr(775,root, man) /var/catman/cat*
%attr(775,root, man) /var/catman/local/cat*
%attr(775,root, man) /var/catman/X11R6/cat*

%lang(cs) %attr(775,root, man) /var/catman/cs/cat[1-9n]
%lang(cs) %attr(775,root, man) /var/catman/local/cs/cat[1-9n]
%lang(cs) %attr(775,root, man) /var/catman/X11R6/cs/cat[1-9n]
%lang(da) %attr(775,root, man) /var/catman/da/cat[1-9n]
%lang(da) %attr(775,root, man) /var/catman/local/da/cat[1-9n]
%lang(da) %attr(775,root, man) /var/catman/X11R6/da/cat[1-9n]
%lang(de) %attr(775,root, man) /var/catman/de/cat[1-9n]
%lang(de) %attr(775,root, man) /var/catman/local/de/cat[1-9n]
%lang(de) %attr(775,root, man) /var/catman/X11R6/de/cat[1-9n]
%lang(es) %attr(775,root, man) /var/catman/es/cat[1-9n]
%lang(es) %attr(775,root, man) /var/catman/local/es/cat[1-9n]
%lang(es) %attr(775,root, man) /var/catman/X11R6/es/cat[1-9n]
%lang(fi) %attr(775,root, man) /var/catman/fi/cat[1-9n]
%lang(fi) %attr(775,root, man) /var/catman/local/fi/cat[1-9n]
%lang(fi) %attr(775,root, man) /var/catman/X11R6/fi/cat[1-9n]
%lang(fr) %attr(775,root, man) /var/catman/fr/cat[1-9n]
%lang(fr) %attr(775,root, man) /var/catman/local/fr/cat[1-9n]
%lang(fr) %attr(775,root, man) /var/catman/X11R6/fr/cat[1-9n]
%lang(it) %attr(775,root, man) /var/catman/it/cat[1-9n]
%lang(it) %attr(775,root, man) /var/catman/local/it/cat[1-9n]
%lang(it) %attr(775,root, man) /var/catman/X11R6/it/cat[1-9n]
%lang(nl) %attr(775,root, man) /var/catman/nl/cat[1-9n]
%lang(nl) %attr(775,root, man) /var/catman/local/nl/cat[1-9n]
%lang(nl) %attr(775,root, man) /var/catman/X11R6/nl/cat[1-9n]
%lang(pl) %attr(775,root, man) /var/catman/pl/cat[1-9n]
%lang(pl) %attr(775,root, man) /var/catman/local/pl/cat[1-9n]
%lang(pl) %attr(775,root, man) /var/catman/X11R6/pl/cat[1-9n]
%lang(pt) %attr(775,root, man) /var/catman/pt/cat[1-9n]
%lang(pt) %attr(775,root, man) /var/catman/local/pt/cat[1-9n]
%lang(pt) %attr(775,root, man) /var/catman/X11R6/pt/cat[1-9n]
%lang(sl) %attr(775,root, man) /var/catman/sl/cat[1-9n]
%lang(sl) %attr(775,root, man) /var/catman/local/sl/cat[1-9n]
%lang(sl) %attr(775,root, man) /var/catman/X11R6/sl/cat[1-9n]

%lang(cs) /usr/share/locale/cs/man
%lang(da) /usr/share/locale/da/man
%lang(de) /usr/share/locale/de/man
%lang(en) /usr/share/locale/en/man
%lang(es) /usr/share/locale/es/man
%lang(fi) /usr/share/locale/fi/man
%lang(fr) /usr/share/locale/fr/man
%lang(it) /usr/share/locale/it/man
%lang(nl) /usr/share/locale/nl/man
%lang(pl) /usr/share/locale/pl/man
%lang(pt) /usr/share/locale/pt/man
%lang(sl) /usr/share/locale/sl/man

/usr/man/man[15]/*

%files -n man2html
%defattr(644,root,root,755)
%doc {man2html/README,man2html/TODO}.gz

%attr(755,root,root) /usr/bin/man2html

%files -n man2html-cgi
%defattr(644,root,root,755)
/home/httpd/cgi-aux/man/*

%dir /home/httpd/cgi-bin/man
%attr(755,root,root) /home/httpd/cgi-bin/man/*

%dir %attr(755,nobody,nobody) /var/man2html
/var/man2html/.glimpse_filters

%attr(755,root,root) /usr/bin/hman

%changelog
* Wed Apr 28 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.5g-1]
- upgraded to 1.5g
- rewrited man-man2html.patch
- replacement in files
- gzipped man pages and docs

* Sun Dec 20 1998 Marek Obuchowicz <elephant@shadow.eu.org>
  [1.5f-2d]
- fixed permissions
- little spec modifications

* Thu Sep 17 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.5f-1d]
- updated to 1.5f
  (based on Konrad Stêpieñ <konrad@interdata.com.pl> spec file),
- fixed pl translation.
 
* Mon Sep 14 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.5d-5d]
- build against GNU libc-2.1,
- restricted files permissions,
- macro %%{name} in all Sources,
- macro %%config %%verify(not size mtime md5) for /etc/man.config.

* Sat Aug 26 1998 Konrad Stepien <konrad@interdata.com.pl>
  [1.5d-5]
- Reconfig to include international locales and man pages,
- Removed -D_GNU_SOURCE flag,
- Fix %install, to not install man2html
- "install -d" instead "mkdir -p" in %install,
- few simplification in %install,
- added pl translation,
- start at RH spec.
