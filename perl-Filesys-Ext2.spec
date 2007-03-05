#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Filesys
%define	pnam	Ext2
Summary:	Filesys::Ext2 - Interface to ext2 and ext3 filesystem attributes
#Summary(pl):	
Name:		perl-Filesys-Ext2
Version:	0.20
Release:	0.1
# same as perl (REMOVE THIS LINE IF NOT TRUE)
#License:	GPL v1+ or Artistic
License:	-
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	787c8ffb4a2e2a8fa319e8a2f002aa22
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You may specify the path of the e2fsprogs upon use

  use Filesys::Ext2 {PATH=>'/path/to/binaries'};

Otherwise the module will use the default path /usr/bin/



# %description -l pl
# TODO

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
%doc CHANGES INSTALL README TODO
%{_bindir}/ls2.pl
%{perl_vendorlib}/Filesys/*.pm
#%{perl_vendorlib}/Filesys/Ext2
%{_mandir}/man3/*
%{_mandir}/man1/*
