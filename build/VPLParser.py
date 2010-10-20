# $ANTLR 3.1.2 VPL.g 2010-10-21 01:49:28

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EXPONENT=21
RB=13
NUMBER=19
WHITESPACE=24
FLOAT=22
SEMICOLON=14
MIN=10
MINUS=7
MULT=8
EOF=-1
ALPHA=20
SCORE=17
COMMA=11
FUNC=4
EQUAL=15
IDENT=18
PLUS=6
LB=12
VAR=16
DIGIT=23
DIV=9
END=5

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "FUNC", "END", "PLUS", "MINUS", "MULT", "DIV", "MIN", "COMMA", "LB", 
    "RB", "SEMICOLON", "EQUAL", "VAR", "SCORE", "IDENT", "NUMBER", "ALPHA", 
    "EXPONENT", "FLOAT", "DIGIT", "WHITESPACE"
]




class VPLParser(Parser):
    grammarFileName = "VPL.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)







                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class start_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "start"
    # VPL.g:30:1: start : ( function )* ;
    def start(self, ):

        retval = self.start_return()
        retval.start = self.input.LT(1)

        root_0 = None

        function1 = None



        try:
            try:
                # VPL.g:30:7: ( ( function )* )
                # VPL.g:30:9: ( function )*
                pass 
                root_0 = self._adaptor.nil()

                # VPL.g:30:9: ( function )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == FUNC) :
                        alt1 = 1


                    if alt1 == 1:
                        # VPL.g:30:10: function
                        pass 
                        self._state.following.append(self.FOLLOW_function_in_start151)
                        function1 = self.function()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, function1.tree)


                    else:
                        break #loop1





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "start"

    class function_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "function"
    # VPL.g:32:1: function : FUNC IDENT param define statements END ;
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FUNC2 = None
        IDENT3 = None
        END7 = None
        param4 = None

        define5 = None

        statements6 = None


        FUNC2_tree = None
        IDENT3_tree = None
        END7_tree = None

        try:
            try:
                # VPL.g:32:10: ( FUNC IDENT param define statements END )
                # VPL.g:32:12: FUNC IDENT param define statements END
                pass 
                root_0 = self._adaptor.nil()

                FUNC2=self.match(self.input, FUNC, self.FOLLOW_FUNC_in_function163)

                FUNC2_tree = self._adaptor.createWithPayload(FUNC2)
                self._adaptor.addChild(root_0, FUNC2_tree)

                IDENT3=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_function165)

                IDENT3_tree = self._adaptor.createWithPayload(IDENT3)
                self._adaptor.addChild(root_0, IDENT3_tree)

                self._state.following.append(self.FOLLOW_param_in_function167)
                param4 = self.param()

                self._state.following.pop()
                self._adaptor.addChild(root_0, param4.tree)
                self._state.following.append(self.FOLLOW_define_in_function169)
                define5 = self.define()

                self._state.following.pop()
                self._adaptor.addChild(root_0, define5.tree)
                self._state.following.append(self.FOLLOW_statements_in_function171)
                statements6 = self.statements()

                self._state.following.pop()
                self._adaptor.addChild(root_0, statements6.tree)
                END7=self.match(self.input, END, self.FOLLOW_END_in_function173)

                END7_tree = self._adaptor.createWithPayload(END7)
                self._adaptor.addChild(root_0, END7_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "function"

    class param_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "param"
    # VPL.g:34:1: param : ( LB list RB )* ;
    def param(self, ):

        retval = self.param_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LB8 = None
        RB10 = None
        list9 = None


        LB8_tree = None
        RB10_tree = None

        try:
            try:
                # VPL.g:34:6: ( ( LB list RB )* )
                # VPL.g:34:8: ( LB list RB )*
                pass 
                root_0 = self._adaptor.nil()

                # VPL.g:34:8: ( LB list RB )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == LB) :
                        alt2 = 1


                    if alt2 == 1:
                        # VPL.g:34:9: LB list RB
                        pass 
                        LB8=self.match(self.input, LB, self.FOLLOW_LB_in_param181)

                        LB8_tree = self._adaptor.createWithPayload(LB8)
                        self._adaptor.addChild(root_0, LB8_tree)

                        self._state.following.append(self.FOLLOW_list_in_param183)
                        list9 = self.list()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, list9.tree)
                        RB10=self.match(self.input, RB, self.FOLLOW_RB_in_param185)

                        RB10_tree = self._adaptor.createWithPayload(RB10)
                        self._adaptor.addChild(root_0, RB10_tree)



                    else:
                        break #loop2





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "param"

    class list_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "list"
    # VPL.g:36:1: list : IDENT ( COMMA IDENT )* ;
    def list(self, ):

        retval = self.list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT11 = None
        COMMA12 = None
        IDENT13 = None

        IDENT11_tree = None
        COMMA12_tree = None
        IDENT13_tree = None

        try:
            try:
                # VPL.g:36:5: ( IDENT ( COMMA IDENT )* )
                # VPL.g:36:7: IDENT ( COMMA IDENT )*
                pass 
                root_0 = self._adaptor.nil()

                IDENT11=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_list195)

                IDENT11_tree = self._adaptor.createWithPayload(IDENT11)
                self._adaptor.addChild(root_0, IDENT11_tree)

                # VPL.g:36:13: ( COMMA IDENT )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == COMMA) :
                        alt3 = 1


                    if alt3 == 1:
                        # VPL.g:36:14: COMMA IDENT
                        pass 
                        COMMA12=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_list198)

                        COMMA12_tree = self._adaptor.createWithPayload(COMMA12)
                        self._adaptor.addChild(root_0, COMMA12_tree)

                        IDENT13=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_list200)

                        IDENT13_tree = self._adaptor.createWithPayload(IDENT13)
                        self._adaptor.addChild(root_0, IDENT13_tree)



                    else:
                        break #loop3





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "list"

    class define_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "define"
    # VPL.g:38:1: define : ( VAR list SEMICOLON )* ;
    def define(self, ):

        retval = self.define_return()
        retval.start = self.input.LT(1)

        root_0 = None

        VAR14 = None
        SEMICOLON16 = None
        list15 = None


        VAR14_tree = None
        SEMICOLON16_tree = None

        try:
            try:
                # VPL.g:38:7: ( ( VAR list SEMICOLON )* )
                # VPL.g:38:9: ( VAR list SEMICOLON )*
                pass 
                root_0 = self._adaptor.nil()

                # VPL.g:38:9: ( VAR list SEMICOLON )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == VAR) :
                        alt4 = 1


                    if alt4 == 1:
                        # VPL.g:38:10: VAR list SEMICOLON
                        pass 
                        VAR14=self.match(self.input, VAR, self.FOLLOW_VAR_in_define211)

                        VAR14_tree = self._adaptor.createWithPayload(VAR14)
                        self._adaptor.addChild(root_0, VAR14_tree)

                        self._state.following.append(self.FOLLOW_list_in_define213)
                        list15 = self.list()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, list15.tree)
                        SEMICOLON16=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_define215)

                        SEMICOLON16_tree = self._adaptor.createWithPayload(SEMICOLON16)
                        self._adaptor.addChild(root_0, SEMICOLON16_tree)



                    else:
                        break #loop4





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "define"

    class statements_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "statements"
    # VPL.g:40:1: statements : statement ( SEMICOLON statement )* ;
    def statements(self, ):

        retval = self.statements_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMICOLON18 = None
        statement17 = None

        statement19 = None


        SEMICOLON18_tree = None

        try:
            try:
                # VPL.g:40:11: ( statement ( SEMICOLON statement )* )
                # VPL.g:40:13: statement ( SEMICOLON statement )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_statement_in_statements225)
                statement17 = self.statement()

                self._state.following.pop()
                self._adaptor.addChild(root_0, statement17.tree)
                # VPL.g:40:23: ( SEMICOLON statement )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == SEMICOLON) :
                        alt5 = 1


                    if alt5 == 1:
                        # VPL.g:40:24: SEMICOLON statement
                        pass 
                        SEMICOLON18=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_statements228)

                        SEMICOLON18_tree = self._adaptor.createWithPayload(SEMICOLON18)
                        self._adaptor.addChild(root_0, SEMICOLON18_tree)

                        self._state.following.append(self.FOLLOW_statement_in_statements230)
                        statement19 = self.statement()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, statement19.tree)


                    else:
                        break #loop5





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "statements"

    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "statement"
    # VPL.g:42:1: statement : ( ( IDENT EQUAL arithmetic ) | IDENT LB list RB ) ;
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT20 = None
        EQUAL21 = None
        IDENT23 = None
        LB24 = None
        RB26 = None
        arithmetic22 = None

        list25 = None


        IDENT20_tree = None
        EQUAL21_tree = None
        IDENT23_tree = None
        LB24_tree = None
        RB26_tree = None

        try:
            try:
                # VPL.g:42:10: ( ( ( IDENT EQUAL arithmetic ) | IDENT LB list RB ) )
                # VPL.g:42:12: ( ( IDENT EQUAL arithmetic ) | IDENT LB list RB )
                pass 
                root_0 = self._adaptor.nil()

                # VPL.g:42:12: ( ( IDENT EQUAL arithmetic ) | IDENT LB list RB )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == IDENT) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == EQUAL) :
                        alt6 = 1
                    elif (LA6_1 == LB) :
                        alt6 = 2
                    else:
                        nvae = NoViableAltException("", 6, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # VPL.g:42:13: ( IDENT EQUAL arithmetic )
                    pass 
                    # VPL.g:42:13: ( IDENT EQUAL arithmetic )
                    # VPL.g:42:14: IDENT EQUAL arithmetic
                    pass 
                    IDENT20=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement243)

                    IDENT20_tree = self._adaptor.createWithPayload(IDENT20)
                    self._adaptor.addChild(root_0, IDENT20_tree)

                    EQUAL21=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_statement245)

                    EQUAL21_tree = self._adaptor.createWithPayload(EQUAL21)
                    self._adaptor.addChild(root_0, EQUAL21_tree)

                    self._state.following.append(self.FOLLOW_arithmetic_in_statement247)
                    arithmetic22 = self.arithmetic()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, arithmetic22.tree)





                elif alt6 == 2:
                    # VPL.g:42:40: IDENT LB list RB
                    pass 
                    IDENT23=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement252)

                    IDENT23_tree = self._adaptor.createWithPayload(IDENT23)
                    self._adaptor.addChild(root_0, IDENT23_tree)

                    LB24=self.match(self.input, LB, self.FOLLOW_LB_in_statement254)

                    LB24_tree = self._adaptor.createWithPayload(LB24)
                    self._adaptor.addChild(root_0, LB24_tree)

                    self._state.following.append(self.FOLLOW_list_in_statement256)
                    list25 = self.list()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, list25.tree)
                    RB26=self.match(self.input, RB, self.FOLLOW_RB_in_statement258)

                    RB26_tree = self._adaptor.createWithPayload(RB26)
                    self._adaptor.addChild(root_0, RB26_tree)







                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "statement"

    class arithmetic_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "arithmetic"
    # VPL.g:44:1: arithmetic : atom ( ( MULT | DIV ) atom )* ( ( PLUS | MINUS ) atom ( ( MULT | DIV ) atom )* )* ;
    def arithmetic(self, ):

        retval = self.arithmetic_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set28 = None
        set30 = None
        set32 = None
        atom27 = None

        atom29 = None

        atom31 = None

        atom33 = None


        set28_tree = None
        set30_tree = None
        set32_tree = None

        try:
            try:
                # VPL.g:44:12: ( atom ( ( MULT | DIV ) atom )* ( ( PLUS | MINUS ) atom ( ( MULT | DIV ) atom )* )* )
                # VPL.g:44:15: atom ( ( MULT | DIV ) atom )* ( ( PLUS | MINUS ) atom ( ( MULT | DIV ) atom )* )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_atom_in_arithmetic269)
                atom27 = self.atom()

                self._state.following.pop()
                self._adaptor.addChild(root_0, atom27.tree)
                # VPL.g:44:20: ( ( MULT | DIV ) atom )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((MULT <= LA7_0 <= DIV)) :
                        alt7 = 1


                    if alt7 == 1:
                        # VPL.g:44:21: ( MULT | DIV ) atom
                        pass 
                        set28 = self.input.LT(1)
                        if (MULT <= self.input.LA(1) <= DIV):
                            self.input.consume()
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set28))
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_atom_in_arithmetic282)
                        atom29 = self.atom()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, atom29.tree)


                    else:
                        break #loop7


                # VPL.g:44:44: ( ( PLUS | MINUS ) atom ( ( MULT | DIV ) atom )* )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if ((PLUS <= LA9_0 <= MINUS)) :
                        alt9 = 1


                    if alt9 == 1:
                        # VPL.g:44:45: ( PLUS | MINUS ) atom ( ( MULT | DIV ) atom )*
                        pass 
                        set30 = self.input.LT(1)
                        if (PLUS <= self.input.LA(1) <= MINUS):
                            self.input.consume()
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set30))
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_atom_in_arithmetic298)
                        atom31 = self.atom()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, atom31.tree)
                        # VPL.g:44:67: ( ( MULT | DIV ) atom )*
                        while True: #loop8
                            alt8 = 2
                            LA8_0 = self.input.LA(1)

                            if ((MULT <= LA8_0 <= DIV)) :
                                alt8 = 1


                            if alt8 == 1:
                                # VPL.g:44:68: ( MULT | DIV ) atom
                                pass 
                                set32 = self.input.LT(1)
                                if (MULT <= self.input.LA(1) <= DIV):
                                    self.input.consume()
                                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set32))
                                    self._state.errorRecovery = False

                                else:
                                    mse = MismatchedSetException(None, self.input)
                                    raise mse


                                self._state.following.append(self.FOLLOW_atom_in_arithmetic311)
                                atom33 = self.atom()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, atom33.tree)


                            else:
                                break #loop8




                    else:
                        break #loop9





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "arithmetic"

    class min_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "min"
    # VPL.g:46:1: min : MIN LB arithmetic COMMA arithmetic RB ;
    def min(self, ):

        retval = self.min_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MIN34 = None
        LB35 = None
        COMMA37 = None
        RB39 = None
        arithmetic36 = None

        arithmetic38 = None


        MIN34_tree = None
        LB35_tree = None
        COMMA37_tree = None
        RB39_tree = None

        try:
            try:
                # VPL.g:46:5: ( MIN LB arithmetic COMMA arithmetic RB )
                # VPL.g:46:7: MIN LB arithmetic COMMA arithmetic RB
                pass 
                root_0 = self._adaptor.nil()

                MIN34=self.match(self.input, MIN, self.FOLLOW_MIN_in_min325)

                MIN34_tree = self._adaptor.createWithPayload(MIN34)
                self._adaptor.addChild(root_0, MIN34_tree)

                LB35=self.match(self.input, LB, self.FOLLOW_LB_in_min327)

                LB35_tree = self._adaptor.createWithPayload(LB35)
                self._adaptor.addChild(root_0, LB35_tree)

                self._state.following.append(self.FOLLOW_arithmetic_in_min329)
                arithmetic36 = self.arithmetic()

                self._state.following.pop()
                self._adaptor.addChild(root_0, arithmetic36.tree)
                COMMA37=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_min331)

                COMMA37_tree = self._adaptor.createWithPayload(COMMA37)
                self._adaptor.addChild(root_0, COMMA37_tree)

                self._state.following.append(self.FOLLOW_arithmetic_in_min333)
                arithmetic38 = self.arithmetic()

                self._state.following.pop()
                self._adaptor.addChild(root_0, arithmetic38.tree)
                RB39=self.match(self.input, RB, self.FOLLOW_RB_in_min335)

                RB39_tree = self._adaptor.createWithPayload(RB39)
                self._adaptor.addChild(root_0, RB39_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "min"

    class nest_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "nest"
    # VPL.g:48:1: nest : LB arithmetic RB ;
    def nest(self, ):

        retval = self.nest_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LB40 = None
        RB42 = None
        arithmetic41 = None


        LB40_tree = None
        RB42_tree = None

        try:
            try:
                # VPL.g:48:6: ( LB arithmetic RB )
                # VPL.g:48:8: LB arithmetic RB
                pass 
                root_0 = self._adaptor.nil()

                LB40=self.match(self.input, LB, self.FOLLOW_LB_in_nest343)

                LB40_tree = self._adaptor.createWithPayload(LB40)
                self._adaptor.addChild(root_0, LB40_tree)

                self._state.following.append(self.FOLLOW_arithmetic_in_nest345)
                arithmetic41 = self.arithmetic()

                self._state.following.pop()
                self._adaptor.addChild(root_0, arithmetic41.tree)
                RB42=self.match(self.input, RB, self.FOLLOW_RB_in_nest347)

                RB42_tree = self._adaptor.createWithPayload(RB42)
                self._adaptor.addChild(root_0, RB42_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "nest"

    class atom_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "atom"
    # VPL.g:50:1: atom : ( IDENT | NUMBER | min | nest ) ;
    def atom(self, ):

        retval = self.atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT43 = None
        NUMBER44 = None
        min45 = None

        nest46 = None


        IDENT43_tree = None
        NUMBER44_tree = None

        try:
            try:
                # VPL.g:50:6: ( ( IDENT | NUMBER | min | nest ) )
                # VPL.g:50:8: ( IDENT | NUMBER | min | nest )
                pass 
                root_0 = self._adaptor.nil()

                # VPL.g:50:8: ( IDENT | NUMBER | min | nest )
                alt10 = 4
                LA10 = self.input.LA(1)
                if LA10 == IDENT:
                    alt10 = 1
                elif LA10 == NUMBER:
                    alt10 = 2
                elif LA10 == MIN:
                    alt10 = 3
                elif LA10 == LB:
                    alt10 = 4
                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # VPL.g:50:9: IDENT
                    pass 
                    IDENT43=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_atom356)

                    IDENT43_tree = self._adaptor.createWithPayload(IDENT43)
                    self._adaptor.addChild(root_0, IDENT43_tree)



                elif alt10 == 2:
                    # VPL.g:50:17: NUMBER
                    pass 
                    NUMBER44=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_atom360)

                    NUMBER44_tree = self._adaptor.createWithPayload(NUMBER44)
                    self._adaptor.addChild(root_0, NUMBER44_tree)



                elif alt10 == 3:
                    # VPL.g:50:26: min
                    pass 
                    self._state.following.append(self.FOLLOW_min_in_atom364)
                    min45 = self.min()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, min45.tree)


                elif alt10 == 4:
                    # VPL.g:50:32: nest
                    pass 
                    self._state.following.append(self.FOLLOW_nest_in_atom368)
                    nest46 = self.nest()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, nest46.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "atom"


    # Delegated rules


 

    FOLLOW_function_in_start151 = frozenset([1, 4])
    FOLLOW_FUNC_in_function163 = frozenset([18])
    FOLLOW_IDENT_in_function165 = frozenset([12, 16, 18])
    FOLLOW_param_in_function167 = frozenset([12, 16, 18])
    FOLLOW_define_in_function169 = frozenset([12, 16, 18])
    FOLLOW_statements_in_function171 = frozenset([5])
    FOLLOW_END_in_function173 = frozenset([1])
    FOLLOW_LB_in_param181 = frozenset([18])
    FOLLOW_list_in_param183 = frozenset([13])
    FOLLOW_RB_in_param185 = frozenset([1, 12])
    FOLLOW_IDENT_in_list195 = frozenset([1, 11])
    FOLLOW_COMMA_in_list198 = frozenset([18])
    FOLLOW_IDENT_in_list200 = frozenset([1, 11])
    FOLLOW_VAR_in_define211 = frozenset([18])
    FOLLOW_list_in_define213 = frozenset([14])
    FOLLOW_SEMICOLON_in_define215 = frozenset([1, 16])
    FOLLOW_statement_in_statements225 = frozenset([1, 14])
    FOLLOW_SEMICOLON_in_statements228 = frozenset([12, 16, 18])
    FOLLOW_statement_in_statements230 = frozenset([1, 14])
    FOLLOW_IDENT_in_statement243 = frozenset([15])
    FOLLOW_EQUAL_in_statement245 = frozenset([10, 12, 18, 19])
    FOLLOW_arithmetic_in_statement247 = frozenset([1])
    FOLLOW_IDENT_in_statement252 = frozenset([12])
    FOLLOW_LB_in_statement254 = frozenset([18])
    FOLLOW_list_in_statement256 = frozenset([13])
    FOLLOW_RB_in_statement258 = frozenset([1])
    FOLLOW_atom_in_arithmetic269 = frozenset([1, 6, 7, 8, 9])
    FOLLOW_set_in_arithmetic272 = frozenset([10, 12, 18, 19])
    FOLLOW_atom_in_arithmetic282 = frozenset([1, 6, 7, 8, 9])
    FOLLOW_set_in_arithmetic288 = frozenset([10, 12, 18, 19])
    FOLLOW_atom_in_arithmetic298 = frozenset([1, 6, 7, 8, 9])
    FOLLOW_set_in_arithmetic301 = frozenset([10, 12, 18, 19])
    FOLLOW_atom_in_arithmetic311 = frozenset([1, 6, 7, 8, 9])
    FOLLOW_MIN_in_min325 = frozenset([12])
    FOLLOW_LB_in_min327 = frozenset([10, 12, 18, 19])
    FOLLOW_arithmetic_in_min329 = frozenset([11])
    FOLLOW_COMMA_in_min331 = frozenset([10, 12, 18, 19])
    FOLLOW_arithmetic_in_min333 = frozenset([13])
    FOLLOW_RB_in_min335 = frozenset([1])
    FOLLOW_LB_in_nest343 = frozenset([10, 12, 18, 19])
    FOLLOW_arithmetic_in_nest345 = frozenset([13])
    FOLLOW_RB_in_nest347 = frozenset([1])
    FOLLOW_IDENT_in_atom356 = frozenset([1])
    FOLLOW_NUMBER_in_atom360 = frozenset([1])
    FOLLOW_min_in_atom364 = frozenset([1])
    FOLLOW_nest_in_atom368 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("VPLLexer", VPLParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
