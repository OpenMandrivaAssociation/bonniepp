%define	debug_package	%{nil}

Summary:	A program for benchmarking hard drives and filesystems
Name:		bonnie++
Version:	1.96
Release:	4
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.coker.com.au/bonnie++/
Source0:	http://www.coker.com.au/bonnie++/%{name}-%{version}.tgz 
Provides:	bonnie

%description
Bonnie++ is a benchmark suite that is aimed at performing a number of simple
tests of hard drive and file system performance.

%prep
%setup -q

%build
%configure2_5x
%make MORECFLAGS="%{optflags} %{?ldflags}"
sed -i -e "s@/usr/share/doc/bonnie\+\+/@%{_docdir}/%{name}-%{version}/@" bonnie++.8

%install
[ -e debian/changelog ]&& (rm -f changelog.txt;mv debian/changelog changelog.txt)
sed -i -e "s@usr/share/man@%{buildroot}%{_mandir}@g" Makefile
%makeinstall eprefix=%{buildroot} DESTDIR=%{buildroot}

%files
%doc changelog.txt readme.html credits.txt
/sbin/bonnie++
/sbin/getc_putc
/sbin/getc_putc_helper
/sbin/zcav
/bin/bon_csv2html
/bin/bon_csv2txt
/bin/generate_randfile
%{_mandir}/man1/*
%{_mandir}/man8/*

