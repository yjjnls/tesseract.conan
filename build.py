#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_default
import os

if __name__ == "__main__":
    CONAN_USERNAME = os.environ.get("CONAN_USERNAME")
    CONAN_UPLOAD = 'https://api.bintray.com/conan/%s/%s' % (CONAN_USERNAME,
                                                            'stable')
    os.environ['CONAN_UPLOAD'] = CONAN_UPLOAD
    os.environ['CONAN_CHANNEL'] = 'stable'
    os.environ['CONAN_UPLOAD_ONLY_WHEN_STABLE'] = 'False'

    builder = build_template_default.get_builder()

    builder.run()
