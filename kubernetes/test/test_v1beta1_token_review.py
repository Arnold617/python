# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_token_review import V1beta1TokenReview


class TestV1beta1TokenReview(unittest.TestCase):
    """ V1beta1TokenReview unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1TokenReview(self):
        """
        Test V1beta1TokenReview
        """
        model = kubernetes.client.models.v1beta1_token_review.V1beta1TokenReview()


if __name__ == '__main__':
    unittest.main()