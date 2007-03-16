#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Filesys
%define	pnam	Ext2
Summary:	Filesys::Ext2 - Interface to ext2 and ext3 filesystem attributes
Summary(pl.UTF-8):	Filesys::Ext2 - interfejs do atrybutów systemów plików ext2 i ext3
Name:		perl-Filesys-Ext2
Version:	0.20
Release:	0.1
License:	free (see LICENSE.pod)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Filesys/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	787c8ffb4a2e2a8fa319e8a2f002aa22
URL:		http://search.cpan.org/dist/Filesys-Ext2/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# lsattr, chattr
Requires:	e2fsprogs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesys::Ext2 is an interface to ext2 and ext3 filesystem attributes
(chattr and lsattr functions).

%description -l pl.UTF-8
Filesys::Ext2 to interfejs do atrybutów systemów plików ext2 i ext3
(funkcji chattr i lsattr).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL LICENSE.pod README TODO
%attr(755,root,root) %{_bindir}/ls2.pl
%{perl_vendorlib}/Filesys/Ext2.pm
%{_mandir}/man3/*
%{_mandir}/man1/*
