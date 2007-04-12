%define module	DateTime-Calendar-Pataphysical
%define name	perl-%{module}
%define version	0.04
%define release	%mkrel 2

Summary:	Dates in the pataphysical calendar
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
Requires:	perl
BuildRequires:	perl-devel
BuildRequires:  perl-DateTime
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
DateTime::Calendar::Pataphysical is the implementation of the pataphysical
calendar. Each year in this calendar contains 13 months of 29 days. This
regularity makes this a convenient alternative for the irregular Gregorian
calendar.

%prep
%setup -q -n %{module}-%{version}

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

