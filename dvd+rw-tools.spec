%define name                    dvd+rw-tools
%define version			7.1
%define release                 %mkrel 7

Summary:	Tools for burning on DVD+RW compliant burner
Group:          Archiving/Cd burning
Name: 		%{name}
Version:	%{version}
Release:        %{release}
License:	GPLv2
Source0:	http://fy.chalmers.se/~appro/linux/DVD+RW/tools/dvd+rw-tools-%{version}.tar.gz
Source1:	dvd+rw-mediainfo.1
# (fc) use genisoimage, not mkisofs by default (SUSE)
Patch0:		growisofs-genisoimage.patch
# fix build with gcc 4.3
Patch2:		dvd+rw-tools-limits.h_fix.diff
# (fc) Allow burn small images on DVD-DL (Fedora bug #476154)
Patch3:		dvd+rw-tools-7.0-dvddl.patch
# (fc) fix widechar overflow (Fedora bug #426068)
Patch4:		dvd+rw-tools-7.0-wctomb.patch
# (fc) fix exit status of dvd+rw-format (Fedora bug #243036)
Patch5:		dvd+rw-tools-7.0-wexit.patch
# (fc) use rpm_opt_flags (SUSE)
Patch6:		rpm_opt_flags.diff
URL:		http://fy.chalmers.se/~appro/linux/DVD+RW/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	cdrkit-genisoimage

%description 
Even though a modified kernel can let you put for example an ext2 file
system on DVD+RW, it's probably not very practical, because you most
likely want to access the data on an arbitrary computer. Or in other
words you most likely want ISO9660. The trouble is that you might as
well want to add data now and then. And what options do you have in
the lack of multiple sessions (no, DVD+RW has no notion of multiple
sessions)? Complete re-mastering which takes more and more time as
data set grows? Well, yes, unless you employ growisofs! Growisofs
provides the way to both lay down and grow an ISO9660 file system on
(as well as to burn an arbitrary pre-mastered image to) all supported
optical media.

%prep

%setup -q
%patch0 -p1 -b .genisoimage
%patch2 -p1 -b .limits
%patch3 -p1 -b .dvddl
%patch4 -p1 -b .wctomb
%patch5 -p1 -b .wexit
%patch6 -p1 -b .rpm_opt_flags

%build

%make LDFLAGS="%{ldflags}"
%make rpl8 btcflash LDFLAGS="%{ldflags}"

%install

make install prefix=$RPM_BUILD_ROOT%{_prefix}
install -d $RPM_BUILD_ROOT%{_sbindir}
install -m755 rpl8 $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf %buildroot

%files
%defattr(-, root, root) 
%doc index.html
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 7.1-5mdv2011.0
+ Revision: 663898
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 7.1-4mdv2011.0
+ Revision: 604835
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 7.1-3mdv2010.1
+ Revision: 520096
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 7.1-2mdv2010.0
+ Revision: 413414
- rebuild

* Tue Jan 20 2009 Frederic Crozat <fcrozat@mandriva.com> 7.1-1mdv2009.1
+ Revision: 331826
- Release 7.1
- Remove patch1 (no needed)
- Regenerate patch0 with SUSE version
- Patch3 (Fedora): allow to burn small images on DVD-DL (fedora bug #476154)
- Patch4 (Fedora): fix widechar overflow (Fedora bug #426068)
- Patch5 (Fedora): fix exit status of dvd+rw-format (Fedora bug #243036)
- Patch6 (SUSE): use rpm opt flags

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 7.0-7mdv2009.1
+ Revision: 316620
- use %%optflags and %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 7.0-6mdv2009.0
+ Revision: 220712
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 7.0-5mdv2008.1
+ Revision: 179827
- added P2 to make it build (thanks erwan velu)
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 7.0-3mdv2008.0
+ Revision: 90203
- fix the patch
- add dvd+rw-tools-7.0-pointer.patch to fix a pointer type error during build. From OpenSDE trac
- rebuild for 2008
- improved description
- new license policy


* Tue Jan 09 2007 Götz Waschk <waschk@mandriva.org> 7.0-2mdv2007.0
+ Revision: 106600
- use cdrkit

* Sun Dec 03 2006 Emmanuel Andry <eandry@mandriva.org> 7.0-1mdv2007.1
+ Revision: 90163
- New version 7.0
  %%mkrel
- Import dvd+rw-tools

* Wed Feb 15 2006 Warly <warly@mandriva.com> 6.1-1mdk
- new version
   - Initial DVD+RW Double Layer support
   - fix for DVD+R recordings in Samsung TS-H542A;
   - DVD-R Dual Layer DAO and Incremental support;

* Mon Aug 30 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 5.21.4.10.8-2mdk
- Add missing files (manpages and programs)
- Drop dependency on cdrecord, only mkisofs is needed
- Add manpage for dvd+rw-media-info from Debian

* Mon Aug 30 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 5.21.4.10.8-1mdk
- Release 5.21.4.10.8 (ie linux 2.6.8 friendly version)

* Sat Jul 31 2004 Laurent Culioli <laurent@mandrake.org> 5.20.4.10.8-1mdk
- new version ( fix speed pb with k3b )

* Wed Jun 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 5.18.4.8.6-2mdk
- Rebuild

* Thu Apr 29 2004 Warly <warly@mandrakesoft.com> 5.18.4.8.6-1mdk
- new version

* Thu Feb 26 2004 Warly <warly@mandrakesoft.com> 5.17.4.8.6-1mdk
- new version
- seems to fix burning under 2.6 ATA interface

