"""
Inference Engine to run the forward and backward chaining on the parsed
KnowledgeBase and ClauseBase
"""

import os

from engine.components.knowledge import Knowledge
from engine.logger.logger import Log
from engine.parser.clauseParser import ClauseParser
from engine.parser.knowledgeParser import KnowledgeBaseParser
from engine.util.constants import USER_INPUT_SEP, AVATAR, PERCENT_MATCH
from engine.util.utilities import sortDictionary


class Inference:
    """
    Inference parses the input files and creates KnowledgeBase and ClauseBase that can be
    used for forward and backward chaining

    Attributes
    -----------
    __knowledgeParser : KnowledgeBaseParser
        parser to parse the knowledge file into objects
    __clauseParser : ClauseParser
        parser to parse the clause file into objects
    __knowledgeBase : list
        list of parsed Knowledge objects
    __clauseBase : list
        list of parsed Clause objects
    __verbose : bool
        to print the matched values percents
    __method : str
        values accepted

            forward : run forward chaining
            backward : run backward chaining

    """

    def __init__(self):
        self.FORWARD = "forward"
        self.BACKWARD = "backward"

        self.__knowledgeParser = KnowledgeBaseParser()
        self.__clauseParser = ClauseParser()

        self.__knowledgeBase = None
        self.__clauseBase = None
        self.__verbose = None
        self.__method = None
        self.__userInput = None


    def startEngine(self, knowledgeBase, clauseBase, userInput, verbose=False, method="forward"):
        """
        Read the files to parse and other options. Initialize the parsers and get the parsed values

        Parameters
        ----------
        knowledgeBase : str
            name and path of the file
        clauseBase : str
            name and path of the file
        verbose : bool, default=False
            to print extra details
        method : str, default="forward"
            method to run on

        """
        if not os.path.isfile(knowledgeBase):
            Log.e(f"The knowledge file {knowledgeBase} does not exists.")
        if not os.path.isfile(clauseBase):
            Log.e(f"The clause file {clauseBase} does not exists.")

        Log.d("Parsing the files to generate a Knowledge Base...")
        self.__knowledgeBase = self.__knowledgeParser.getKnowledgeBase(knowledgeBase)
        self.__clauseBase = self.__clauseParser.getClauseBase(clauseBase)
        self.__verbose = verbose
        self.__method = method
        self.__userInput = userInput

        # asking the questions from the Clause base
        self.__askQuestion()

    def __askQuestion(self):
        """
        Ask the question iteratively from the Clause base
        """
        for clause in self.__clauseBase:
            print()
            #userInput = input(Log.modes['WARN'] + AVATAR + " >>> " + clause.getClause() + "\nYou >>> ").strip()
            
            output = self.__inferenceResolve(self.__userInput)
            if output[0]:
                Log.i(clause.getPositive() + output[1])
                self.clause = clause.getPositive() + output[1]
                self.percent = output[2]
            else:
                Log.i(clause.getNegative() + output[1])
                self.clause = clause.getNegative() + output[1]
                self.percent = output[2]

        Log.i("Espero que esteja satisfeito com a resposta!")

    def __inferenceResolve(self, userInput):
        """
        Run the inference on the user input for each clause. Method attribute determines
        the method being used

        Parameters
        ----------
        userInput : str
            input from the user

        Returns
        -------
        tuple
            bool : True for finding a match and string : A formatted string with target and percentage

        """
        userKnowledge = Knowledge()
        userInputs = self.__parseGUIInput(userInput)
        #userInputs = userInput.split(USER_INPUT_SEP)

        # creating a knowledge base of the user input
        for userIn in userInputs:
            userKnowledge.addRule("user", userIn)

        # run inference with selected method
        if self.__method == "forward":
            return self.__runForwardChain(userKnowledge)
        else:
            return self.__runBackwardChain(userKnowledge)

    def __runForwardChain(self, userBase):
        """
        Running forward chaining.Steps are as follows :

            1. Match each user rule with all the rules for each Knowledge target
            2. Calculate the percentage for each target
            3. Return the output for the percent that satisfies the Min percent
            4. If verbose is True, print all matches with percentages

        Parameters
        ----------
        userBase : Knowledge
            Knowledge object created by parsing the user input

        Returns
        -------
        tuple
            bool : True denoting match found; str : formatted target name and percentage
        """
        matchesRules = dict()

        # getting each knowledge from the base
        for knowledge in self.__knowledgeBase:
            match = 0

            # comparing each rule
            for rule in knowledge.getRules():
                for userRule in userBase.getRules():
                    if rule == userRule:
                        match += 1

            # adding the percent of match for each target
            matchesRules[knowledge.getTarget()] = (match / len(knowledge.getRules())) * 100

        # high percentage is returned based on satisfaction of MATCH
        matchesRules = sortDictionary(matchesRules)

        if self.__verbose:
            for target, percent in matchesRules.items():
                Log.d(f"Target :: {target} --->  Matched :: {percent}")
            print()

        # returning the first match if it greater than the MIN
        for target, percent in matchesRules.items():
            if percent >= PERCENT_MATCH:
                return True, target, percent
            else:
                return False, target

    def __runBackwardChain(self, userBase: Knowledge):
        """
        Running forward chaining.Steps are as follows :

            1. Scan the Knowledge Base rules with the user rule
            2. When match is found, save the Knowledge target as new target
            3. Run match on the selected targets
            4. Return the output based on the Min percent

        Parameters
        ----------
        userBase : Knowledge
            Knowledge object created by parsing the user input

        Returns
        -------
        tuple
            bool : True denoting match found; str : formatted target name and percentage
        """
        matchedTargets = list()
        matchesRules = dict()

        # finding initial target
        for knowledge in self.__knowledgeBase:
            for rule in knowledge.getRules():
                for userRule in userBase.getRules():
                    # rule match target acquired
                    if rule == userRule:
                        matchedTargets.append(knowledge)
                        break

        # running matching on the selected targets
        for matchedTarget in matchedTargets:
            match = 0
            for rule in matchedTarget.getRules():
                for userRule in userBase.getRules():
                    if rule == userRule:
                        match += 1

            # saving the target with its percent match
            matchesRules[matchedTarget.getTarget()] = (match / len(matchedTarget.getRules())) * 100

        # sorting the matched rules by the percentages
        matchesRules = sortDictionary(matchesRules)

        if self.__verbose:
            for target, percent in matchesRules.items():
                Log.d(f"Target :: {target} --->  Matched :: {percent}")
            print()

        # returning the highest matches target if is greater than the MIN
        for target, percent in matchesRules.items():
            if percent >= PERCENT_MATCH:
                return True, target ,percent
            else:
                return False, target, percent

    def __parseGUIInput(self, userInpute):
        userInput = []
        rule = userInpute

        if rule[0]:
            userInput.append("wheezing")
        if rule[1]:
            userInput.append("shortness of breath")
        if rule[2]:
            userInput.append("tight chest")
        if rule[3]:
            userInput.append("coughing")
        if rule[4]:
            userInput.append("fast breathing")
        if rule[5]:
            userInput.append("feeling drowsy")
        if rule[6]:
            userInput.append("joint pain")
        if rule[7]:
            userInput.append("tenderness")
        if rule[8]:
            userInput.append("stiffness")
        if rule[9]:
            userInput.append("inflammation")
        if rule[10]:
            userInput.append("red skin")
        if rule[11]:
            userInput.append("weakness")
        if rule[12]:
            userInput.append("bone pain")
        if rule[13]:
            userInput.append("lumps on bones")
        if rule[14]:
            userInput.append("weak bones")
        if rule[15]:
            userInput.append("fractures")     
        if rule[16]:
            userInput.append("headaches")
        if rule[17]:
            userInput.append("seizures")
        if rule[18]:
            userInput.append("fits")
        if rule[19]:
            userInput.append("mental changes")           
        if rule[20]:
            userInput.append("behavioural changes")
        if rule[21]:
            userInput.append("memory problems")
        if rule[22]:
            userInput.append("paralyses of parts of body")
        if rule[23]:
            userInput.append("fevers")
        if rule[24]:
            userInput.append("asthma")
        if rule[25]:
            userInput.append("heart pain")
        if rule[26]:
            userInput.append("mucus")
        if rule[27]:
            userInput.append("rapid heartbeat")
        if rule[28]:
            userInput.append("chest pain")
        if rule[29]:
            userInput.append("runny nose")
        if rule[30]:
            userInput.append("block nose")
        if rule[31]:
            userInput.append("sneezing")
        if rule[32]:
            userInput.append("sore throat")
        if rule[33]:
            userInput.append("throat pain")
        if rule[34]:
            userInput.append("stress")
        if rule[35]:
            userInput.append("loss of appetite")
        if rule[36]:
            userInput.append("no sleep")
        if rule[37]:
            userInput.append("mood swings")
        if rule[38]:
            userInput.append("dizziness")

        return userInput