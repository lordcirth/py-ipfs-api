# -*- coding: utf-8 -*-
from __future__ import absolute_import

from . import base

from .. import multipart


class Section(base.SectionBase):
	"""
	Functions used to manage objects in IPFS's Merkle Directed Acyclic Graph.
	"""

	def get(self, **kwargs):
		"""
		Get and serialize the DAG node named by multihash.
		
		Parameters
		----------
		multihash : str
		"""
		pass
