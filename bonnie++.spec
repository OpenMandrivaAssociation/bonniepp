Name: bonnie++
Version: 1.03b
Release: %mkrel 1
Summary: A program for benchmarking hard drives and filesystems
License: GPLv2+
Group: System/Kernel and hardware
URL: http://www.coker.com.au/bonnie++/
Source: http://www.coker.com.au/bonnie++/bonnie++-%{version}.tgz 
Provides: bonnie
Obsoletes: bonnie

%description
Bonnie++ is a benchmark suite that is aimed at performing a number of simple
tests of hard drive and file system performance.

%prep
%setup -q
autoconf

%build
%configure2_5x
%make 
perl -pi -e "s@/usr/share/doc/bonnie\+\+/@%_docdir/%name-%version/@" bonnie++.8

%install
rm -rf $RPM_BUILD_ROOT
[ -e debian/changelog ]&& (rm -f changelog.txt;mv debian/changelog changelog.txt)
perl -pi -e "s@usr/share/man@%{buildroot}%_mandir@g" Makefile
%makeinstall eprefix=%{buildroot} DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc changelog.txt readme.html credits.txt
/sbin/bonnie++
/sbin/zcav
/bin/bon_csv2html
/bin/bon_csv2txt
%{_mandir}/man1/*
%{_mandir}/man8/*


