Summary:     manual page reader
Summary(de): Manual-Page-Reader
Summary(fr): Lecteur de pages de man.
Summary(pl): Czytnik stron man
Summary(tr): Kýlavuz sayfasý okuyucusu
Name:        man
Version:     1.5
Release:     5d
Copyright:   GPL
Group:       Utilities/System
Source0:     ftp://sunsite.unc.edu/pub/Linux/apps/doctools/%{name}-%{version}.tar.gz
Source1:     makewhatis.cron
Source2:     man-1.5d-PLD.patch
Patch0:      man-1.5a-manpath.patch
Patch1:      man-1.5a-sgid.patch
Patch2:      man-1.5d-properfree.patch
Requires:    groff
Buildroot:   /tmp/%{name}-%{version}-root

%description
The man page suite, including man, apropos, and whatis.  These programs are
used to read most of the documentation available on a Linux system.  The
whatis and apropos programs can be used to find documentation related to a
particular subject.

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

%description -l pl
Pakiet man, zawiera man, apropos i whatis. Te programy s± u¿ywane co
czytania wiêkszo¶ci dokumentacji dostêpnej w systemie Linux. Programy whatis
i apropos mog± byæ u¿yte do znalezienia dokumentacji na tematy powi±zane z
poszukiwanym.

%description -l tr
Kýlavuz sayfa takýmý: man, apropos, whatis. Bu programlar Linux sisteminde
bulunan birçok belgenin okunmasýnda kullanylyr. whatis ve apropos
programlarý özel bir konu ile alakalý belgeleri bulmak için kullanýlabilir.

%prep
%setup -q
%patch0 -p1 -b .manpath
%patch1 -p1 -b .sgid
%patch2 -p1 -b .freefix

%build
./configure -default +fsstnd +lang all
patch -p0 -s < $RPM_SOURCE_DIR/man-1.5d-PLD.patch
make CC="gcc $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/cron.weekly,usr/{bin,man,sbin}}

# XXX avoid man2html install
( cd src
  make install BINROOTDIR="$RPM_BUILD_ROOT"
  cd ../man
  make installsubdirs BINROOTDIR="$RPM_BUILD_ROOT"
  cd ../msgs
  make install BINROOTDIR="$RPM_BUILD_ROOT"
)

install $RPM_SOURCE_DIR/makewhatis.cron $RPM_BUILD_ROOT/etc/cron.weekly

install -d $RPM_BUILD_ROOT/var/catman/{local,X11R6}
install -d $RPM_BUILD_ROOT/var/catman/cat{1,2,3,4,5,6,7,8,9,n}
install -d $RPM_BUILD_ROOT/var/catman/local/cat{1,2,3,4,5,6,7,8,9,n}
install -d $RPM_BUILD_ROOT/var/catman/X11R6/cat{1,2,3,4,5,6,7,8,9,n}
for i in cs da de es fr it nl pl pt sl
do
#  install -d $RPM_BUILD_ROOT/var/catman/$i/cat{1,5}
  install -d $RPM_BUILD_ROOT/var/catman/$i/cat{1,2,3,4,5,6,7,8,9,n}
  install -d $RPM_BUILD_ROOT/var/catman/local/$i/cat{1,2,3,4,5,6,7,8,9,n}
  install -d $RPM_BUILD_ROOT/var/catman/X11R6/$i/cat{1,2,3,4,5,6,7,8,9,n}
done

strip $RPM_BUILD_ROOT/usr/bin/man

%preun
# Clean up accumulated cat litter.
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
%defattr(644, root, man, 755)
%attr(0644, root, root) %config /etc/cron.weekly/makewhatis.cron
%attr(2755, root,  man) /usr/bin/man
%attr(0755, root, root) /usr/bin/apropos
%attr(0755, root, root) /usr/bin/whatis
%attr(0755, root, root) /usr/sbin/makewhatis
%attr(0644, root, root) %config /etc/man.config

# Supported languages cs da de en es fr it nl pl pt sl

