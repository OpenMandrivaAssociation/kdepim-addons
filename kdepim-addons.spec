Summary:	Add-Ons for the KDE PIM suite
Name:		kdepim-addons
Version:	16.08.3
Release:	2
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	sasl-devel
BuildRequires:	boost-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5GAPI)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5AkonadiNotes)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5MailCommon)
BuildRequires:	cmake(KF5KaddressbookGrantlee)
BuildRequires:	cmake(KF5MessageViewer)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5GrantleeTheme)
BuildRequires:	cmake(KF5PimCommon)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(KF5IncidenceEditor)
BuildRequires:	cmake(KF5MessageCore)
BuildRequires:	cmake(KF5MessageComposer)
BuildRequires:	cmake(KF5MessageList)
BuildRequires:	cmake(KF5CalendarSupport)
BuildRequires:	cmake(KF5EventViews)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5Gravatar)
BuildRequires:	cmake(KF5Tnef)
BuildRequires:	pkgconfig(shared-mime-info)
Conflicts:	kmail <= 3:16.04.3-2

%description
Add-Ons for the KDE PIM suite.

%files
%config %{_sysconfdir}/xdg/kdepim-addons.categories
%config %{_sysconfdir}/xdg/kmail.antispamrc
%config %{_sysconfdir}/xdg/kmail.antivirusrc
%{_bindir}/kmail_antivir.sh
%{_bindir}/kmail_clamav.sh
%{_bindir}/kmail_fprot.sh
%{_bindir}/kmail_sav.sh
%{_libdir}/akonadi/contact/editorpageplugins/cryptopageplugin.so
# (tpg) these libs should be splitted into separate subpackages ?
%{_libdir}/libkaddressbookmergelibprivate.so.5*
%{_libdir}/libshorturlpluginprivate.so.5*
%{_libdir}/libadblocklibprivate.so.5*
%{_libdir}/qt5/plugins/kaddressbook/*.so
%{_libdir}/qt5/plugins/kmail/*.so
%{_libdir}/qt5/plugins/korg_datenums.so
%{_libdir}/qt5/plugins/korg_hebrew.so
%{_libdir}/qt5/plugins/korg_picoftheday.so
%{_libdir}/qt5/plugins/korg_thisdayinhistory.so
%{_libdir}/qt5/plugins/messageviewer/*.so
%{_libdir}/qt5/plugins/messageviewer_bodypartformatter_application_mstnef.so
%{_libdir}/qt5/plugins/messageviewer_bodypartformatter_text_calendar.so
%{_libdir}/qt5/plugins/messageviewer_bodypartformatter_text_vcard.so
%{_libdir}/qt5/plugins/messageviewer_bodypartformatter_text_xdiff.so
%{_libdir}/qt5/plugins/pimcommon/*.so
%{_libdir}/qt5/plugins/plasmacalendarplugins/*.so
%{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents/PimEventsConfig.qml
%{_libdir}/qt5/plugins/webengineviewer/*.so
%{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/libpimcalendarsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/qmldir
%{_datadir}/kmail2/pics/*
%{_datadir}/kservices5/korganizer/datenums.desktop
%{_datadir}/kservices5/korganizer/hebrew.desktop
%{_datadir}/kservices5/korganizer/picoftheday.desktop
%{_datadir}/kservices5/korganizer/thisdayinhistory.desktop
%{_datadir}/messageviewer/defaultthemes/*/*
%{_datadir}/messageviewer/plugins/bodypartformatter/*.desktop
%{_datadir}/kconf_update/webengineurlinterceptoradblock.upd

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
