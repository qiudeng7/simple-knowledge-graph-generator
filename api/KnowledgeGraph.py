import sys
sys.path.append('/workspace/cnschema')
from cnschema import predict
import hydra

class KnowledgeGraph():
    
    def __init__(self,long_text:str):
        self.triples = []
        self.sentences = [] 
        for line in long_text.splitlines():
            sub_lines = line.split("。")
            [ self.sentences.append(sub_line) for sub_line in sub_lines if len(sub_line)>2 ]
        
        for sentence in self.sentences:
            try:
                self.get_triple_from_current_sentence(sentence)
            except:
                pass
        print(self.triples)
        
    def get_triple_from_current_sentence(self,sentence) ->tuple:
        @hydra.main(config_path="cnschema/conf", config_name='config',strict=False)
        def wrapper(cfg):            
            cfg.text = sentence
            triple = predict.main(cfg)
            self.triples.append(triple)
        wrapper()

if __name__ == "__main__":
    KnowledgeGraph('美羊羊不喜欢沸羊羊。')