/usr/man/man[15]/*
%lang(cs) /usr/man/cs/man[15]/*
%lang(da) /usr/man/da/man[15]/*
%lang(de) /usr/man/de/man[15]/*
%lang(es) /usr/man/es/man[15]/*
%lang(fr) /usr/man/fr/man[15]/*
%lang(it) /usr/man/it/man[15]/*
%lang(nl) /usr/man/nl/man[15]/*
%lang(pl) /usr/man/pl/man[15]/*
%lang(pt) /usr/man/pt/man[15]/*
%lang(sl) /usr/man/sl/man[15]/*

/var/catman/cat[123456789n]
/var/catman/local/cat[123456789n]
/var/catman/X11R6/cat[123456789n]
%lang(cs) /var/catman/cs/cat[123456789n]
%lang(cs) /var/catman/local/cs/cat[123456789n]
%lang(cs) /var/catman/X11R6/cs/cat[123456789n]
%lang(da) /var/catman/da/cat[123456789n]
%lang(da) /var/catman/local/da/cat[123456789n]
%lang(da) /var/catman/X11R6/da/cat[123456789n]
%lang(de) /var/catman/de/cat[123456789n]
%lang(de) /var/catman/local/de/cat[123456789n]
%lang(de) /var/catman/X11R6/de/cat[123456789n]
%lang(es) /var/catman/es/cat[123456789n]
%lang(es) /var/catman/local/es/cat[123456789n]
%lang(es) /var/catman/X11R6/es/cat[123456789n]
%lang(fr) /var/catman/fr/cat[123456789n]
%lang(fr) /var/catman/local/fr/cat[123456789n]
%lang(fr) /var/catman/X11R6/fr/cat[123456789n]
%lang(it) /var/catman/it/cat[123456789n]
%lang(it) /var/catman/local/it/cat[123456789n]
%lang(it) /var/catman/X11R6/it/cat[123456789n]
%lang(nl) /var/catman/nl/cat[123456789n]
%lang(nl) /var/catman/local/nl/cat[123456789n]
%lang(nl) /var/catman/X11R6/nl/cat[123456789n]
%lang(pl) /var/catman/pl/cat[123456789n]
%lang(pl) /var/catman/local/pl/cat[123456789n]
%lang(pl) /var/catman/X11R6/pl/cat[123456789n]
%lang(pt) /var/catman/pt/cat[123456789n]
%lang(pt) /var/catman/local/pt/cat[123456789n]
%lang(pt) /var/catman/X11R6/pt/cat[123456789n]
%lang(sl) /var/catman/sl/cat[123456789n]
%lang(sl) /var/catman/local/sl/cat[123456789n]
%lang(sl) /var/catman/X11R6/sl/cat[123456789n]

%lang(cs) /usr/share/locale/cs/man
%lang(da) /usr/share/locale/da/man
%lang(de) /usr/share/locale/de/man
%lang(en) /usr/share/locale/en/man
%lang(es) /usr/share/locale/es/man
%lang(fr) /usr/share/locale/fr/man
%lang(it) /usr/share/locale/it/man
%lang(nl) /usr/share/locale/nl/man
%lang(pl) /usr/share/locale/pl/man
%lang(pt) /usr/share/locale/pt/man
%lang(sl) /usr/share/locale/sl/man

%changelog
* Sat Aug 26 1998 Konrad Stepien <konrad@interdata.com.pl>
  [1.5d-5]
- Reconfig to include international locales and man pages,
- Removed -D_GNU_SOURCE flag,
- Fix %install, to not install man2html
- "install -d" instead "mkdir -p" in %install,
- few simplification in %install,
- added pl translation.

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
  [1.5d-5]
- enable fsstnd organization
- change /var/catman/X11 to X11R6
- %post/%preun to clean up cat litter

* Tue Jun 02 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Tue Jun 02 1998 Erik Troan <ewt@redhat.com>
- you can't do free(malloc(10) + 4) <sigh>

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.5d

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.5a

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- uses a build root

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- updated to man-1.4j, which fixes some security problems; release 1 is
  for RH 4.2, release 2 is for glibc
 
* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Added /usr/lib/perl5/man to default manpath
