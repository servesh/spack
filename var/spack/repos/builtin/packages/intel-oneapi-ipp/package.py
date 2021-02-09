# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *

releases = {
    '2021.1.1': {'irc_id': '17436', 'build': '47'}}


class IntelOneapiIpp(IntelOneApiLibraryPackage):
    """Intel oneAPI IPP."""

    maintainers = ['rscohn2']

    homepage = 'https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/ipp.html'

    version('2021.1.1', sha256='2656a3a7f1f9f1438cbdf98fd472a213c452754ef9476dd65190a7d46618ba86', expand=False)

    provides('ipp')

    def __init__(self, spec):
        self.component_info(dir_name='ipp',
                            components='intel.oneapi.lin.ipp.devel',
                            releases=releases,
                            url_name='ipp_oneapi')
        super(IntelOneapiIpp, self).__init__(spec)
