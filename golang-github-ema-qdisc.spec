%bcond_without check
%global goipath     github.com/ema/qdisc
%global commit      b307c22d3ce761d351b6e6270b50195b44ee9248
Version:            0

%global common_description %{expand:
Package qdisc allows to get queuing discipline information via netlink,
similar to what tc (from iproute2) does.}

%gometa

Name:    %{goname}
Release: 0.2%{?dist}
Summary: qdisc allows to get queuing discipline information via netlink
License: MIT
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(github.com/mdlayher/netlink)

%description
%{common_description}

%package   devel
Summary:   %{summary}

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q
rm -rf vendor

%install
%goinstall

%check
%if %{with check}
  # Tests fail on s390x possibly due to endianess, for more info
  # See: https://github.com/mdlayher/netlink/issues/77
  %ifnarch s390x
    %gochecks
  %endif
%endif

%files devel -f devel.file-list
%license LICENSE.md
%doc *\.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitb307c22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Paul Gier <pgier@redhat.com> - 0-0.1.20180508gitb307c22
- First package for Fedora

