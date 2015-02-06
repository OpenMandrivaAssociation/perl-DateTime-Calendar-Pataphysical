%define upstream_name	 DateTime-Calendar-Pataphysical
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Dates in the pataphysical calendar
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(DateTime)
BuildArch:	noarch

%description
DateTime::Calendar::Pataphysical is the implementation of the pataphysical
calendar. Each year in this calendar contains 13 months of 29 days. This
regularity makes this a convenient alternative for the irregular Gregorian
calendar.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/DateTime/Calendar/*
%{_mandir}/man3/*


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 681389
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 406974
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.04-5mdv2009.0
+ Revision: 241200
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-3mdv2008.0
+ Revision: 86339
- rebuild


* Mon Jan 23 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-2mdk
- Add BuildRequires: perl-DateTime

* Tue Nov 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.04-1mdk
- Initial MDV package

