%define name xferstats
%define version 2.16
%define release %mkrel 6

Summary:	Compiles information about file transfers from logfiles
Name:		%name
Version:	%version
Release:	%release
URL:		http://xferstats.off.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		xferstats.patch.bz2
Patch1:		xferstats-2.16-config-loc.patch.bz2
License:	GPL
Group:		Monitoring
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	glib-devel >= 1.2

%description
xferstats compiles information about file transfers from logfiles.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/xferstats/
cp -a graphs %{buildroot}%{_datadir}/xferstats/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog
%config(noreplace) %{_sysconfdir}/xferstats.cfg
%{_bindir}/xferstats
%{_mandir}/*/*
%{_datadir}/xferstats

