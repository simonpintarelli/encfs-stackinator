# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Encfs(CMakePackage):
    """ EncFS provides an encrypted filesystem in user-space."""

    homepage = "https://github.com/vgough/encfs"
    url = "https://github.com/vgough/encfs/releases/download/v1.9.5/encfs-1.9.5.tar.gz"

    maintainers("lukasgd", "simonpintarelli")

    version("1.9.5", sha256="4709f05395ccbad6c0a5b40a4619d60aafe3473b1a79bafb3aa700b1f756fd63")
    version("1.9.4", sha256="20656b4ead58ebd8d5f49a5c346b59e70dc2dc31220159e5b5a115bfa1bc40d6")
    version("1.9.3", sha256="7da150aa8e281c1323b07adca8df2bba42a323b10402930a5543d3634f44ea71")
    version("1.9.1", sha256="67203aeff7a06ce7be83df4948db296be89a00cffe1108a0a41c96d7481106a4")
    version("1.9", sha256="30d2db1555ec359082046748d278018b8a246dc49c0442291c5671da0486f4bf")
    version("1.8.1", sha256="8a0257ff500c14244ee99acdd472696966796e2a0931e4a132191f14a666d5d1")

    variant("shared", default=True, description="Build shared libraries")
    variant("lint", default=False, description="enable lint output")
    variant("unit_tests", default=False, description="build unit tets")

    depends_on("libfuse")
    depends_on("openssl")
    depends_on("tinyxml2")

    def cmake_args(self):

        args = [self.define("INSTALL_LIBENCFS", True),
                self.define("USE_INTERNAL_TINYXML", False),
                self.define_from_variant("BUILD_UNIT_TESTS", "unit_tests"),
                self.define_from_variant("BUILD_SHARED_LIBS", "shared")]
        return args
