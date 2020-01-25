#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Object
%define	pnam	Signature
Summary:	Signature - Generate cryptographic signatures for objects
Summary(pl.UTF-8):	Signature - generowanie podpisów kryptograficznych dla obiektów
Name:		perl-Object-Signature
Version:	1.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	387fd336d07bd5e74669ec33515c28ef
URL:		http://search.cpan.org/dist/Object-Signature/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Object::Signature is an abstract base class that you can inherit from
in order to allow your objects to generate unique cryptographic
signatures.

The method used to generate the signature is based on Storable and
Digest::MD5. The object is fed to Storable::nfreeze to get a string,
which is then passed to Digest::MD5::md5_hex to get a unique 32
character hexadecimal signature.

%description -l pl.UTF-8
Object::Signature to abstrakcyjna klasa bazowa, z której można
dziedziczyć, aby umożliwić obiektom generowanie unikalnych podpisów
kryptograficznych.

Metoda używana do generowania podpisów opiera się na Storable i
Digest::MD5. Obiekt jest przekazywany do Storable::nfreeze w celu
uzyskania łańcucha znaków, który jest następnie przekazywany do
Digest::MD5::md5_hex w celu uzyskania unikalnego 32-znakowego podpisu
szesnastkowego.

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
%doc Changes README
%{perl_vendorlib}/Object/*.pm
%{perl_vendorlib}/Object/Signature
%{_mandir}/man3/*
