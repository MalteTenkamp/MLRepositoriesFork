#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:11:15 2017

@author: msuzen

%load_ext autoreload
%autoreload 2

"""

import unittest
import bristol.ensembles as ensembles
import numpy as np

class test_n_eigen_circular2(unittest.TestCase):

      epsilon = 1e-9

      def test_n_eigen_circular2_01(self):
          mseed   = 2963416
          e_cue   = ensembles._n_eigen_circular2(
                                                 seed=mseed, 
                                                 N=5,
                                                 size=1,
                                                 ensemble='CUE', 
                                                 set_seed=True
                                                )  
          e_coe   = ensembles._n_eigen_circular2(
                                                 seed=mseed, 
                                                 N=10,
                                                 size=1,
                                                 ensemble='COE', 
                                                 set_seed=True
                                                )   
          e_cse   = ensembles._n_eigen_circular2(
                                                 seed=mseed, 
                                                 N=15,
                                                 size=1,
                                                 ensemble='CSE', 
                                                 set_seed=True
                                                )   
          n_cue   = np.imag(e_cue['c_eigen']).sum()
          n_coe   = np.imag(e_coe['c_eigen']).sum()
          n_cse   = np.imag(e_cse['c_eigen']).sum()
          self.assertTrue(n_cue+0.70246404091524939 < self.epsilon)
          self.assertTrue(n_coe-0.02388152067472389 < self.epsilon)
          self.assertTrue(np.abs(n_cse)< self.epsilon)
          
          
      def test_n_eigen_circular2_02(self):
          mseed   = 2963416
          e_cue   = ensembles._n_eigen_circular2(
                                                 seed=mseed, 
                                                 N=5,
                                                 size=3,
                                                 ensemble='CUE', 
                                                 set_seed=True
                                                )
          e_coe   = ensembles._n_eigen_circular2(
                                                 seed=mseed, 
                                                 N=10,
                                                 size=3,
                                                 ensemble='COE', 
                                                 set_seed=True
                                                )   
          e_cse   = ensembles._n_eigen_circular2(
                                                 seed=mseed, 
                                                 N=15,
                                                 size=3,
                                                 ensemble='CSE', 
                                                 set_seed=True
                                                )   
          n_cue   = np.imag(e_cue['c_eigen']).sum()
          n_coe   = np.imag(e_coe['c_eigen']).sum()
          n_cse   = np.imag(e_cse['c_eigen']).sum()
          self.assertTrue(n_cue+2.107392122745748 < self.epsilon)
          self.assertTrue(n_coe-0.071644562024171 < self.epsilon)
          self.assertTrue(np.abs(n_cse) < self.epsilon)   