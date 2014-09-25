#!/usr/bin/env python3

# ------------------------------
# TestNetflix.py
# Brian Gallagher, bg9554
# Viet Mai, vtm239
# ------------------------------


# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_eval, netflix_solve

# -----------
# TestNetflix
# -----------

class TestCollatz (TestCase) :

    # ----
    # eval
    # ----
    
    def test_eval1 (self) :
        user = "2210667"
        movie = "5044"
        guessmia = 3.164285714285714
        w = StringIO()
        netflix_eval(user, movie, w, guessmia)
        self.assertEqual(w.getvalue(), "3.5\n")
        
    def test_eval2 (self) :
        user = "1730746"
        movie = "5048"
        guessmia = 3.9432624113475176
        w = StringIO()
        netflix_eval(user, movie, w, guessmia)
        self.assertEqual(w.getvalue(), "4.5\n")

    def test_eval3 (self) :
        user = "2639803"
        movie = "5050"
        guessmia = 4.091953522781671
        w = StringIO()
        netflix_eval(user, movie, w, guessmia)
        self.assertEqual(w.getvalue(), "4.2\n")

    def test_eval4 (self) :
        user = "435271"
        movie = "505"
        guessmia = 3.1397894736842105
        w = StringIO()
        netflix_eval(user, movie, w, guessmia)
        self.assertEqual(w.getvalue(), "3.5\n")
    
    def test_eval5 (self) :    
        user = "1941872"
        movie = "11545"
        guessmia = 2.7410714285714284
        w = StringIO()
        netflix_eval(user, movie, w, guessmia)
        self.assertEqual(w.getvalue(), "3.7\n")
        
    def test_eval6 (self) :    
        user = "2511359"
        movie = "3435"
        guessmia = 1.989247311827957
        w = StringIO()
        netflix_eval(user, movie, w, guessmia)
        self.assertEqual(w.getvalue(), "2.4\n")
        
    def test_eval7 (self) :    
        user = "2351449"
        movie = "436"
        guessmia = 3.8146341463414632
        w = StringIO()
        netflix_eval(user, movie, w, guessmia)
        self.assertEqual(w.getvalue(), "3.0\n")

    # -----
    # solve
    # -----

    def test_solve1 (self) :
        r = StringIO("5044:\n2210667\n1659535\n5045:\n2351908\n1030037\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "5044:\n3.5\n3.7\n5045:\n3.7\n3.9\nRMSE: 1.22\n")
        
    def test_solve2 (self) :
        r = StringIO("5047:\n2422980\n28439\n5048:\n1730746\n942914\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "5047:\n3.4\n3.5\n5048:\n4.5\n4.0\nRMSE: 1.1\n")

# ----
# main
# ----

main()

"""
% coverage3 run --branch TestNetflix.py >  TestNetflix.out 2>&1



% coverage3 report -m                   >> TestNetflix.out
"""
