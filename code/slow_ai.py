'''
Language : Python 3.x
email : andrew@openmarmot.com
project repo : https://github.com/openmarmot/slow_ai
notes : framework for running and using slow local AIs on suboptimal hardware

'''

#import built in packages

#import external packages

#import local packages
import ai.ai_builder

# !! Note -- just testing things for now. This is far from a working release 

#---------------------------------------------------------------------------
def run():
    ai_list=[]

    # instantiate AIs 
    ai_list.append(ai.ai_builder.get_ai_object('CapyBaraHermes 2.5 Mistral 7B - GGUF'))

    question="How many roads must a man walk down?"

    # keyword search
    # - do thee search 
    selected=ai_list[0] 

    # load ai 
    selected.load()

    # generate answer 
    response=selected.generate_response(question)
    print(response)


run()