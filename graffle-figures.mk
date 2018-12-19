graffle_figures := figures/target-graph.pdf \
	figures/mapped-simulator.pdf \
	figures/memory-model-block-diagram.pdf \
	figures/model-operation-1.pdf \
	figures/model-operation-2.pdf \
	figures/model-operation-3.pdf \
	figures/model-operation-4.pdf

figures/target-graph.pdf:midas-graphics/graffle/masters-target.graffle
	omnigraffle-export -c target-graph midas-graphics/graffle/masters-target.graffle figures/target-graph.pdf

figures/mapped-simulator.pdf:midas-graphics/graffle/masters-target.graffle
	omnigraffle-export -c f1 midas-graphics/graffle/masters-target.graffle figures/mapped-simulator.pdf

figures/memory-model-block-diagram.pdf:midas-graphics/graffle/memory-model-block-diagram.graffle
	omnigraffle-export -c full midas-graphics/graffle/memory-model-block-diagram.graffle figures/memory-model-block-diagram.pdf

figures/model-operation-1.pdf:midas-graphics/graffle/memory-model-operation.graffle
	omnigraffle-export -c 1 midas-graphics/graffle/memory-model-operation.graffle figures/model-operation-1.pdf

figures/model-operation-2.pdf:midas-graphics/graffle/memory-model-operation.graffle
	omnigraffle-export -c 2 midas-graphics/graffle/memory-model-operation.graffle figures/model-operation-2.pdf

figures/model-operation-3.pdf:midas-graphics/graffle/memory-model-operation.graffle
	omnigraffle-export -c 3 midas-graphics/graffle/memory-model-operation.graffle figures/model-operation-3.pdf

figures/model-operation-4.pdf:midas-graphics/graffle/memory-model-operation.graffle
	omnigraffle-export -c 4 midas-graphics/graffle/memory-model-operation.graffle figures/model-operation-4.pdf
