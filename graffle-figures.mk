graffle_figures := figures/fased-block-diagram.pdf \
	figures/model-operation-1.pdf \
	figures/model-operation-2.pdf \
	figures/model-operation-3.pdf \
	figures/model-operation-4.pdf \
	figures/static-multiclock-wrapper.pdf \
	figures/gg-target.pdf \
	figures/sim-wrapper-layers.pdf \
	figures/queue-channel.pdf \
	figures/pipe-channel.pdf \
	figures/adder-example1.pdf \
	figures/adder-example2.pdf \
	figures/adder-example3.pdf \
	figures/adder-example4.pdf \
	figures/adder-example5.pdf \
	figures/libdn-wrapper.pdf \
	figures/aport-network-wrapper.pdf \
	figures/rocket-target-graph.pdf \
	figures/mapped-simulator-f1.pdf \
	figures/midas-flow.pdf

figures/fased-block-diagram.pdf:midas-graphics/graffle/memory-model-block-diagram.graffle
	omnigraffle-export -c full midas-graphics/graffle/memory-model-block-diagram.graffle figures/fased-block-diagram.pdf

figures/model-operation-1.pdf:midas-graphics/graffle/memory-model-operation.graffle
	omnigraffle-export -c 1 midas-graphics/graffle/memory-model-operation.graffle figures/model-operation-1.pdf

figures/model-operation-2.pdf:midas-graphics/graffle/memory-model-operation.graffle
	omnigraffle-export -c 2 midas-graphics/graffle/memory-model-operation.graffle figures/model-operation-2.pdf

figures/model-operation-3.pdf:midas-graphics/graffle/memory-model-operation.graffle
	omnigraffle-export -c 3 midas-graphics/graffle/memory-model-operation.graffle figures/model-operation-3.pdf

figures/model-operation-4.pdf:midas-graphics/graffle/memory-model-operation.graffle
	omnigraffle-export -c 4 midas-graphics/graffle/memory-model-operation.graffle figures/model-operation-4.pdf

figures/static-multiclock-wrapper.pdf:midas-graphics/graffle/wrapper-transforms.graffle
	omnigraffle-export -c multiclock-wrapper midas-graphics/graffle/wrapper-transforms.graffle figures/static-multiclock-wrapper.pdf

figures/gg-target.pdf:midas-graphics/graffle/midas2-target.graffle
	omnigraffle-export -c gg-target midas-graphics/graffle/midas2-target.graffle figures/gg-target.pdf

figures/sim-wrapper-layers.pdf:midas-graphics/graffle/sim-wrapper-layers.graffle
	omnigraffle-export -c wrappers midas-graphics/graffle/sim-wrapper-layers.graffle figures/sim-wrapper-layers.pdf

figures/queue-channel.pdf:midas-graphics/graffle/channel-types.graffle
	omnigraffle-export -c queue midas-graphics/graffle/channel-types.graffle figures/queue-channel.pdf

figures/pipe-channel.pdf:midas-graphics/graffle/channel-types.graffle
	omnigraffle-export -c pipe midas-graphics/graffle/channel-types.graffle figures/pipe-channel.pdf

figures/adder-example1.pdf:midas-graphics/graffle/adder-example.graffle
	omnigraffle-export -c initial-state midas-graphics/graffle/adder-example.graffle figures/adder-example1.pdf

figures/adder-example2.pdf:midas-graphics/graffle/adder-example.graffle
	omnigraffle-export -c tfire-cycle0 midas-graphics/graffle/adder-example.graffle figures/adder-example2.pdf

figures/adder-example3.pdf:midas-graphics/graffle/adder-example.graffle
	omnigraffle-export -c cycle1 midas-graphics/graffle/adder-example.graffle figures/adder-example3.pdf

figures/adder-example4.pdf:midas-graphics/graffle/adder-example.graffle
	omnigraffle-export -c inputb-fires midas-graphics/graffle/adder-example.graffle figures/adder-example4.pdf

figures/adder-example5.pdf:midas-graphics/graffle/adder-example.graffle
	omnigraffle-export -c cycle2 midas-graphics/graffle/adder-example.graffle figures/adder-example5.pdf

figures/libdn-wrapper.pdf:midas-graphics/graffle/wrapper-transforms.graffle
	omnigraffle-export -c libdn-wrapper midas-graphics/graffle/wrapper-transforms.graffle figures/libdn-wrapper.pdf

figures/aport-network-wrapper.pdf:midas-graphics/graffle/wrapper-transforms.graffle
	omnigraffle-export -c aport-network-wrapper midas-graphics/graffle/wrapper-transforms.graffle figures/aport-network-wrapper.pdf

figures/rocket-target-graph.pdf:midas-graphics/graffle/masters-target.graffle
	omnigraffle-export -c rocket-target-graph midas-graphics/graffle/masters-target.graffle figures/rocket-target-graph.pdf

figures/mapped-simulator-f1.pdf:midas-graphics/graffle/mapped-simulator.graffle
	omnigraffle-export -c f1 midas-graphics/graffle/mapped-simulator.graffle figures/mapped-simulator-f1.pdf

figures/midas-flow.pdf:midas-graphics/graffle/toolchain.graffle
	omnigraffle-export -c midas-flow midas-graphics/graffle/toolchain.graffle figures/midas-flow.pdf
