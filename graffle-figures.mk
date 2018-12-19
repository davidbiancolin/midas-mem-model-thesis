graffle_figures := figures/memory-model-block-diagram.pdf \
	figures/model-operation-1.pdf \
	figures/model-operation-2.pdf \
	figures/model-operation-3.pdf \
	figures/model-operation-4.pdf

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
