%define name                    dvd+rw-tools
%define version			7.0
%define release                 %mkrel 2

Summary:	Tools for burning on DVD+RW compliant burner
Group:          Archiving/Cd burning
Name: 		%{name}
Version:	%{version}
Release:        %{release}
License:	GPL
Source0:	http://fy.chalmers.se/~appro/linux/DVD+RW/tools/dvd+rw-tools-%{version}.tar.bz2
Source1:	dvd+rw-mediainfo.1
Patch: dvd+rw-tools-7.0-cdrkit.patch
URL:		http://fy.chalmers.se/~appro/linux/DVD+RW/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	cdrkit-genisoimage

%description 

As for cdrecord[-ProDVD]. DVD+RW/+R recording strategy is somewhat
different from one supported by cdrecord. DVD+RW (but not DVD+R) is a
true random write access media and therefore is suitable for housing
of arbitrary filesystem, e.g. udf, vfat, ext2, etc. This, and this
alone, qualifies DVD+RW support for kernel implementation.

Even though modified kernel can let you put for example an ext2
filesystem on DVD+RW, it's probably not very practical, because you
most likely want to access the data on arbitrary computer. Or in other
words you most likely want ISO9660.

%prep

%setup -q
%patch -p1

%build

%make
%make rpl8
%make btcflash

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


