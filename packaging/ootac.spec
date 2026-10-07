Name:           ootac
Version:        0.1.0
Release:        1%{?dist}
Summary:        Reverses files line by line using fast backwards seek and ring buffer scanning.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootac
Source0:        ootac-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootac is a sovereign, capability-bounded FILE INVERTER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootac
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootac-uninstall

%files
/usr/bin/ootac
/usr/bin/ootac-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
