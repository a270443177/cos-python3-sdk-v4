#!/usr/bin/env python
# -*- coding: utf-8 -*-
from qcloud_cos.cos_client import CosClient
from qcloud_cos.cos_client import *
from qcloud_cos.cos_client import *
from qcloud_cos.cos_request import UploadFileRequest
from qcloud_cos.cos_request import UploadSliceFileRequest
from qcloud_cos.cos_request import UpdateFileRequest
from qcloud_cos.cos_request import UpdateFolderRequest
from qcloud_cos.cos_request import DelFolderRequest
from qcloud_cos.cos_request import DelFileRequest
from qcloud_cos.cos_request import CreateFolderRequest
from qcloud_cos.cos_request import StatFileRequest
from qcloud_cos.cos_request import StatFolderRequest
from qcloud_cos.cos_request import ListFolderRequest
from qcloud_cos.cos_request import DownloadFileRequest
from qcloud_cos.cos_request import MoveFileRequest
from qcloud_cos.cos_auth import Auth
from qcloud_cos.cos_cred import CredInfo


import logging

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
