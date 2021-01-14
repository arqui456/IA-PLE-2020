import sys
from engine.inference import Inference
from GUI import Example
from PyQt5.QtWidgets import QApplication
# knowledgeBaseFile = "./data/birds/knowledge.json"
# clauseBaseFile = "./data/birds/clause.json"
#
# inferenceEngine = Inference()
# inferenceEngine.startEngine(knowledgeBaseFile,
#                             clauseBaseFile,
#                             verbose=True,
#                             method=inferenceEngine.BACKWARD)

# # for disease inference
knowledgeBaseFile = "./data/diseases/knowledge.json"
clauseBaseFile = "./data/diseases/clause.json"

ui = QApplication(sys.argv)
ex = Example()
sys.exit(ui.exec_())

print(ex.cb.isChecked())

inferenceEngine = Inference()
inferenceEngine.startEngine(knowledgeBaseFile,
                            clauseBaseFile,
                            verbose=True,
                            method=inferenceEngine.BACKWARD)
