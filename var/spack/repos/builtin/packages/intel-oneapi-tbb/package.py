# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *

releases = {
    '2021.1.1': {'irc_id': '17378', 'build': '119'}}


class IntelOneapiTbb(IntelOneApiLibraryPackage):
    """Intel oneAPI TBB."""

    maintainers = ['rscohn2']

    homepage = 'https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onetbb.html'

    version('2021.1.1', sha256='535290e3910a9d906a730b24af212afa231523cf13a668d480bade5f2a01b53b', expand=False)

    provides('tbb')

    def __init__(self, spec):
        self.component_info(dir_name='tbb',
                            components='intel.oneapi.lin.tbb.devel',
                            releases=releases,
                            url_name='tbb_oneapi')
        super(IntelOneapiTbb, self).__init__(spec)

    def _join_prefix(self, path):
        return join_path(self.prefix, 'tbb', 'latest', path)

    def _ld_library_path(self):
        dirs = ['lib/intel64/gcc4.8']
        for dir in dirs:
            yield self._join_prefix(dir)

    def _library_path(self):
        dirs = ['lib/intel64/gcc4.8']
        for dir in dirs:
            yield self._join_prefix(dir)

    def setup_run_environment(self, env):
        for dir in self._library_path():
            env.prepend_path('LIBRARY_PATH', dir)
        for dir in self._ld_library_path():
            env.prepend_path('LD_LIBRARY_PATH', dir)
        env.set('TBBROOT', join_path(self.prefix, 'tbb', 'latest'))
