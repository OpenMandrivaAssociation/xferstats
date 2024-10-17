%define name xferstats
%define version 2.16
%define release 9

Summary:	Compiles information about file transfers from logfiles
Name:		%name
Version:	%version
Release:	%release
URL:		https://xferstats.off.net/
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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.16-8mdv2010.0
+ Revision: 435116
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.16-7mdv2009.0
+ Revision: 262430
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.16-6mdv2009.0
+ Revision: 257061
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.16-4mdv2008.1
+ Revision: 130143
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import xferstats


* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.16-4mdk
- Rebuild

* Sun Dec 07 2003 Franck Villaume <fvill@freesurf.fr> 2.16-3mdk
- add BuildRequires glib-devel >= 1.2

* Sun Feb 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.16-2mdk
- rebuild

* Thu Nov 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.16-1mdk
- from Austin Acton <aacton@yorku.ca> :
	- stole and modified spec from RedHat for Mandrake 9.0
