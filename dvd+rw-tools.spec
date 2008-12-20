%define name                    dvd+rw-tools
%define version			7.0
%define release                 %mkrel 7

Summary:	Tools for burning on DVD+RW compliant burner
Group:          Archiving/Cd burning
Name: 		%{name}
Version:	%{version}
Release:        %{release}
License:	GPL+
Source0:	http://fy.chalmers.se/~appro/linux/DVD+RW/tools/dvd+rw-tools-%{version}.tar.bz2
Source1:	dvd+rw-mediainfo.1
Patch0:		dvd+rw-tools-7.0-cdrkit.patch
# Fixes incompatible pointer type errors during build. From 
# http://trac.opensde.org/ticket/8 - AdamW 2007/09
Patch1:		dvd+rw-tools-7.0-pointer.patch
Patch2:		dvd+rw-tools-limits.h_fix.diff
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
%patch0 -p1
%patch1 -p1 -b .pointer
%patch2 -p1

%build

%make CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}"
%make rpl8 CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}"
%make btcflash CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

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

