Name: bonnie++
Version: 1.96
Release: %mkrel 4
Summary: A program for benchmarking hard drives and filesystems
License: GPLv2+
Group: System/Kernel and hardware
URL: http://www.coker.com.au/bonnie++/
Source: http://www.coker.com.au/bonnie++/bonnie++-%{version}.tgz 
Provides: bonnie
Obsoletes: bonnie
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Bonnie++ is a benchmark suite that is aimed at performing a number of simple
tests of hard drive and file system performance.

%prep

%setup -q

%build
%configure2_5x
%make MORECFLAGS="%{optflags} %{?ldflags}"
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
/sbin/getc_putc
/sbin/getc_putc_helper
/sbin/zcav
/bin/bon_csv2html
/bin/bon_csv2txt
/bin/generate_randfile
%{_mandir}/man1/*
%{_mandir}/man8/*




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.96-4mdv2011.0
+ Revision: 663329
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.96-3mdv2011.0
+ Revision: 603763
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.96-2mdv2010.1
+ Revision: 520016
- rebuilt for 2010.1

* Sun Jul 05 2009 Frederik Himpe <fhimpe@mandriva.org> 1.96-1mdv2010.0
+ Revision: 392661
- Update to new version 1.96

* Wed Dec 10 2008 Funda Wang <fwang@mandriva.org> 1.03e-1mdv2009.1
+ Revision: 312424
- New version 1.03e

* Thu Jul 24 2008 Erwan Velu <erwan@mandriva.org> 1.03d-1mdv2009.0
+ Revision: 245950
- 1.03d

* Wed May 21 2008 Oden Eriksson <oeriksson@mandriva.com> 1.03c-2mdv2009.0
+ Revision: 209673
- added a gcc43 patch from fedora

* Sun Jan 27 2008 Funda Wang <fwang@mandriva.org> 1.03c-1mdv2008.1
+ Revision: 158663
- update to new version 1.03c

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 05 2007 Funda Wang <fwang@mandriva.org> 1.03b-1mdv2008.1
+ Revision: 115504
- New version 1.03b


* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1.03a-3mdv2007.1
+ Revision: 145449
- Import bonnie++

* Wed Dec 28 2005 Erwan Velu <erwan@seanodes.com> 1.03a-3mdk
- Rebuild

* Sat Jun 05 2004 <lmontel@n2.mandrakesoft.com> 1.03a-2mdk
- Rebuild

* Mon Mar 22 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.03a-1mdk
- Release 1.03a.

