graffle_figures := figures/adder-example1.pdf \
	figures/adder-example2.pdf \
	figures/adder-example3.pdf

figures/adder-example1.pdf:midas-graphics/graffle/adder-example.graffle
	omnigraffle-export -c initial-state midas-graphics/graffle/adder-example.graffle figures/adder-example1.pdf

figures/adder-example2.pdf:midas-graphics/graffle/adder-example.graffle
	omnigraffle-export -c tfire-cycle0 midas-graphics/graffle/adder-example.graffle figures/adder-example2.pdf

figures/adder-example3.pdf:midas-graphics/graffle/adder-example.graffle
	omnigraffle-export -c cycle1 midas-graphics/graffle/adder-example.graffle figures/adder-example3.pdf
