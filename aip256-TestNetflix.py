
# ------- # imports # -------

from io	import StringIO
import re
from unittest import main, TestCase

from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve, calculate_rsme, compile_prediction_and_actual

# -----------
# TestCollatz
# -----------

class TestNetflix (TestCase) :

	# ----
	# read
	# ----

	def test_read_1 (self):
		r	= StringIO("")
		i = netflix_read(r)
		self.assertEqual(i,None)

	def test_read_2 (self):
		r	= StringIO("1:\n")
		i = netflix_read(r)
		self.assertEqual(i,"1:")

	def test_read_3 (self):
		r	 = StringIO("1:\n30878")
		i = netflix_read(r)
		self.assertEqual(i,"1:")

	def test_read_4 (self):
		r	 = StringIO("a")
		i = netflix_read(r)
		self.assertEqual(i,None)

	def test_read_5 (self):
		r	 = StringIO("\n")
		i = netflix_read(r)
		self.assertEqual(i,None)

	# ----
	# eval
	# ----

	def test_eval_1 (self):
		v = netflix_eval(1,30878)
		t = v > 5 or v < 1
		self.assertFalse(t)

	def test_eval_2 (self):
		v = netflix_eval(17770,54864)
		t = v > 5 or v < 1
		self.assertFalse(t)

	def test_eval_3 (self):
		v = netflix_eval(17767,745667)
		t = v > 5 or v < 1
		self.assertFalse(t)

	# -----
	# solve
	# -----

	def test_solve_1 (self) :
		r = StringIO("")
		w = StringIO()
		netflix_solve(r, w)
		self.assertEqual(w.getvalue(), "1:\n")

	def test_solve_2 (self) :
		r = StringIO("1:")
		w = StringIO()
		netflix_solve(r, w)
		self.assertEqual(w.getvalue(), "1:\n")

	def test_solve_3 (self):
		r = StringIO("1:\n30878")
		w = StringIO()
		netflix_solve(r, w)
		regexRmse = re.compile("1:\n4\nRMSE: .*")
		self.assertTrue(regexRmse.match(w.getvalue()))

	def test_solve_4 (self):
		r = StringIO("1:\n30878\n6:\n1064641")
		w = StringIO()
		netflix_solve(r, w)
		regexRmse = re.compile("1:\n4\n6:\n3\nRMSE: .*")
		self.assertTrue(regexRmse.match(w.getvalue()))

	def test_solve_5 (self):
		r = StringIO("1:\n30878\n6:\n7:")
		w = StringIO()
		netflix_solve(r, w)
		regexRmse = re.compile("1:\n4\n6:\n7:\nRMSE: .*")
		self.assertTrue(regexRmse.match(w.getvalue()))

	def test_solve_6 (self):
		r = StringIO("1:\n6:\n7:")
		w = StringIO()
		netflix_solve(r, w)
		self.assertEqual(w.getvalue(), "1:\n6:\n7:\n")

	# -----
	# print
	# -----

	def test_print (self) :
		w = StringIO()
		netflix_print(w, 1)
		self.assertEqual(w.getvalue(), "1\n")

	# -----
	# calculate_rsme
	# -----

	def test_rmse_1(self):
		v = calculate_rsme([1,1,1],[2,2,2])
		self.assertEqual(v,1)

	def test_rmse_2(self):
		v = calculate_rsme([1,1,1],[1,1,1])
		self.assertEqual(v,0)

	def test_rmse_3(self):
		v = calculate_rsme([1,1,1,1],[2,2,2])
		self.assertNotEqual(v,1)

	def test_rmse_4(self):
		v = calculate_rsme([],[])
		self.assertEqual(v,None)

	def test_rmse_5(self):
		v = calculate_rsme([1,5,1],[5,1,5])
		self.assertEqual(v,4)

	def test_rmse_6(self):
		v = calculate_rsme([],[1])
		self.assertEqual(v,None)

	def test_rmse_7(self):
		v = calculate_rsme([1],[])
		self.assertEqual(v,None)

	# -----
	# compile_prediction_and_actual
	# -----

	def test_compile_prediction_and_actual_1(self):
		v = compile_prediction_and_actual({1: {2: 1, 4: 2}}, {1: {4: 1, 2: 2}})
		self.assertEqual(v, {"prediction":[1,2],"actual":[2,1]})

	def test_compile_prediction_and_actual_2(self):
		v = compile_prediction_and_actual({1: {2: 3, 4: 5}, 2: {4: 5, 1: 1}}, {1: {2: 1, 4: 4}, 2: {4: 2, 1: 1}})
		self.assertEqual(v, {"prediction":[3,5,1,5],"actual":[1,4,1,2]})

	# ----
	# main
	# ----

main()