%define upstream_name	 DateTime-Calendar-Pataphysical
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Dates in the pataphysical calendar
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-DateTime
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
DateTime::Calendar::Pataphysical is the implementation of the pataphysical
calendar. Each year in this calendar contains 13 months of 29 days. This
regularity makes this a convenient alternative for the irregular Gregorian
calendar.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{perl_vendorlib}/DateTime/Calendar/*
%{_mandir}/man3/*
