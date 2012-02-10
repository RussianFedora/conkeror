%define _conkdir %{_libdir}/conkeror

Summary:	A 100% keyboard driven mozilla based web browser.
Summary(ru):	Клавиатурно ориентированный веб браузер, основан на Mozilla XULRunner
Name:		conkeror
Version:	1.0pre
Release:	1%{?dist}.R

License:	MPLv1.1 or GPLv2 or LGPLv2.1
Group:		Applications/Internet
URL:		http://conkeror.org 
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-adaptation-reremix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires:	xulrunner
Provides:	webclient


%description
Conkeror is a keyboard-oriented, highly-customizable, highly-exten-
sible web browser based on Mozilla XULRunner, written mainly in 
JavaScript, and inspired by exceptional software such as Emacs and vi.
 Conkeror features a sophisticated keyboard system, allowing users to
 run commands and interact with content in powerful and novel ways. It
 is self-documenting, featuring a powerful interactive help system. 


%description -l ru
Conkeror является клавиатурно ориентированным, конфигурируемым, расшир
яемым веб браузером основанным на Mozilla XULRunner.

#---------------------------------------------------------------------
%prep
%setup -q
%patch0 -p1
%{__chmod} 755 reremix/conkeror
%{__chmod} 700 reremix/install.sh


%build
make %{?_smp_mflags}
sed -i "s!application.ini!%{_conkdir}/application.ini!" reremix/conkeror


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir}}
reremix/install.sh -prefix $RPM_BUILD_ROOT/usr &> /dev/null
ln -sf ../lib64/conkeror/conkeror $RPM_BUILD_ROOT%{_bindir}/conkeror


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING
%{_conkdir}
%{_bindir}/conkeror


%changelog
* Wed Jan  4 2012 Ilya Kuchmin <ikuchmin@ikuchmin.home.lan> - 1.0pre-1
- Change short notation -
- Compatibility xulrunner 7.0.1 -
- Change install process

* Sun Aug  7 2011 Ilya Kuchmin <ikuchmin@ikuchmin.home.lan> - 0.9.3-1.git20010721
- Initial build. First build. Patch from install lib64/. -
- Bug 437608 -

