%define upstream_name	 Date-HolidayParser
%define upstream_version 0.41

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Parser for ~/.holiday-style files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/ReadLine/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)

BuildArch:	noarch

%description
This is a module that parses .holiday-style files. These are
files that define holidays in various parts of the world.
The files are easy to write and easy for humans to read, but can
be hard to parse because the format allows many different ways to write it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make "CFLAGS=%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/Date


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.410.0-2mdv2011.0
+ Revision: 681387
- mass rebuild

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.410.0-1mdv2011.0
+ Revision: 595096
- update to new version 0.41

  + Jérôme Quelin <jquelin@mandriva.org>
    - adding missing buildrequires
    - update to 0.4

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.1
+ Revision: 504811
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3-5mdv2010.0
+ Revision: 430404
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.3-4mdv2009.0
+ Revision: 256488
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.3-2mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-2mdv2008.0
+ Revision: 86335
- rebuild


* Tue Aug 01 2006 Eskild Hustvedt <eskild@mandriva.org> 0.3-1mdv
- Initial Mandriva package

