import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        if isinstance(fact,Fact) == True:
            if self.facts ==[]:
                self.facts.append(fact)
            else:
                for element in self.facts:
                    if match(element.statement,fact.statement) == True:
                        print('fact is already in kb')
                        return
                self.facts.append(fact)
                print('appended')
        else:
            print("Can only insert facts into the kb")
            return
        """Assert a fact or rule into the KB
        
        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        lob = ListOfBindings()
        for item in self.facts:
            if match(fact.statement,item.statement) != False:
                lob.add_bindings(match(fact.statement,item.statement),fact)
        if lob.list_of_bindings == []: 
            return False
        else:
            return lob    
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
