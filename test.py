# from database import checkpointer
# from agent import config, graph
# # for item in checkpointer.list(config):
# #     print(item)
# # print(checkpointer.get_tuple(config))
# snapshot = graph.get_state_history(config)
# print(snapshot)

from tools import retreival_tool

result = retreival_tool.invoke("Who is the CEO of the company?")
print(result)