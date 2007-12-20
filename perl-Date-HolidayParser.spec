%define module	Date-HolidayParser
%define name	perl-%{module}
%define version 0.3
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Parser for ~/.holiday-style files
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/ReadLine/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch

%description
This is a module that parses .holiday-style files. These are
files that define holidays in various parts of the world.
The files are easy to write and easy for humans to read, but can
be hard to parse because the format allows many different ways to write it.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make "CFLAGS=%{optflags}"

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/Date

