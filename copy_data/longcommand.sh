am broadcast -a clipper.set -e text "文档概述：包含项目背景、项目目标、文档版本信息、目标读者、参考文档、名词解释之类的一般文档都会有的章节；整体架构：主要从整个IT层描述系统所处的位置，与周边关联系统之间的调用关系；逻辑架构：系统内部功能模块的划分以及各模块功能介绍、相互之间的关系表述；接口设计：包括系统间的接口设计以及内部功能模块之间的接口设计；数据架构：本系统与上下游系统间的数据流关系，以及本系统关键数据表设计、数据管理策略等；技术架构：实施此架构需要用到哪些技术能力，有哪些复用能力及风险；部署架构：系统如何部署，网络拓扑上有何要求，对硬件服务器有何要求，需要几台，是否需要优化服务器参数；非功能性设计：性能、高可用、可扩展性、可维护、安全性、可移植性等。其他说明：如特别约束条件、风险考虑、进度要求、政策限制、环境影响等；"

sleep 0.2
input tap 396 538
exit
