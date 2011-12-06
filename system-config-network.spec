# -*- RPM-SPEC -*-
Summary: The GUI of the Network Adminstration Tool
Name: system-config-network
Version: 1.6.0.el6.2
Release: 1%{?dist}
URL: http://fedoraproject.org/wiki/SystemConfig/network
Source0: %{name}-%{version}.tar.bz2
License: GPLv2+
Group: Applications/System 
BuildArch: noarch
Obsoletes: isdn-config <= 0.18-10.70 internet-config <= 0.40-2 rp3 <= 1.1.10-4 redhat-config-network < %{version}
Provides: redhat-config-network = %{version} isdn-config = 0.18-10.70.1 internet-config = 0.40-2.1
BuildRequires: python >= 0:2.2, openjade, docbook-style-dsssl, perl, gettext, glibc-devel
BuildRequires: gcc, desktop-file-utils, perl-XML-Parser, intltool
Requires: %{name}-tui = %{version}-%{release}
Requires: pygtk2-libglade, pygtk2, gnome-python2, gnome-python2-canvas
Requires: usermode-gtk, /usr/bin/htmlview, gnome-python2-gnome, gnome-python2-bonobo
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This is the GUI of the network configuration tool,
supporting Ethernet, Wireless, TokenRing, ADSL, ISDN and PPP.

%package tui
Summary: The Network Adminstration Tool
Group: Applications/System 
Obsoletes: netcfg <= 2.36-3p redhat-config-network-tui < %{version} netconf <= 0.1-1 netconfig <= 0.8.24-1.2.2.1
Provides: redhat-config-network-tui = %{version} netcfg = 2.36-3p.1 netconf = 0.1-1.1 netconfig = 0.8.24-1.2.2.1.1
Requires: initscripts >= 0:5.99, usermode , python, rpm-python, newt-python, pciutils, usermode, dbus-python
Requires: python-ethtool python-iwlib

%description tui
This is the network configuration tool,
supporting Ethernet, Wireless, TokenRing, ADSL, ISDN and PPP.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

mkdir $RPM_BUILD_ROOT%{_datadir}/applications

for i in system-config-network.desktop system-control-network.desktop; do \
  desktop-file-install --vendor redhat --delete-original       \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
    --add-category System                                     \
    --add-category Settings                                   \
    $RPM_BUILD_ROOT%{_datadir}/system-config-network/$i; \
done;

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/networking/devices
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/networking/profiles/default

