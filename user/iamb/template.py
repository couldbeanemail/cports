pkgname = "iamb"
pkgver = "0.0.11"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
# Build can use git for version generation, but is unused since the tar archive
# doesn't include .git. Doesn't make a lot of sense for releases.
makedepends = ["rust-std", "sqlite-devel"]
pkgdesc = "Matrix chat client that uses Vim keybindings"
license = "Apache-2.0"
url = "https://iamb.chat"

# No release : waiting for the world to end.
# source = f"https://github.com/ulyssa/iamb/archive/refs/tags/v{pkgver}.tar.gz"
# sha256 = "f628cfbd9eba9e8881902b970e9432fec815044ec9bea901a8562ea3ef8f4615"
source="https://github.com/ulyssa/iamb/archive/a32149f60413736e797723582fca49c991b8edcd.tar.gz"
sha256 = "d76a23eab444d62c531bc9a4b78dce008aa03841b0eec6442a45c387f7974a9b"

def install(self):
    self.install_license("LICENSE")
    self.install_bin(f"target/{self.profile().triplet}/release/iamb")
    self.install_man("docs/iamb.1")
    self.install_man("docs/iamb.5")
    self.install_file(
        "config.example.toml", "usr/share/iamb", name="config.toml"
    )
