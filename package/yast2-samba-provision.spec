#
# spec file for package yast2-samba-provision
#
# Copyright (c) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           yast2-samba-provision
Version:        1.0.3
Release:        0
Summary:        YaST2 - Samba AD DC provision
Group:          System/YaST
License:        GPL-2.0
Url:            https://github.com/yast/yast-samba-provision

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  yast2 >= 3.3.8
BuildRequires:  yast2-perl-bindings
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-testsuite
BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files

Requires:       yast2 >= 3.3.8
Requires:       yast2-ruby-bindings >= 3.3.1
Requires:       yast2-python3-bindings >= 4.0.8
Requires:       yast2-network

BuildArch:      noarch

%description
This package contains the YaST2 component to configure samba as an Active
Directory Domain Controller.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}

%changelog
