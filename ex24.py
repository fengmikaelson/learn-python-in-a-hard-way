# -*- coding: utf-8 -*-
# @Author: fengm
# @Date:   2016-12-02 10:50:07
# @Last Modified by:   fengm
# @Last Modified time: 2016-12-02 11:20:33

print("let's practice everything.")
print('you\'d ned to know \'bout escapes with \\that do \n newline and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none
"""

print("----------")
print(poem)
print("----------")

five=10-2+3-6
print("this should be five:%s"%five)

def secret_formula(started):
	jelly_beans=started*500
	jars=jelly_beans/1000
	crates=jars/100
	return jelly_beans,jars,crates

start_point=10000
beans,jars,crates=secret_formula(start_point)
print("with a starting point of:%d"%start_point)
print("we'd have %d beans,%d jars, and %d crates."%(beans,jars,crates))

start_point=start_point/10

print("we can also do that this way")
print("we'd have %d beans,%d jars,and %d crates."%secret_formula(start_point))