rm -fr $RPM_BUILD_ROOT%{_datadir}/system-config-network/pixmaps
rm -fr $RPM_BUILD_ROOT%{_datadir}/system-config-network/netconfpkg/gui
rm -fr $RPM_BUILD_ROOT%{_datadir}/system-config-network/netconf.py*
rm -fr $RPM_BUILD_ROOT%{_datadir}/system-config-network/netconf_control.py*
rm -fr $RPM_BUILD_ROOT%{_sbindir}/system-config-network-gui
rm -fr $RPM_BUILD_ROOT%{_bindir}/system-control-network
rm -fr $RPM_BUILD_ROOT%{_datadir}/applications/*
rm -fr $RPM_BUILD_ROOT%{_datadir}/pixmaps/*

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang tui
%defattr(-,root,root,-)
%doc COPYING
%dir %{_datadir}/system-config-network
%doc %dir %{_datadir}/system-config-network/help
%doc %{_datadir}/system-config-network/help/*
%{_datadir}/system-config-network/netconf_cmd.py*
%{_datadir}/system-config-network/netconf_tui.py*
%{_datadir}/system-config-network/version.py*
%dir %{_datadir}/system-config-network/netconfpkg
%{_datadir}/system-config-network/netconfpkg/conf
%{_datadir}/system-config-network/netconfpkg/tui
%{_datadir}/system-config-network/netconfpkg/plugins
%{_datadir}/system-config-network/netconfpkg/*.py*
%{_datadir}/system-config-network/module-info
%{_datadir}/system-config-network/providerdb
%config(noreplace) %{_sysconfdir}/pam.d/*
%config(noreplace) %{_sysconfdir}/security/console.apps/*
%dir %{_sysconfdir}/sysconfig/networking
%dir %{_sysconfdir}/sysconfig/networking/profiles
%dir %{_sysconfdir}/sysconfig/networking/profiles/default
%dir %{_sysconfdir}/sysconfig/networking/devices
%{_sbindir}/system-config-network
%{_sbindir}/system-config-network-tui
%{_sbindir}/system-config-network-cmd
%{_bindir}/system-config-network
%{_bindir}/system-config-network-cmd

%changelog
* Tue Jun 22 2010 Harald Hoyer <harald@redhat.com> 1.6.0.el6.2-1
- only build tui subpackage
- fixed moduled.conf handling
Resolves: rhbz#606794
- fixed crypto/hash 
Resolves: rhbz#606796

* Fri Jan 15 2010 Harald Hoyer <harald@redhat.com> 1.6.0-1
- version 1.6.0
- Resolves: rhbz#555142 rhbz#533495

* Mon Sep 14 2009 Harald Hoyer <harald@redhat.com> 1.5.99-1
- version 1.5.99
- removed all rhpl requirements
- extended classes for --import and --export

* Tue Apr 14 2009 Harald Hoyer <harald@redhat.com> 1.5.97-1
- translation update

* Wed Feb 18 2009 Harald Hoyer <harald@redhat.com> 1.5.96-1
- translation update (harald)
- added DNS1 and DNS2 to the device specific config (harald)
- do not raise NotImplementedError for getDialog (harald)
- DSN -> DNS typo (harald)
- NotImplemented -> NotImplementedError (harald)

* Fri Dec 12 2008 Jiri Moskovcak <jmoskovc@redhat.com> 1.5.95-1
- New version 1.5.95
- Fixed hostname test according to latest rfc. (rhbz#473919)
- Don't write empty options to config file
- Fixed s-control-network crash when run as non-root (rhbz#470203)
- DSL: Fixed overwritting synchrounous mode to 'yes' (rhbz#475155)
- Fixed typo in NCIPsec.py. (rhbz#474988)
- Added gnome-python2-gnome to Requirements (rhbz#472154)
- Improved compatibility with NetworkManager
- Resolves: #472154, #475155, #473919, #474988, #470203

* Tue Dec 02 2008 Jiri Moskovcak <jmoskovc@redhat.com> 1.5.94-1 
- version 1.5.94
- fixed tcp/ip gateway/netmask problem
- fixed crash when pap-secrets contains spaces
- Resolves: #469434, #465748

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.5.93-3 
- Rebuild for Python 2.6

* Tue Oct 28 2008 Harald Hoyer <harald@redhat.com> 1.5.93-2 
- version 1.5.93

* Mon Oct 27 2008 Tom "spot" Callaway <tcallawa@redhat.com>
- don't try to write out Description if vendor is NULL (bz 468355)
  (thanks to Kazunori Asayama)

* Mon Oct 27 2008 Matthias Clasen  <mclasen@redhat.com>
- Require usermode-gtk

* Sat Mar 29 2008 Harald Hoyer <harald@redhat.com> - 1.5.92
- removed unnecessary self argument in super calls (bz#437678) (harald)

* Thu Mar 27 2008 Harald Hoyer <harald@redhat.com> - 1.5.91
- more pylint and cleanups (harald)
- removed Init2 string (clashes with UTMS) (harald)
- check if hostname is not None, before checking it (harald)
- changed to python logging (harald)
- no activate/deactivate/delete NMControlled devices (harald)
- changed source from tar.gz to tar.bz2 (harald)

* Thu Mar 27 2008 Harald Hoyer <harald@redhat.com> - 1.5.90
- genClass replacement (harald@redhat.com)
- split Conf.py in several submodules (harald@redhat.com)
- added tui/NCPluginTokenRingInterface (harald@redhat.com)
- BackendHal fix to use Factory classes (harald@redhat.com)
- name consistency (harald@redhat.com)
- named all plugins NCPlugin (harald@redhat.com)
- speedup module loading by only calling register_plugin from __init__ (harald@redhat.com)
- make pylint and pychecker happy (harald@redhat.com)
- ignore system hardware for the UnitTest (harald@redhat.com)
- MTU moved to base device (harald@redhat.com)
- extended UnitTests (harald@redhat.com)
- use newer automake/aclocal syntax (harald@redhat.com)

* Thu Feb 28 2008 Harald Hoyer <harald@redhat.com> - 1.5.1
- removed CIPE (harald)
- s/Devernet/Network/ (harald)
- Auto -> auto (harald)
- only append localhost to AliasList, if not already in (harald)
- show error dialog, if device loading failes (harald)
- moved MRU to Dialup only (harald)
- recognize qeth devices in kudzu lists (rhbz#184734) (harald)
- added MRU field (rhbz#221294) (harald)
- added TUI for QETH (harald)
- do not traceback, if we try to remove a device not in our active list (harald)
- added qeth support (harald)
- removed ctc and iucv devices (rhbz#219180) (harald)
- do not handle ifcfg-${parent_device}-range* rhbz#221292 (harald)
- Minor fix in hosts parser to make tui works. (jmoskovc)
- Stupid mode doesn't go away anymore.(rhbz#177931) (jmoskovc)
- Fixed crash when Baud=None (jmoskovc)
- Removing PPP option should work. NETWORKMANAGER -> NM_CONTROLLED (jmoskovc)
- Fixed problem with import rhbz#429725 (jmoskovc)
- Changed Clist in host editor to GtkTreeView, added checkbox to show loopbacks in hosts (jmoskovc)
- Minor fix in hosts parser - now it accepts trailing dot. (jmoskovc)
- Improved {pap|chap}-secrets parser, added checkbox to reveal password in dialup config (jmoskovc)
- Fixed crash when hostname is changed. (jmoskovc)

* Mon Dec 03 2007 Harald Hoyer <harald@redhat.com> - 1.5.0
- v1.5.0

* Mon Dec 03 2007 Harald Hoyer <harald@redhat.com>, Jiri Moskovcak <jmoskovc@redhat.com> - 1.4.7
- added HAL support
- fixed /etc/hosts parser
- added "Controlled by NetworkManager"
- do not fall into modified state for activate/deactivate (rhbz#377261)

* Mon Nov 12 2007 Harald Hoyer <harald@redhat.com> - 1.4.6
- moved network.xpm to (pkgdatadir)/pixmaps (rhbz#377861)

* Mon Nov 12 2007 Harald Hoyer <harald@redhat.com> - 1.4.5
- changed yelp to htmlview

* Wed Nov  7 2007 Stepan Kasal <skasal@redhat.com> - 1.4.4
- s/NEtwork/Network/ in the summary of -tui, to be consistent
  with the summary line of the main rpm (the neat acronym is no
  longer advertised anyway)
- Resolves: #239216

* Fri Oct 26 2007 Harald Hoyer <harald@redhat.com> - 1.4.4
- removed not yet used NCBackendHal.py (rhbz#353771)
- fixed yelp dependency (rhbz#344981)
- moved %%configure to %%build (rhbz#353761)
- fixed type with getRoot (rhbz#368871)

* Mon Oct 15 2007 Harald Hoyer <harald@redhat.com> - 1.4.3
- fixed /etc/hosts problem (rhbz#331451)

* Fri Oct 12 2007 Harald Hoyer <harald@redhat.com> - 1.4.3
- added version.py.in to POTFILES.in (rhbz#244053)
- corrected URL (rhbz#237717)

* Mon Oct 08 2007 Harald Hoyer <harald@redhat.com> - 1.4.2
- speedup genClass
- restorecon selinux context

* Mon Sep 24 2007 Harald Hoyer <harald@redhat.com> - 1.4.1-2
- require newt-python instead of newt only

* Mon Sep 24 2007 Harald Hoyer <harald@redhat.com> - 1.4.1
- version 1.4.1

* Thu Aug 16 2007 Harald Hoyer <harald@redhat.com> - 1.4.0
- version 1.4.0

* Mon Jan  8 2007 Harald Hoyer <harald@redhat.com> - 1.3.99
- fixed #221289
- Resolves: rhbz#221289

* Fri Dec 15 2006 Harald Hoyer <harald@redhat.com> - 1.3.98
- translation update (bug #216559)
- Resolves: rhbz#216559

* Tue Nov 28 2006 Harald Hoyer <harald@redhat.com> - 1.3.97
- translation update

* Thu Nov  2 2006 Harald Hoyer <harald@redhat.com> - 1.3.96
- Resolves: rhbz #211980, rhbz #213181

* Wed Oct  4 2006 Harald Hoyer <harald@redhat.com> - 1.3.95
- translation update (bug #208886)
- use rhpl.iwlib for wireless functions (bug #197954)
- added perl-XML-Parser build requirement

* Tue Aug 15 2006 Harald Hoyer <harald@redhat.com> - 1.3.94
- translation update (bug #182650)

* Tue Aug 15 2006 Harald Hoyer <harald@redhat.com> - 1.3.93
- added tui subdir (bug #202560)

* Fri Aug 11 2006 Harald Hoyer <harald@redhat.com> - 1.3.92
- fixed #201659 
- translation update

* Tue Jul 25 2006 Harald Hoyer <harald@redhat.com> - 1.3.91
- fixed "New Device" in text-mode

* Tue Jul 18 2006 Harald Hoyer <harald@redhat.com> - 1.3.90
- fixed:
- [135014] MTU and MRU should be confiurable for ADSL
- [141055] system-config-network needs to be able to set MTU
- [149780] no GATEWAY, IPADDR and NETMASK, if BOOTPROTO=dhcp 
- [150362] [Errno 2] No such file or directory: '/etc/hosts'
- [157172] Wrong DNS for provider "ZEDAT_Berlin"
- [160417] Bad: cannot make any changes to network settings
- [169819] Trailing space in host name causes crash
- [175078] String (country name) change request
- [176145] Please enable Serbian translation in system-config-network
- [177198] deprecation warning in system-config-network
- [187563] localized option passed to ifcfg-wlan0 files
- [188321] Creating an alias for a network interface breaks device 
           setup after reboots
- [190242] Firefox instance running as root when used to read docs 
           for system-config-*
- [197401] Don't write HWADDR for alias interfaces

* Fri Jul 14 2006 Nils Philippsen <nphilipp@redhat.com>
- enable ml, or, sr, sr@Latn translations (#176145)

* Wed Nov 02 2005 Harald Hoyer <harald@redhat.com> - 1.3.30
- removed interdruid
- reversed Cancel/Ok button ordering

* Tue Oct 25 2005 Harald Hoyer <harald@redhat.com> - 1.3.29
- fixed profileFrame labeling

* Wed Oct 10 2005 Harald Hoyer <harald@redhat.com> - 1.3.28
- fixed picture paths in glade files
- fixed cancel case of passphrase dialog

* Wed Oct 10 2005 Harald Hoyer <harald@redhat.com> - 1.3.27
- use new pam stack replacement
- added OnParent for Alias Devices
- added SPI and better key generation for ipsec
- corrected column handling in main window
- GUI liftup
- added AVM Fritz!PCI v2.0 ISDN card to ISDN Hardwarelist (bug 134605)
- remove /etc/sysconfig/isdncard, if no ISDN is configured

* Wed Apr 20 2005 Harald Hoyer <harald@redhat.com> - 1.3.26
- CBCP_MSN added (bug #125710)

* Tue Mar 31 2005 Harald Hoyer <harald@redhat.com> - 1.3.25
- more i18n languages

* Wed Mar 30 2005 Harald Hoyer <harald@redhat.com> - 1.3.24
- gtk.FALSE and gtk.TRUE cleanups

* Mon Mar 21 2005 Harald Hoyer <harald@redhat.com> - 1.3.23-2
- moved gui parts out of the tui package

* Fri Mar 04 2005 Harald Hoyer <harald@redhat.com> - 1.3.23
- update to new gnome/gtk/glade

* Wed Oct 20 2004 Harald Hoyer <harald@redhat.com> - 1.3.22
- translation updates, added nb.po (bug 136462)

* Tue Oct 05 2004 Harald Hoyer <harald@redhat.com> - 1.3.21
- fixed /etc/hosts handling
- handle .ko module names in updateFromKudzu

* Fri Sep 03 2004 Harald Hoyer <harald@redhat.com> - 1.3.20
- dhcp cannot be selected for aliased devices (bug 129096)

* Thu Aug 26 2004 Harald Hoyer <harald@redhat.com> - 1.3.19
- hopefully fixed bug 125393
- fixed removal of device files

* Fri Jul 30 2004 Harald Hoyer <harald@redhat.com> - 1.3.18
- changed mainloop and mainquit
- translation updates
 
* Tue Jul 06 2004 Harald Hoyer <harald@redhat.com> - 1.3.17
- bugfix release for FC2

* Tue Jun 29 2004 Harald Hoyer <harald@redhat.com> - 1.3.17
- better "make clean"
- removed references to Red Hat Linux
- added testsuite for data layer
- added some module-info entries
- added command line parsing to network-control
- added IPsec to network-cmd
- switched logging to syslog
- do not touch bonding slaves
- better alias handling
- better handling of chroot 
- read *.ko modules also
- handle modules parameter without "="
- create correct SPI_ identifier for manual IPsec keying
- better hostname handling
- better profile handling
- fix kernel version parsing
- unknown-flag.xpm for unknown country flags
- fixed TokenRing glade file (bad hash at beginning of file)
- fix the length of IPSec shared keys
- prevent modified status after profile switching
- save dialog, for ipsec deactivation
- PEERDNS defaults to yes
- routing for wireless config dialog
- only display CIPE for kernel < 2.6

* Thu Apr  1 2004 Harald Hoyer <harald@redhat.com> - 1.3.17
- translation updates (119610)

* Thu Mar  4 2004 Harald Hoyer <harald@redhat.com> - 1.3.16
- be more relaxed, when parsing the kernel version (115917)
- fixed removing of Hostname (115795)
- fixed "DevEthernet instance has no attribute 'IPv6Init'" (116375)
- removed save dialog, when switching profiles (107399)
- added generic Initstrings (115768)
- added secure.png logo
- added "-c" parameter for activate/deactivate
- changed hotkeys to avoid double entries
- use new pixmap loading code (only take local paths, if debugging is active)
- moved updateNetworkScripts() to NC_functions.py
- fallback on /etc/sysconfig/network-scripts
- removed /usr/lib/rhs/python from sys.path
- added -? as a command line option
- corrected --root= option for gui
- activate/deactivate buttons always sensitive
- check for ipsec-tools and dynamically display ipsec tab
- no second dialog while activating in system-control-network
- change hosts file on hostname change
- PEERDNS is true, if not configured

* Thu Jan 29 2004 Harald Hoyer <harald@redhat.com> - 1.3.15
- added IPv6 support per device (111377)

* Wed Jan 28 2004 Harald Hoyer <harald@redhat.com> - 1.3.14
- modules.conf -> modprobe.conf

* Thu Dec 18 2003 Harald Hoyer <harald@redhat.de> 1.3.13-2
- added mkinstalldirs to EXTRA_DIST
- added version to provides

* Wed Dec 17 2003 Harald Hoyer <harald@redhat.de> 1.3.13
- fixed T-Online dialog #110911
- default flow control to CTSRTS #110347
- only clear login/pw on provider select, if provider has its own number
- fixed cancel of dialup process #103421
- default to "/" for chrooted configuration
- default to "default" profile if none active
- fixed "activate button not active" #110193
- scn-tui requires newt #104213
- fixed #107816, by recognizing /var/run/ppp-ppp<NICKNAME>.pid
- fixed a bug in ISDN activate #100677

* Tue Dec 16 2003 Harald Hoyer <harald@redhat.de> 1.3.12
- renamed redhat-config-network -> system-config-network
- added pciutils requirement
- added utf-8 encoding comments
- corrected some translation strings
- added redhat-config-network provides

* Tue Oct 28 2003 Harald Hoyer <harald@redhat.de> 1.3.10
- removed restriction on t-online password entry #105970
- failsafe changing the error image #108094
- corrected indention #108151

* Mon Oct 27 2003 Harald Hoyer <harald@redhat.de> 1.3.9
- fixed 107501, 107387, 106751, 104213
- fallback to no logfile, if opening the logfile fails
- test, if /etc/{hosts,resolv.conf} exists
- removed ipsec tab

* Thu Oct 23 2003 Than Ngo <than@redhat.com> 1.3.8
- fix a bug in ISDN activate

* Wed Oct 22 2003 Than Ngo <than@redhat.com> 1.3.7-2
- fix a bug in saving of ISDN config file
- add support nickname for ISDN
  
* Wed Oct  8 2003 Harald Hoyer <harald@redhat.de> 1.3.7
- merged in changes from Taroon

* Thu Aug 14 2003 Harald Hoyer <harald@redhat.de> 1.3.6
- fixed #100471

* Wed Aug  6 2003 Harald Hoyer <harald@redhat.de> 1.3.5
- fixed #98251

* Fri Aug  1 2003 Harald Hoyer <harald@redhat.de> 1.3.4
- fixed #101386
- save wireless keys in keys file

* Thu Jul 31 2003 Harald Hoyer <harald@redhat.de> 1.3.3
- fixed #85365
- fixed glade file loading
- more ipsec stuff
- neat can use a "chrooted" environment now (-r)
- .rpmsave will not be loaded
- no interrupt/io settings for PNP cards
- HIGIfied labels
- double click for hardware and ipsec

* Wed Jul  2 2003 Than Ngo <than@redhat.com> 1.3.2-2
- upgrade provide database

* Wed Jun 18 2003 Harald Hoyer <harald@redhat.de> 1.2.12-2
- fixed #97562

* Thu Jun 17 2003 Harald Hoyer <harald@redhat.de> 1.2.12-1
- wlan0 handling
- splash screen bug fixed
- improvements in HW list handling
- isdncard handling #91607

* Thu Jun 12 2003 Harald Hoyer <harald@redhat.de> 1.2.11
- fixed #97027
- fixed subs of -

* Wed Jun 11 2003 Harald Hoyer <harald@redhat.de> 1.2.10
- fixed #97027 #96994
- fixed fedora bugzilla issues #326
- update of some translations

* Wed Jun  4 2003 Harald Hoyer <harald@redhat.de> 1.2.8
- lazy file unlinking
- fixed #91620 #91583
- ConfEHosts -> ConfFHosts

* Mon May 19 2003 Harald Hoyer <harald@redhat.de> 1.2.7
- make PAP/CHAP work again
- route files chmod(0644)
- added local variables to traceback

* Thu May 01 2003 Harald Hoyer <harald@redhat.de> 1.2.6
- use unsernetctl instead of ifdown/ifup

* Thu May 01 2003 Harald Hoyer <harald@redhat.de> 1.2.5
- fixed early import of plugins

* Wed Apr 30 2003 Harald Hoyer <harald@redhat.de> 1.2.4-3
- fixed #89915 and #89916

* Tue Apr 29 2003 Harald Hoyer <harald@redhat.de> 1.2.4-1
- 1.2.4 bugfix release

* Wed Apr  2 2003 Harald Hoyer <harald@redhat.de> 1.2.3-3
- Bugfix release for 9
- fixed #85011, #85703, #85653, #84956, #83640, #68169, #86476, #78043, #77763

* Fri Feb 21 2003 Harald Hoyer <harald@redhat.de> 1.2.0-2
- bump to 1.2.0
- fixed #84725
- warning for #84752

* Fri Feb 12 2003 Harald Hoyer <harald@redhat.de> 1.1.97-1
- fixed #83692
- updated documentation

* Mon Feb  3 2003 Harald Hoyer <harald@redhat.de> 1.1.94-1
- base -> tui, gui -> base

* Thu Jan 30 2003 Harald Hoyer <harald@redhat.de> 1.1.93-1
- 1.1.93

* Wed Jan 29 2003 Harald Hoyer <harald@redhat.de> 1.1.92-1
- 1.1.92

* Tue Jan 14 2003 Harald Hoyer <harald@redhat.de> 1.1.90-1
- 1.1.90

* Thu Dec 19 2002 Than Ngo <than@redhat.com>
- import ConfDevice

* Mon Dec 16 2002 Harald Hoyer <harald@redhat.de>
- 1.1.86

* Fri Dec 13 2002 Harald Hoyer <harald@redhat.de>
- 1.1.85

* Wed Dec 11 2002 Elliot Lee <sopwith@redhat.com> 1.1.80-1
- Remove unpackaged files

* Mon Sep  2 2002 Than Ngo <than@redhat.com> 1.1.20-1
- don't crash by selecting provider
- Set correct HangupTimeout for ISDN connection

* Sat Aug 31 2002 Preston Brown <pbrown@localhost.localdomain>
- fix typo in error dialog function

* Thu Aug 22 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.1.17-1
- Make it use the gnome help system, add yelp as a dependency (#71857)
- Traceback fix: # 72581
- translation updates

* Wed Aug 14 2002 Harald Hoyer <harald@redhat.de>
- #71448
- #71265
- #70988

* Tue Aug 13 2002 Harald Hoyer <harald@redhat.de> 1.1.15-1
- many bugfixes, including  #71062 #69333 #68793 #69133

* Thu Aug  1 2002 Than Ngo <than@redhat.com> 1.1.14-1
- set correct device type for rawip ISDN connections (bug #69568)
- add some ISPs for Austria

* Tue Jul 30 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.1.13-1
- Fixes to the traceback dialog (fix "save to floppy" (we don't do that),
  add i18n.)
- Fix traceback with malformed /etc/hosts (#69320)
- Fix dependencies (#69990)
- Some minor userhelper fixes

* Thu Jul 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.1.12-1
- doc loc fixes (images)
- add pam_timestamp support (#69869)

* Wed Jul 24 2002 Harald Hoyer <harald@redhat.de>
- renamed "default" profile in GUI
- fixed device renaming in profiles

* Wed Jul 24 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.1.10-1
- More bugfixes, including #69635 #69636
- Updated docs

* Tue Jul 23 2002 Harald Hoyer <harald@redhat.de> 1.1.9-1
- lots of bugfixes again :)

* Wed Jul 17 2002 Harald Hoyer <harald@redhat.de>
- lots of bugfixes
- reactivated profile gui

* Mon Jul  8 2002 Harald Hoyer <harald@redhat.de>
- lots of bugfixes, new .desktop stuff
- added desktop-file-utils BuildRequires

* Tue Jul  2 2002 Harald Hoyer <harald@redhat.de> 1.1.7-1
- cleanup, usability

* Mon Jul 01 2002 Than Ngo <than@redhat.com> 1.1.6-1
- get rid of isdnup userisdnctl, both are now part of isdn4k-utils

* Thu Jun 27 2002 Harald Hoyer <harald@redhat.de> 1.1.5-1
- many bug fixes due to gtk2 conversion
- fixed #67273 #66200 #65185 #65073 #63963

* Wed Jun 26 2002 Preston Brown <pbrown@redhat.com>
- ethtool, pcmcia, wireless improvements

* Sat Jun 22 2002 Than Ngo <than@redhat.com> 1.1.4-1
- fixed traceback bug in activate
- some fixes in glade file

* Sun Jun 16 2002 Than Ngo <than@redhat.com> 1.1.3-1
- get_pixbuf: if no icon was not found, looks the icons
  in standard icon directory
- bug fixes in wireless

* Wed Jun 12 2002 Harald Hoyer <harald@redhat.de> 1.1.2-1
- lots of i18n and migration changes
- wireless reactivated

* Fri Jun 07 2002 Than Ngo <than@redhat.com> 1.1.1-1
- set PPPOE_TIMEOUT=80 as default, it should be about 4 times
  the LCP_INTERVAL (bug #64903)

* Wed May 29 2002 Harald Hoyer <harald@redhat.de>
- ported to python2, gtk2, gnome2

* Wed Apr 17 2002 Trond Eivind Glomsrød <teg@redhat.com> 
- Turn off wireless. It doesn't work with all modes, all cards
 and you can't edit IP settings after the initial attempt

* Wed Apr 17 2002 Harald Hoyer <harald@redhat.com> 1.0.0-1
- moved ethmodule.so to /usr/lib
- call it 1.0.0

* Tue Apr 16 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.30-1
- Updated translations
- Updated docs

* Tue Apr 16 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.28-1
- more fixes

* Mon Apr 15 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.27-1
- Update translations, more fixes

* Mon Apr 15 2002 Harald Hoyer <harald@redhat.com> 0.9.26-1
- The Most Fixes (tm)

* Sat Apr 13 2002 Than Ngo <than@redhat.com> 0.9.25-1
- More fixes

* Thu Apr 11 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.24-1
- More fixes (#63177,#57064,#63207)

* Tue Apr 09 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.23-1
- more fixes 
- updated translations

* Thu Apr 04 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.22-1
- more fixes, including #62697,

* Sat Mar 30 2002 Than Ngo <than@redhat.com> 0.9.21-1
- add Token Ring/Wireless/Cipe Druids
- more fixes

* Wed Mar 26 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.20-1
- Rebuild... it should have more fixes

* Wed Mar 26 2002 Than Ngo <than@redhat.com> 0.9.19-1
- add functions for status/activate/deactivate in neat
- more fixes

* Sat Mar 16 2002 Than Ngo <than@redhat.com> 0.9.18-1
- add userisdnctl for ISDN
- more fixes

* Thu Mar 14 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.17-1
- Even more fixes

* Thu Mar 14 2002 Than Ngo <than@redhat.com> 0.9.16-1
- various fixes

* Thu Mar 14 2002 Than Ngo <than@redhat.com> 0.9.15-1
- add desktop file for neat-control
- various fixes, additions

* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.14-1
- Require gnome-core, buildrequire gnome-core-devel

* Mon Mar 11 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.13-1
- New build
- No longer noarch

* Thu Feb 28 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.12-1
- Various fixes, additions

* Tue Jan 29 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.11-1
- build in new environment

* Mon Jan 07 2002 Than Ngo <than@redhat.com> 0.9.10.1-1
- fixed bug #57853

* Tue Dec 03 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.9.10-1
- minor fixes, more translations

* Mon Nov 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.9.9-0.1
- Trying again, with more fixes :)

* Fri Nov 25 2001 Than Ngo <than@redhat.com> 0.9.8-0.6
- fixed bug #56145, #56146, #56147

* Tue Nov 20 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.9.8-0.5
- prepare for errata

* Fri Nov 02 2001 Than Ngo <than@redhat.com> 0.9.7-1
- fixed 'AVM PnP'/'Sedlbauer Speed Fax+ PnP'/'ASUS Com ISDNLink ISA PnP'
- update provider DB

* Tue Oct 30 2001 Than Ngo <than@redhat.com> 0.9.7-1
- allow setting AVM PCI (Fritz!PCI v2) if kernel supports it
- fixed some typo bugs

* Wed Oct 24 2001 Harald Hoyer <harald@redhat.com> 0.9.6-1
- seperated gui from data layer
- make .pyc ghost files
- fixed profile/alias problem
- modem probing only once

* Mon Oct 22 2001 Harald Hoyer <harald@redhat.com> 0.9.5-1
- fixed consolehelper
- added chars [_-] ro nickname pattern
- added traceback catching dialog

* Wed Oct 17 2001 Harald Hoyer <harald@redhat.com> 0.9.4-1
- fixed /etc/hosts
- fixed pap/chap
- fixed 'save changes?'

* Tue Oct 16 2001 Than Ngo <than@redhat.com> 0.9.3-1
- fix internet-druid fails (bug #54192)
- fix dial on demand problem from some ISDN Provider in German
- don't trace back if length of Login name is 2 (bug #54322)

* Thu Sep 27 2001 Than Ngo <than@redhat.com> 0.9.2-1
- enable TCPIP for CIPE
- show device Tab as default if devices exist

* Wed Sep 12 2001 Than Ngo <than@redhat.com> 0.9.1-1
- add CTC and IUCV support for s390/s390x
- disable Dialup on s390/s390x

* Thu Sep  5 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.9-1
- Add Russian

* Wed Sep  4 2001 Phil Knirsch <phil@redhat.de> 0.8.4-1
- Fixed problem with unwanted removal of entries in /etc/modules.conf (#53042)

* Mon Sep  3 2001 Than Ngo <than@redhat.com> 0.8.3-1
- fix a bug in setting Authentication
- fix some critical typo bugs

* Fri Aug 31 2001 Than Ngo <than@redhat.com> 0.8.2-1
- fix backtrace bug in CIPE
- fix traceback bug if self.device.Dialup is None
- if hardware is deleted, remove all devices used this hardware
- de.po: fix bad translation

* Fri Aug 31 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.8.1-1
- Add support for Czech

* Fri Aug 31 2001 Than Ngo <than@redhat.com>
- fix #52920, #52922, #52914, #52916, #52917

* Fri Aug 31 2001 Phil Knirsch <phil@redhat.de> 0.8.0-2
- Fixed wrong option handling in /etc/modules.conf (#52853, #52923)
- Fixed empty search entry in /etc/resolv.conf (#52926)
- Fixed empty domain entry in /etc/resolv.conf (#52924)
- Fixed ethernet hardware probing traceback (#52921)

* Tue Aug 28 2001 Than Ngo <than@redhat.com> 0.8.0-1
- fix some typo bugs

* Tue Aug 28 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.7.10-1
- minor fixes, including bootprotocol for CIPE (don't say it will use DHCP...)

* Tue Aug 28 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.7.9-1
- Not everything was marked for translation (#52650)

* Tue Aug 28 2001 Than Ngo <than@redhat.com> 0.7.8-1
- fix some typo bugs
- fix wrong Modem entry (Bug #52601)

* Mon Aug 27 2001 Than Ngo <than@redhat.com> 0.7.7-1
- fix wrong type CBHUP

* Mon Aug 27 2001 Phil Knirsch <phil@redhat.de> 0.7.6-2
- Fixed use of /etc/sysconfig/network (#52359)

* Fri Aug 24 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.7.6-1
- Reordered tabs, added descriptions on each of the tabs

* Fri Aug 24 2001 Bill Nottingham <notting@redhat.com> 0.7.5-1
- tokenring support

* Thu Aug 23 2001 Phil Knirsch <phil@redhat.de> 0.7.4-2
- Fixed recalculation of BROADCAST and NETWORK values if IP and netmask are
  present (#51462)

* Mon Aug 20 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.7.4-1
- More bugfixes, among them #51929, #51991, #51721, #51722,
  partial #52044, #51720. 
- Updated translations, include more languages

* Thu Aug 16 2001 Phil Knirsch <phil@redhat.de> 0.7.3-2
- Fixed major bug in device renaming (#50885)

* Tue Aug 14 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.7.3-1
- more bugfixes, more docs, GUI fixes

* Fri Aug 10 2001 Than Ngo <than@redhat.com> 0.7.2-1
- more bugfixes

* Fri Aug 10 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.7.1-1
- more bugfixes, more docs

* Wed Aug  8 2001 Alexander Larsson <alexl@redhat.com> 0.7-2
- Install desktop files in sysconfig instead of serverconf.

* Wed Aug  8 2001 Phil Knirsch <phil@redhat.de> 0.7-1
- Added a lot of documentation
- Final changes to the Modem druid dialog and code to look just like the
  hardware add dialog for modems.

* Wed Aug  8 2001 Phil Knirsch <phil@redhat.de> 0.6.8-3
- Added the modem detection for the ModemDruid.
- Added kudzu as requirement as it is needed for modem detection.
- For compatibility still check for symlinks, too. Otherwise older setups will
  break.

* Tue Aug  7 2001 Phil Knirsch <phil@redhat.de> 0.6.7-2
- Fixed various important bugzilla bugs
- Added and implemented the add Hardware dialog.
- Added a working Apply button.
- Switched to using hardlinks instead of symlinks for config files.

* Tue Aug  7 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.6.7-1
- Add online help capability (#50739)

* Mon Aug  6 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.6.6-1
- Disable profiles in GUI and as necesarry in code

* Mon Aug  6 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.6.5-1
- more bugfixes
- add Conf.py from pythonlib, which has gone to the great bitbucket
  in the sky

* Sun Aug  5 2001 Than Ngo <than@redhat.com>
- fix bug 50740
- wvdial.conf readonly for root

* Fri Aug  3 2001 Than Ngo <than@redhat.com>
- fix pap/chap Login name for T-online
- fix InitStrings
- use gettext function in NC_functions
- fix loading DEFROUTE/PERSIST/DEMAND/IDLETIMEOUT for Modem dialup
- don't backtrace if 'SetVolume' and 'Dial Command' are not defined

* Thu Aug 02 2001 Phil Knirsch <phil@redhat.de> 0.6.1-2
- Fixed buggous removal of ifcfg-lo (#50478)
- Fixed problems with modem volume in hardware dialog
- Fixed missing /dev/modem for modem setup (#50673)

* Wed Aug  2 2001 Yukihiro Nakai <ynakai@redhat.com>
- POTFILES.in list up fix
- Add Japanese translation

* Wed Aug 02 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.6.2-1
- More bugfixes

* Tue Jul 24 2001 Than Ngo <than@redhat.com> 0.6.1-1
- Some more bugfixes...

* Tue Jul 24 2001 Phil Knirsch <phil@redhat.de> 0.6-2
- Some more bugfixes...

* Tue Jul 24 2001 Phil Knirsch <phil@redhat.de> 0.6-1
- Bumped version to 0.6

* Tue Jul 24 2001 Than Ngo <than@redhat.com>
- add Druid for dialup connection (ISDN/ADSL/Modem)

* Thu Jul 19 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Obsolete netcfg - rp3 is next, when gnome-lokkit doesn't require
  it anymore
- More fixes...

* Tue Jul 17 2001 Trond Eivind Glomsrød <teg@redhat.com>
- CIPE and wireless added

* Mon Jul 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add i18n
- Many minor fixes...

* Wed Jul 11 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Don't run autogen.sh
- Mark files in /etc as configuration files
- Multiple fixes to automake files
- Add Norwegian translation to desktop files
- install into the configuration tool desktop directory

* Wed Jul 11 2001 Than Ngo <than@redhat.com> 0.3.1-1
- obsolete isdn-config internet-config
- requires consolehelper, alchemist
- add icon and desktop file
- use bzip2

* Wed Jul 11 2001 Phil Knirsch <phil@redhat.de> 0.3.0-2
- Fixed critical problem during profile saving.

* Wed Jul 10 2001 Phil Knirsch <phil@redhat.de> 0.3.0-1
- 0.3.0-1
- Final touches for beta2. Most stuff should work now.

* Thu Jul 10 2001 Phil Knirsch <phil@redhat.de> 0.2.2-2
- Added some missing files.

* Tue Jul 10 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 0.2.2

* Tue Jul 10 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 0.2.1

* Mon Jul  9 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 0.2
- New name - system-config-network. 
  Shortcut: neat (NEtwork Administration Tool)

* Fri Jul 06 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Require a recent version of initscripts
- Initial build. Don't obsolete older tools just yet...
