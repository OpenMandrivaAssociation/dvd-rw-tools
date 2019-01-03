Summary:	Tools for burning on DVD+RW compliant burner
Group:          Archiving/Cd burning
Name: 		dvd+rw-tools
Version:	7.1
Release:        23
License:	GPLv2
Url:		http://fy.chalmers.se/~appro/linux/DVD+RW/
Source0:	http://fy.chalmers.se/~appro/linux/DVD+RW/tools/dvd+rw-tools-%{version}.tar.gz
Source1:	dvd+rw-mediainfo.1
# (fc) use genisoimage, not mkisofs by default (SUSE)
Patch0:         growisofs-genisoimage.patch
# (tpg) Fedora patches
Patch1:		dvd+rw-tools-7.0.manpatch
Patch2:		dvd+rw-tools-7.0-wexit.patch
Patch3:		dvd+rw-tools-7.0-glibc2.6.90.patch
Patch4:		dvd+rw-tools-7.0-reload.patch
Patch5:		dvd+rw-tools-7.0-wctomb.patch
Patch6:		dvd+rw-tools-7.0-dvddl.patch
Patch7:		dvd+rw-tools-7.1-noevent.patch
Patch8:		dvd+rw-tools-7.1-lastshort.patch
Patch9:		dvd+rw-tools-7.1-format.patch
Patch10:	dvd+rw-tools-7.1-bluray_srm+pow.patch
Patch11:	dvd+rw-tools-7.1-bluray_pow_freespace.patch
Patch12:	dvd+rw-tools-7.1-sysmacro-inc.patch

Requires:	mkisofs

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
%patch0 -p1 -b .genisoimage
%patch1 -p1 -b .manpatch
%patch2 -p1 -b .wexit
%patch3 -p1 -b .glibc2.6.90
%patch4 -p1 -b .reload
%patch5 -p0 -b .wctomb
%patch6 -p0 -b .dvddl
%patch7 -p1 -b .noevent
%patch8 -p1 -b .lastshort
%patch9 -p1 -b .format
%patch10 -p1 -b .pow
%patch11 -p1 -b .freespace
%patch12 -p1 -b .sysmacro

%build
%setup_compile_flags
%make_build WARN="-DDEFAULT_BUF_SIZE_MB=16 -DRLIMIT_MEMLOCK" LDFLAGS="%{ldflags}"
%make_build rpl8 btcflash LDFLAGS="%{ldflags}"

%install
make install prefix=%{buildroot}%{_prefix}
install -d %{buildroot}%{_sbindir}
install -m755 rpl8 %{buildroot}%{_sbindir}

%files
%doc index.html
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man1/*

