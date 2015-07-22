from kata import *
import gol_utils as gol
import unittest
import numpy.testing as nt


class TestClass(unittest.TestCase):
	N = 3
	def test_first(self):
		world = gol.create_world([(1,1)], N)
		new_world = evolve_world(world, N)
		control_world = gol.create_world([], N)
		nt.assert_array_equal(new_world,control_world)

	def test_tots_mini(self):
		control_world = gol.create_world([], N)
		for i in range(3):
			for j in range(3):
				world = gol.create_world([(i,j)],N)
				new_world = evolve_world(world,N)
				nt.assert_array_equal(new_world,control_world)

	def test_block(self):
		world = gol.create_world([(1,1),(1,0),(0,1),(0,0)],N)
		new_world = evolve_world(world,N)
		control_world = gol.create_world([],N)
		nt.assert_array_equal(new_world,world)

	def test_semafor(self):
		world = gol.create_world([(1,0),(1,1),(1,2)],N)
		new_world = evolve_world(world,N)
		control_world = gol.create_world([(1,1),(0,1),(2,1)],N)
		nt.assert_array_equal(new_world,control_world)

	def test_toad(self):
		N = 6
		world = gol.create_world([(2,2), (2,3),(2,4),(3,1),(3,2),(3,3)],N)
		new_world = evolve_world(world,N)
		control_world = gol.create_world([(1,3), (2,1),(2,4),(3,1),(3,4),(4,2)],N)
		nt.assert_array_equal(new_world,control_world)

	def test_bacon(self):
		N = 6
		world = gol.create_world([(1,1), (1,2),(2,1),(2,2),(3,3),(3,4),(4,3),(4,4)],N)
		new_world = evolve_world(world,N)
		control_world = gol.create_world([(1,1), (1,2),(2,1),(3,4),(4,3),(4,4)],N)
		nt.assert_array_equal(new_world,control_world)


if __name__ == '__main__':
    unittest.main()

